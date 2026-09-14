#!/usr/bin/env bash
# Sobe o FLOW completo a partir desta pasta (server):
#   backend  :8000  +  frontend :5173
set -e
BASE="$(cd "$(dirname "$0")" && pwd)"
P="$HOME/assistente-flow/venv/bin/python"
NODE_BIN="$(command -v node)"
LOG="$HOME/assistente-flow/logs"
mkdir -p "$LOG"

echo "== FLOW server =="
echo "base: $BASE"

# Frontend: garante dependências
if [ ! -d "$BASE/frontend/node_modules" ]; then
  echo "[frontend] npm install (primeira vez)..."
  (cd "$BASE/frontend" && npm install) || true
fi

echo "[backend] iniciando em :8000 ..."
nohup "$P" -m uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir "$BASE/backend" \
  > "$LOG/backend.log" 2>&1 &
echo $! > "$LOG/backend.pid"

echo "[frontend] iniciando em :5173 ..."
  (cd "$BASE/frontend" && nohup "$NODE_BIN" "$BASE/frontend/node_modules/vite/bin/vite.js" --port 5173 --host \
    > "$LOG/frontend.log" 2>&1 &)
  echo $! > "$LOG/frontend.pid"

sleep 4
echo ""
echo "Backend : http://localhost:8000/api/health"
echo "Frontend: http://localhost:5173"
echo "Parar   : kill \$(cat $LOG/backend.pid) \$(cat $LOG/frontend.pid)"
echo "Alternativa via systemd: systemctl --user start flow-backend flow-frontend"