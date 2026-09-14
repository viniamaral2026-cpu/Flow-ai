# FLOW AI --- FLOW_AI_API_CONTRACT.md

## 1. Objetivo

Contrato central das APIs do FLOW AI.

Domínio público da API:

``` text
https://api-flow-ai.flowsocial.fun
```

Frontend:

``` text
https://flow-ai.flowsocial.fun
```

Os domínios são os fornecidos para o projeto e devem ser validados no
ambiente de produção antes do go-live.

## 2. Convenções

Base:

``` text
/api/v1/
```

Formato:

``` text
application/json
```

IDs:

-   UUID recomendado;
-   nunca depender de IDs incrementais expostos quando não forem
    necessários.

Datas:

``` text
ISO 8601 / UTC
```

## 3. Resposta de sucesso

``` json
{
  "ok": true,
  "data": {},
  "request_id": "uuid"
}
```

## 4. Erro

``` json
{
  "ok": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados inválidos.",
    "details": {}
  },
  "request_id": "uuid"
}
```

## 5. Códigos HTTP

-   200 --- sucesso
-   201 --- criado
-   202 --- aceito para processamento
-   204 --- sem conteúdo
-   400 --- requisição inválida
-   401 --- não autenticado
-   403 --- sem permissão
-   404 --- não encontrado
-   409 --- conflito
-   422 --- validação
-   429 --- limite excedido
-   500 --- erro interno
-   502 --- provedor externo
-   503 --- serviço indisponível

## 6. Autenticação

Endpoints do usuário exigem autenticação.

API de desenvolvedor utiliza API Key:

``` http
Authorization: Bearer <API_KEY>
```

Nunca enviar API keys em query string.

## 7. Accounts

``` text
GET    /api/v1/me
PATCH  /api/v1/me
GET    /api/v1/me/security
POST   /api/v1/me/password
POST   /api/v1/me/2fa
DELETE /api/v1/me/sessions
```

## 8. Chat

``` text
GET    /api/v1/conversations
POST   /api/v1/conversations
GET    /api/v1/conversations/{id}
PATCH  /api/v1/conversations/{id}
DELETE /api/v1/conversations/{id}

GET    /api/v1/conversations/{id}/messages
POST   /api/v1/conversations/{id}/messages
POST   /api/v1/conversations/{id}/share
POST   /api/v1/conversations/{id}/export
```

## 9. IA

``` text
POST /api/v1/ai/chat
POST /api/v1/ai/vision
POST /api/v1/ai/execute
GET  /api/v1/ai/models
GET  /api/v1/ai/status
```

A seleção do modelo deve ser validada pelo backend.

## 10. Memória

``` text
GET    /api/v1/memories
POST   /api/v1/memories
GET    /api/v1/memories/{id}
PATCH  /api/v1/memories/{id}
DELETE /api/v1/memories/{id}
POST   /api/v1/memories/import
POST   /api/v1/memories/export
```

## 11. Voz

``` text
GET  /api/v1/voice/config
PATCH /api/v1/voice/config
POST /api/v1/voice/test
GET  /api/v1/voice/history
POST /api/v1/voice/wake-word/test
```

## 12. Rotinas

``` text
GET    /api/v1/routines
POST   /api/v1/routines
GET    /api/v1/routines/{id}
PATCH  /api/v1/routines/{id}
DELETE /api/v1/routines/{id}
POST   /api/v1/routines/{id}/test
POST   /api/v1/routines/{id}/execute
GET    /api/v1/routines/{id}/executions
```

## 13. Timers

``` text
GET    /api/v1/timers
POST   /api/v1/timers
GET    /api/v1/timers/{id}
PATCH  /api/v1/timers/{id}
DELETE /api/v1/timers/{id}
POST   /api/v1/timers/{id}/pause
POST   /api/v1/timers/{id}/resume
POST   /api/v1/timers/{id}/cancel
```

## 14. Devices

``` text
GET    /api/v1/devices
POST   /api/v1/devices
GET    /api/v1/devices/{id}
PATCH  /api/v1/devices/{id}
DELETE /api/v1/devices/{id}
POST   /api/v1/devices/{id}/pair
```

## 15. Smart Home

``` text
GET  /api/v1/home/rooms
POST /api/v1/home/rooms
GET  /api/v1/home/devices
POST /api/v1/home/scenes
POST /api/v1/home/scenes/{id}/execute
POST /api/v1/home/automations
```

## 16. Integrações

``` text
GET    /api/v1/integrations
GET    /api/v1/integrations/catalog
GET    /api/v1/integrations/{id}
POST   /api/v1/integrations/{id}/connect
PATCH  /api/v1/integrations/{id}
DELETE /api/v1/integrations/{id}
POST   /api/v1/integrations/{id}/sync
GET    /api/v1/integrations/{id}/logs
```

## 17. OAuth

Fluxo genérico:

``` text
GET /api/v1/integrations/{provider}/authorize
GET /api/v1/integrations/{provider}/callback
```

Validar `state`, redirect URI e vínculo com o usuário.

## 18. Meta / Facebook

Exemplo de arquitetura:

``` text
GET  /api/v1/integrations/meta/authorize
GET  /api/v1/integrations/meta/callback
POST /api/v1/webhooks/meta
```

O webhook deve validar o mecanismo de autenticação/verificação exigido
pelo produto Meta utilizado.

Não expor App Secret.

## 19. Firebase

Firebase administrativo não deve ser chamado diretamente pelo navegador
com credenciais privilegiadas.

O backend pode expor endpoints internos para:

``` text
POST /api/v1/notifications/push
```

e utilizar o adapter Firebase no servidor.

## 20. NVIDIA

A chamada ao provedor deve ocorrer no backend.

``` text
POST /api/v1/ai/chat
```

O cliente não deve receber:

``` text
NVIDIA_API_KEY
```

O backend resolve:

``` text
modelo → provider → NVIDIA
```

## 21. Arquivos

``` text
GET    /api/v1/files
POST   /api/v1/files
GET    /api/v1/files/{id}
PATCH  /api/v1/files/{id}
DELETE /api/v1/files/{id}
POST   /api/v1/files/{id}/share
GET    /api/v1/files/{id}/download
```

Uploads grandes podem retornar 202 e processamento assíncrono.

## 22. Skills

``` text
GET    /api/v1/skills
GET    /api/v1/skills/{id}
POST   /api/v1/skills/{id}/install
DELETE /api/v1/skills/{id}
POST   /api/v1/skills/{id}/execute
GET    /api/v1/skills/{id}/logs
POST   /api/v1/skills/{id}/publish
```

## 23. Developer

``` text
GET    /api/v1/developer/keys
POST   /api/v1/developer/keys
DELETE /api/v1/developer/keys/{id}

GET    /api/v1/developer/webhooks
POST   /api/v1/developer/webhooks
PATCH  /api/v1/developer/webhooks/{id}
DELETE /api/v1/developer/webhooks/{id}

GET    /api/v1/developer/logs
GET    /api/v1/developer/usage
```

A API Key completa deve ser exibida somente no momento seguro de
criação, se essa for a política adotada.

## 24. Billing

``` text
GET  /api/v1/billing/plans
GET  /api/v1/billing/subscription
POST /api/v1/billing/checkout
POST /api/v1/billing/upgrade
POST /api/v1/billing/downgrade
POST /api/v1/billing/cancel
POST /api/v1/billing/reactivate
GET  /api/v1/billing/payments
GET  /api/v1/billing/invoices
```

Pagamentos devem ser idempotentes.

## 25. Notifications

``` text
GET   /api/v1/notifications
POST  /api/v1/notifications/{id}/read
POST  /api/v1/notifications/read-all
DELETE /api/v1/notifications
```

## 26. Support

``` text
GET  /api/v1/support/tickets
POST /api/v1/support/tickets
GET  /api/v1/support/tickets/{id}
POST /api/v1/support/tickets/{id}/messages
POST /api/v1/support/tickets/{id}/close
POST /api/v1/support/tickets/{id}/reopen
```

## 27. Webhooks

Todo webhook externo deve:

1.  autenticar;
2.  validar assinatura quando aplicável;
3.  registrar evento;
4.  gerar idempotency key/event ID;
5.  processar;
6.  responder rapidamente;
7.  enviar processamento pesado para worker.

## 28. Rate limiting

Limites devem variar por:

-   usuário;
-   endpoint;
-   API key;
-   plano;
-   risco;
-   provedor externo.

Resposta:

``` http
429 Too Many Requests
```

## 29. Paginação

Padrão:

``` text
?page=1&page_size=20
```

Resposta:

``` json
{
  "ok": true,
  "data": {
    "items": [],
    "page": 1,
    "page_size": 20,
    "total": 0
  }
}
```

## 30. Idempotência

Endpoints sensíveis podem exigir:

``` http
Idempotency-Key: <uuid>
```

Principalmente:

-   checkout;
-   pagamentos;
-   execução de ações externas;
-   criação em provedores;
-   webhooks.

## 31. Versionamento

A API pública inicia em:

``` text
/api/v1/
```

Mudanças incompatíveis devem criar nova versão.

## 32. CORS

Permitir somente origens oficiais configuradas.

Origem principal do aplicativo:

``` text
https://flow-ai.flowsocial.fun
```

Nunca usar `*` em produção para APIs autenticadas.

## 33. OpenAPI

A API deve possuir documentação OpenAPI gerada/validada automaticamente
pelo projeto.

Documentar:

-   autenticação;
-   parâmetros;
-   schemas;
-   exemplos;
-   erros;
-   códigos HTTP;
-   rate limits.

## 34. Health checks

``` text
GET /health
GET /ready
GET /api/v1/system/status
```

`/health` deve ser simples e não expor informações sensíveis.

## 35. Regra de contrato

Frontend e backend devem compartilhar contratos estáveis.

Quando um endpoint mudar:

1.  atualizar schema;
2.  atualizar documentação;
3.  atualizar frontend;
4.  adicionar teste;
5.  validar compatibilidade;
6.  registrar mudança.

## 36. Segurança do contrato

Nunca retornar:

-   API keys;
-   secrets;
-   tokens internos;
-   credenciais de integração;
-   stack trace em produção.

Dados sensíveis devem ser minimizados nas respostas.
