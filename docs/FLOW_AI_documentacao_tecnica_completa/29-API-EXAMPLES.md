# FLOW AI — API EXAMPLES

## Base
`https://api-flow-ai.flowsocial.fun/api/v1`

## Criar conversa
```http
POST /conversations
Authorization: Bearer <token>
Content-Type: application/json

{"title":"Minha conversa"}
```

## Enviar mensagem
```http
POST /conversations/{id}/messages
Authorization: Bearer <token>
Content-Type: application/json

{"content":"Olá FLOW"}
```

## Criar rotina
```http
POST /routines
Authorization: Bearer <token>
Content-Type: application/json

{"name":"Rotina manhã","enabled":true}
```

## Criar timer
```http
POST /timers
Authorization: Bearer <token>
Content-Type: application/json

{"duration_seconds":300}
```

## Erro
```json
{
  "ok": false,
  "error": {
    "code": "PERMISSION_DENIED",
    "message": "Ação não permitida."
  },
  "request_id": "uuid"
}
```

## Observação
Os exemplos representam o contrato-alvo. Os schemas finais devem ser gerados/validados contra o código e OpenAPI real.
