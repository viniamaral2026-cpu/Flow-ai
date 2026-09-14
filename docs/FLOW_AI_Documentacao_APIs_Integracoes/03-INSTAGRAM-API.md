# FLOW AI — INSTAGRAM API

## Objetivo
Permitir integração autorizada com recursos do Instagram suportados pelo produto Meta.

## Fluxo
```text
Instagram
 → Meta authorization
 → FLOW callback
 → token
 → Integration
 → Graph API
```

## Endpoints internos
```http
GET  /api/v1/integrations/instagram
GET  /api/v1/integrations/instagram/authorize
GET  /api/v1/integrations/instagram/callback
GET  /api/v1/integrations/instagram/status
POST /api/v1/integrations/instagram/disconnect
POST /api/v1/webhooks/instagram
```

## DM
Quando o produto/permissão suportar mensagens:
```text
Instagram DM
 → webhook
 → normalize
 → conversation
 → FLOW Agent
 → response
```

## Segurança
- OAuth state;
- tokens protegidos;
- scopes mínimos;
- validação de webhook.

## Observação
Capacidades disponíveis variam conforme tipo de conta, produto Meta e permissões aprovadas. Validar documentação vigente antes da implementação.
