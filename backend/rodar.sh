#!/usr/bin/env bash
# Sobe só o backend FastAPI (dentro de backend/)
set -e
BASE="$(cd "$(dirname "$0")" && pwd)"
P="$HOME/assistente-flow/venv/bin/python"
LOG="$HOME/assistente-flow/logs/backend.log"

"$P" -m uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir "$BASE" > "$LOG" 2>&1 &
echo "backend :8000 -> PID $! log:$LOG"