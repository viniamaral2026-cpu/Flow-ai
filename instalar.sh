#!/usr/bin/env bash
# Instala o FLOW completo no Ubuntu (PT-BR):
#   assistente de voz + backend FastAPI + frontend React
# Rode em um terminal:
#   bash instalar.sh
set -e

AQUI="$(cd "$(dirname "$0")" && pwd)"
echo "== FLOW AI — instalação completa =="
echo "Pasta do projeto: $AQUI"
echo ""

# 1. Dependências do sistema (precisa de senha sudo na primeira vez)
echo "[1/5] Dependências do sistema (ffmpeg, python3-venv, alsa, nodejs)..."
command -v ffmpeg >/dev/null || sudo apt update -qq && sudo apt install -y -qq ffmpeg python3-venv alsa-utils espeak-ng 2>/dev/null | tail -1
command -v node >/dev/null || { echo "!! Instale o Node.js (requerido pro frontend)."; echo "   recomendado: usar nvm (https://github.com/nvm-sh/nvm)"; }

# 2. Ambiente virtual Python (usado por assistente + backend)
echo "[2/5] Ambiente virtual Python..."
DEST_VENV="$HOME/assistente-flow/venv"
mkdir -p "$HOME/assistente-flow"
if [ ! -x "$DEST_VENV/bin/python" ]; then
  python3 -m venv "$DEST_VENV"
fi
"$DEST_VENV/bin/pip" install -q --upgrade pip
"$DEST_VENV/bin/pip" install -q faster-whisper edge-tts vosk numpy requests \
  fastapi "uvicorn[standard]" openai pydantic python-multipart playwright chromadb
echo "      libs: whisper, edge-tts, vosk, fastapi, uvicorn, openai, playwright, chromadb"

# 3. Navegador do Playwright (Chromium) para automação
echo "      baixando Chromium do Playwright (primeira vez demora)..."
"$DEST_VENV/bin/playwright" install chromium || true

# 4. Arquivos do assistente de voz na home
echo "[3/5] Copiando assistente de voz para ~/assistente-flow ..."
cp "$AQUI/assistente.py" ~/assistente-flow/
cp "$AQUI/assistente.sh" ~/assistente-flow/
[ -d "$AQUI/modelos/vosk-pt" ] && mkdir -p ~/assistente-flow/modelos && cp -r "$AQUI/modelos/vosk-pt" ~/assistente-flow/modelos/ || true

# 5. Frontend — dependências React
echo "[4/5] Instalando dependências do frontend (npm install)..."
if command -v npm >/dev/null; then
  (cd "$AQUI/frontend" && npm install) || echo "      npm install falhou (pode rodar depois)"
fi

# 6. Serviços systemd (backend + frontend)
echo "[5/5] Criando serviços systemd do usuário..."
mkdir -p "$HOME/.config/systemd/user"
sed -e "s|@BACKEND@|$AQUI/backend|g" -e "s|@FRONTEND@|$AQUI/frontend|g" > "$HOME/.config/systemd/user/flow-backend.service" <<'SVC'
[Unit]
Description=FLOW Backend (FastAPI + NVIDIA brain)
After=network.target

[Service]
Type=simple
WorkingDirectory=@BACKEND@
Environment=DISPLAY=:0
ExecStart=/home/flow-social/assistente-flow/venv/bin/python -m uvicorn main:app --app-dir @BACKEND@ --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=3

[Install]
WantedBy=default.target
SVC
sed -e "s|@FRONTEND@|$AQUI/frontend|g" > "$HOME/.config/systemd/user/flow-frontend.service" <<'SVC'
[Unit]
Description=FLOW Frontend (Vite React)
After=network.target

[Service]
Type=simple
WorkingDirectory=@FRONTEND@
ExecStart=/home/flow-social/.nvm/versions/node/v22.23.2/bin/node @FRONTEND@/node_modules/vite/bin/vite.js --port 5173 --host
Restart=on-failure
RestartSec=3

[Install]
WantedBy=default.target
SVC
systemctl --user daemon-reload
systemctl --user enable --now flow-backend flow-frontend 2>/dev/null || true

# 7. Chave NVIDIA
if [ -z "${NVIDIA_API_KEY:-}" ]; then
  echo ""
  echo "!! NVIDIA_API_KEY não encontrada. Adicione no ~/.bashrc:"
  echo '   export NVIDIA_API_KEY="nvapi-SUA_CHAVE"'
  echo ""
fi

echo ""
echo "== Concluído! =="
echo "Frontend : http://localhost:5173"
echo "Backend  : http://localhost:8000/api/health"
echo "Voz      : ~/assistente-flow/assistente.sh   (diga \"Flow\")"
echo "Servidor : bash $AQUI/rodar.sh"
echo ""