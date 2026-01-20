import json
import sys
from pathlib import Path
print(f"Sys importing {str(Path(__file__).parent )}")
sys.path.insert(0, str(Path(__file__).parent ))

from openai.types.beta.realtime import (InputAudioBufferAppendEvent, SessionUpdateEvent)
from openai.types.beta.realtime.session_update_event import Session, SessionTurnDetection
from typing import Any, Literal, Optional
from tools import Tool


def format_customer_profile(profile: dict) -> str:
    """Format customer profile JSON into readable text for the system prompt."""
    customer = profile.get("customer", {})
    account = profile.get("account", {})
    limits = profile.get("limits", {})
    recent = profile.get("recent_activity", {})
    prefs = profile.get("preferences", {})

    # Calculate remaining daily limit
    daily_remaining = limits.get("daily_limit", 0) - limits.get("today_spend", 0)

    lines = [
        f"**Customer:** {customer.get('name', 'Unknown')} (@{customer.get('username', 'unknown')})",
        f"**Member since:** {customer.get('member_since', 'Unknown')}",
        f"**Status:** {customer.get('status', 'unknown').title()}, Age Verified: {'Yes' if customer.get('age_verified') else 'No'}",
        "",
        f"**Favorite Teams:** {', '.join(customer.get('preferred_teams', []))}",
        f"**Favorite Leagues:** {', '.join(customer.get('preferred_leagues', []))}",
        f"**Betting Style:** {customer.get('betting_style', 'unknown').replace('_', ' ').title()}",
        f"**Risk Appetite:** {customer.get('risk_appetite', 'unknown').title()}",
        "",
        f"**Account Balance:** £{account.get('balance', 0):.2f}",
        f"**Bonus Balance:** £{account.get('bonus_balance', 0):.2f}",
        f"**Pending Bets:** {account.get('pending_bets_count', 0)} (£{account.get('pending_bets_amount', 0):.2f})",
        "",
        f"**Daily Limit:** £{limits.get('daily_limit', 0)} (£{daily_remaining} remaining today)",
        f"**Weekly Limit:** £{limits.get('weekly_limit', 0)}",
        f"**Single Bet Max:** £{limits.get('single_bet_max', 0)}",
        "",
        f"**Last Bet:** {recent.get('last_bet', {}).get('event', 'None')} - {recent.get('last_bet', {}).get('selection', '')} ({recent.get('last_bet', {}).get('result', 'pending')})",
        f"**This Month:** {recent.get('this_month', {}).get('total_bets', 0)} bets, {recent.get('this_month', {}).get('wins', 0)} wins ({recent.get('this_month', {}).get('win_rate', 0)}% win rate)",
        f"**Favorite Bet Types:** {', '.join(recent.get('favorite_bet_types', []))}",
        "",
        f"**Default Stake:** £{prefs.get('default_stake', 10)}",
        f"**Odds Format:** {prefs.get('odds_format', 'decimal').title()}",
    ]

    return "\n".join(lines)

def transform_acs_to_openai_format(msg_data: Any, model: Optional[str], tools: dict[str, Tool], system_message: Optional[str], temperature: Optional[float], max_tokens: Optional[int], disable_audio: Optional[bool], voice: str) -> InputAudioBufferAppendEvent | SessionUpdateEvent | Any | None:
    """
    Transforms websocket message data from Azure Communication Services (ACS) to the OpenAI Realtime API format.
    Args:
        msg_data_json (str): The JSON string containing the ACS message data.
    Returns:
        Optional[str]: The transformed message in the OpenAI Realtime API format
    This is needed to plug the Azure Communication Services audio stream into the OpenAI Realtime API.
    Both APIs have different message formats, so this function acts as a bridge between them.
    This method decides, if the given message is relevant for the OpenAI Realtime API, and if so, it is transformed to the OpenAI Realtime API format.
    """
    oai_message: Any = None

    # Initial message from Azure Communication Services.
    # Set the initial configuration for the OpenAI Realtime API by sending a session.update message.
    try:
        if msg_data["kind"] == "AudioMetadata":
            oai_message = {
                "type": "session.update",
                "session": {
                    "type": "realtime",
                    "tool_choice": "auto" if len(tools) > 0 else "none",
                    "tools": [tool.schema for tool in tools.values()],
                    # "turn_detection": {
                    #     "type": 'server_vad',
                    #     "threshold": 0.7, # Adjust if necessary
                    #     "prefix_padding_ms": 300, # Adjust if necessary
                    #     "silence_duration_ms": 500 # Adjust if necessary
                    # },
                }
            }

            if system_message is not None:
                oai_message["session"]["instructions"] = system_message
            # if temperature is not None:
            #     oai_message["session"]["temperature"] = temperature
            # if max_tokens is not None:
            #     oai_message["session"]["max_response_output_tokens"] = max_tokens
            # if disable_audio is not None:
            #     oai_message["session"]["disable_audio"] = disable_audio

        # Message from Azure Communication Services with audio data.
        # Transform the message to the OpenAI Realtime API format.
        elif msg_data["kind"] == "AudioData":
            oai_message = {
                "type": "input_audio_buffer.append",
                "audio": msg_data["audioData"]["data"]
            }
    except Exception as e:
        print(f"Error transforming ACS to OpenAI format: {str(msg_data)}")

    return oai_message

def transform_openai_to_acs_format(msg_data: Any) -> Optional[Any]:
    """
    Transforms websocket message data from the OpenAI Realtime API format into the Azure Communication Services (ACS) format.
    Args:
        msg_data_json (str): The JSON string containing the message data from the OpenAI Realtime API.
    Returns:
        Optional[str]: A JSON string containing the transformed message in ACS format, or None if the message type is not handled.
    This is needed to plug the OpenAI Realtime API audio stream into Azure Communication Services.
    Both APIs have different message formats, so this function acts as a bridge between them.
    This method decides, if the given message is relevant for the ACS, and if so, it is transformed to the ACS format.
    """
    acs_message = None

    # print("msg_data", msg_data)

    # Message from the OpenAI Realtime API with audio data.
    # Transform the message to the Azure Communication Services format.
    if msg_data["type"] == "response.output_audio.delta":
        acs_message = {
            "kind": "AudioData",
            "audioData": {
                "data": msg_data["delta"]
            }
        }

    # Message from the OpenAI Realtime API detecting, that the user starts speaking and interrupted the AI.
    # In this case, we don't want to send the unplayed audio buffer to the client anymore and clear the buffer audio.
    # Buffered audio is audio data that has been sent to Azure Communication Services, but not yet played by the client.
    if msg_data["type"] == "input_audio_buffer.speech_started":
        acs_message = {
            "kind": "StopAudio",
            "audioData": None,
            "stopAudio": {}
        }


    # print("acs_message", acs_message)
    return acs_message




async def load_prompt_from_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt = file.read()

    # Load and inject customer profile
    # The customer_profile.json is in the audio_backend folder
    prompt_path = Path(file_path)
    # Go up from prompts/ to project root, then into audio_backend/
    customer_profile_path = prompt_path.parent.parent / "audio_backend" / "customer_profile.json"

    if customer_profile_path.exists():
        try:
            with open(customer_profile_path, 'r', encoding='utf-8') as f:
                profile = json.load(f)
            profile_text = format_customer_profile(profile)
            prompt = prompt.replace("{{CUSTOMER_PROFILE}}", profile_text)
        except Exception as e:
            print(f"Warning: Could not load customer profile: {e}")
            prompt = prompt.replace("{{CUSTOMER_PROFILE}}", "(Customer profile not available)")
    else:
        print(f"Warning: Customer profile not found at {customer_profile_path}")
        prompt = prompt.replace("{{CUSTOMER_PROFILE}}", "(Customer profile not available)")

    return prompt
