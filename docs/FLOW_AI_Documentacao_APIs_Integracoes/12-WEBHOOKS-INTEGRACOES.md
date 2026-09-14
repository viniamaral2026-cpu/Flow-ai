# FLOW AI — WEBHOOKS DE INTEGRAÇÕES

## Endpoint
```http
POST /api/v1/webhooks/{provider}
```

## Pipeline
```text
request
→ authentication/signature
→ parse
→ event ID
→ idempotency
→ persist
→ queue
→ worker
→ domain action
```

## Segurança
Cada provider deve possuir mecanismo específico de validação.

## Idempotência
`provider + external_event_id` deve ser único quando aplicável.

## Resposta
Webhook deve responder rapidamente quando o fornecedor exigir processamento assíncrono.

## Estados
`received`, `validated`, `queued`, `processed`, `failed`, `retrying`.

## Dead Letter
Eventos persistentemente falhos devem ficar disponíveis para investigação e reprocessamento seguro.
