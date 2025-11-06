# Contoso AI Commerce - Frontend

React application for the Contoso AI Commerce sales assistant. Provides voice and chat interface with visual product displays.

## Tech Stack

- React 19 + TypeScript
- Vite 6
- Tailwind CSS 4
- Radix UI components
- WebRTC for voice

## Development

### Install Dependencies

```bash
npm install
```

### Run Development Server

```bash
npm run dev
```

Application runs on `http://localhost:5173` by default.

### Build for Production

```bash
npm run build
```

Output goes to `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

## Configuration

Set backend URL in `.env.local`:

```
VITE_BACKEND_BASE_URL=http://localhost:8080/api
```

If not set, defaults to `http://localhost:8080/api`.

## Project Structure

```
src/
├── App.tsx                      # Main application
├── components/
│   ├── contoso/                 # Business components
│   │   ├── DynamicVisualCanvas.tsx
│   │   ├── ProductCard.tsx
│   │   ├── CartIcon.tsx
│   │   └── ...
│   ├── visual-primitives/       # Reusable visual components
│   ├── CallControls.tsx         # Voice/chat controls
│   ├── ChatComposer.tsx         # Message input
│   ├── MessageBubble.tsx        # Chat messages
│   └── ui/                      # Base UI components
├── hooks/
│   ├── use-realtime-session.ts  # WebRTC + function calling
│   └── use-voice-activity.ts    # Voice activity detection
├── lib/
│   ├── constants.ts             # Config and prompts
│   ├── types.ts                 # TypeScript types
│   └── utils.ts                 # Utilities
└── main.css                     # Tailwind imports
```

## Available Scripts

- `npm run dev` - Development server with hot reload
- `npm run build` - Production build
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Requirements

- Node.js 20+
- Modern browser with WebRTC support
- Microphone access for voice features

## Notes

- Frontend must be rebuilt when making changes
- Backend must be running for the app to function
- Visual updates are driven by tool responses with `_visual` metadata
