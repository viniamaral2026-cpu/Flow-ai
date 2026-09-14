# FLOW AI — BACKEND DJANGO

## Apps
`accounts`, `chat`, `ai`, `memory`, `voice`, `vision`, `routines`, `timers`, `devices`, `smart_home`, `integrations`, `skills`, `files`, `health`, `recipes`, `notifications`, `billing`, `developer`, `audit`, `support`, `system`.

## Estrutura
```text
backend/
├── manage.py
├── config/
├── apps/
├── core/
├── services/
├── integrations/
├── workers/
└── tests/
```

## DRF
Views/ViewSets recebem requests; serializers validam entrada/saída; services executam regras; ORM persiste dados.

## Segurança
- `ALLOWED_HOSTS`;
- CORS restritivo;
- CSRF conforme autenticação;
- cookies Secure/HttpOnly/SameSite;
- HSTS;
- rate limiting;
- permissões por objeto;
- auditoria.

## Banco
PostgreSQL como banco transacional.

## Async
Celery/worker + Redis para jobs longos.

## ASGI
Usar ASGI para WebSockets e concorrência quando aplicável.

## Migrations
Toda alteração de schema deve possuir migration versionada e testada.

## Health
`/health` e `/ready` não devem revelar segredos.
