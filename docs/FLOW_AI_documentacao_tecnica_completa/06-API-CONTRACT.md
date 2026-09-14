# FLOW AI — API CONTRACT

## Base
`https://api-flow-ai.flowsocial.fun/api/v1`

## Formato
JSON + UTF-8. Datas em ISO 8601/UTC.

## Sucesso
```json
{"ok":true,"data":{},"request_id":"uuid"}
```

## Erro
```json
{"ok":false,"error":{"code":"VALIDATION_ERROR","message":"Dados inválidos","details":{}},"request_id":"uuid"}
```

## HTTP
200, 201, 202, 204, 400, 401, 403, 404, 409, 422, 429, 500, 502, 503.

## Recursos principais
```text
/accounts
/conversations
/messages
/ai
/memories
/voice
/routines
/timers
/devices
/home
/integrations
/skills
/files
/health
/recipes
/notifications
/billing
/developer
/support
/system
```

## Headers
```http
Authorization: Bearer <token>
Content-Type: application/json
X-Request-ID: <uuid>
Idempotency-Key: <uuid>
```

`Idempotency-Key` deve ser usado em operações críticas quando suportado.

## Versionamento
Mudança incompatível exige `/api/v2`.

## CORS
Produção deve permitir apenas origens explicitamente autorizadas.
