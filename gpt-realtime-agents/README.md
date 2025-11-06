# Contoso AI Commerce

Azure OpenAI Realtime-powered sales assistant that combines voice and chat to help customers find phones and plans. The application displays products visually while the AI assistant guides customers through their purchase.

**Based on:** [gpt-realtime-agents](https://github.com/samelhousseini/gpt-realtime-agents) by samelhousseini

## Architecture

- **Backend:** FastAPI serving API endpoints and static frontend
- **Frontend:** React + Vite single-page application
- **AI:** Azure OpenAI Realtime API with function calling
- **Deployment:** Docker container (frontend + backend bundled)

## Prerequisites

- Python 3.11+
- Node.js 20+
- Docker (for containerized deployment)
- Azure OpenAI Realtime API access

## Local Development

### 1. Configure Environment

```powershell
Copy-Item .env.sample .env
```

Edit `.env` and fill in your Azure OpenAI credentials:
- `AZURE_GPT_REALTIME_URL` - Your Realtime sessions endpoint
- `WEBRTC_URL` - WebRTC endpoint for your region
- `AZURE_GPT_REALTIME_KEY` - API key
- `AZURE_GPT_REALTIME_DEPLOYMENT` - Deployment name
- `AZURE_GPT_REALTIME_VOICE` - Voice selection

### 2. Install Python Dependencies

**Using uv (recommended):**
```powershell
uv venv
uv pip install -e .
```

**Using pip:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

### 3. Run Locally

```powershell
# Build frontend
cd frontend
npm ci
npm run build
cd ..

# Copy frontend to backend
Remove-Item -Recurse -Force audio_backend\frontend_dist -ErrorAction SilentlyContinue
Copy-Item -Recurse -Force frontend\dist audio_backend\frontend_dist

# Run backend
uv run uvicorn audio_backend.backend:app --host 0.0.0.0 --port 8080
```

Access the application at `http://localhost:8080`

## Docker Deployment

### Build and Run Locally

```powershell
docker build -t contoso-ai-commerce .
docker run -p 8080:8080 --env-file .env contoso-ai-commerce
```

Access at `http://localhost:8080`

### Deploy to Azure Container Apps

See `deploy/README.md` for Azure deployment instructions.

## API Endpoints

- `POST /api/session` - Create ephemeral WebRTC session
- `GET /api/tools` - List available function tools
- `POST /api/function-call` - Execute function and return result
- `GET /healthz` - Health check
- `GET /` - Serve React frontend

## Application Features

- **Voice & Chat:** Customers can speak or type
- **Visual Canvas:** Products, comparisons, and plans display on left panel
- **Shopping Cart:** Add devices, accessories, and plans
- **Function Tools:** 29 tools for device search, checkout, etc.
- **Bidirectional Sync:** Clicking products prefills chat, AI calls update visuals

## Adding Custom Tools

Edit `audio_backend/tools_registry.py` and add to `TOOLS_REGISTRY`:

```python
"your_tool_name": {
    "definition": {
        "type": "function",
        "name": "your_tool_name",
        "description": "What this tool does",
        "parameters": {
            "type": "object",
            "properties": {
                "param_name": {"type": "string"}
            }
        }
    },
    "executor": your_executor_function
}
```

The frontend automatically loads and uses new tools.

## Project Structure

```
.
├── audio_backend/          # FastAPI backend
│   ├── backend.py         # Main application
│   ├── tools_registry.py  # Function calling tools
│   └── frontend_dist/     # Built frontend (auto-generated)
├── frontend/              # React application
│   ├── src/
│   │   ├── components/    # UI components
│   │   └── hooks/         # WebRTC and session logic
│   └── package.json
├── deploy/                # Azure deployment scripts
│   ├── deploy-all-fixed.ps1
│   └── README.md
├── Dockerfile             # Multi-stage Docker build
├── .env.sample            # Environment variables template
└── README.md              # This file
```

## Development Notes

- Frontend must be rebuilt when UI changes are made
- Backend hot-reloads automatically in development
- Tools are registered in `tools_registry.py` with definitions and executors
- Visual types: `product_grid`, `comparison_table`, `plan_cards`, `promo_banner`, `cart_preview`

## Troubleshooting

**"Module not found" errors:**
```powershell
pip install -e .
```

**Frontend not updating:**
```powershell
cd frontend && npm run build
cd .. && Copy-Item -Recurse -Force frontend\dist audio_backend\frontend_dist
```

**Docker build fails:**
- Ensure Docker Desktop is running
- Check `.env` file exists

**Container App deployment fails:**
- See `deploy/README.md` troubleshooting section
- Check Azure OpenAI credentials in `.env`

## Credits

This project is based on [gpt-realtime-agents](https://github.com/samelhousseini/gpt-realtime-agents) by [samelhousseini](https://github.com/samelhousseini).

Licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
