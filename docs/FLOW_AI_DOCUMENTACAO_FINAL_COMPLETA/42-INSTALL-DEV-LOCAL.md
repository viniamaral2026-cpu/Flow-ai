# FLOW AI — INSTALAÇÃO DO AMBIENTE DE DESENVOLVIMENTO

## Pré-requisitos
- Git;
- Python;
- Node.js;
- PostgreSQL;
- Redis;
- gerenciador de pacotes;
- editor/IDE.

## Backend
```bash
git clone <repository>
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Variáveis
Copiar `.env.example` para `.env` e preencher somente credenciais de desenvolvimento.

## Worker
Executar worker conforme tecnologia adotada.

## Frontend
```bash
cd frontend
npm install
npm run dev
```

## URLs
Frontend:
`https://flow-ai.flowsocial.fun`

API:
`https://api-flow-ai.flowsocial.fun`

No ambiente local, usar URLs locais apropriadas.

## Checklist
- banco acessível;
- Redis acessível;
- migrations;
- backend;
- worker;
- frontend;
- health;
- login;
- API.

## Regra
Nunca usar secrets de produção no ambiente local.
