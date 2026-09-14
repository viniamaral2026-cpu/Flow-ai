# FLOW AI — DEVELOPER API / API KEYS

## Base
`https://api-flow-ai.flowsocial.fun/api/v1`

## Criação
```http
POST /developer/api-keys
```

## Resposta
O segredo completo deve ser exibido somente quando criado, se esse for o modelo adotado.

## Armazenamento
Preferir armazenar hash do segredo para autenticação.

## Permissões
Exemplo:
- `chat:read`
- `chat:write`
- `memory:read`
- `memory:write`
- `files:read`
- `routines:execute`

## Headers
```http
Authorization: Bearer <api-key>
```

## Rotação
Permitir criar nova chave antes de revogar a antiga.

## Revogação
```http
DELETE /developer/api-keys/{id}
```

## Rate limit
Aplicar por usuário, aplicação e/ou chave.

## Auditoria
Registrar uso, status e origem sem armazenar o segredo.
