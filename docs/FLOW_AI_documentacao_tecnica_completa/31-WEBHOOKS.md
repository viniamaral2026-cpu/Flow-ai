# FLOW AI — WEBHOOKS

## Arquitetura
```text
Provider
→ HTTPS endpoint
→ authenticate
→ validate
→ persist event
→ idempotency check
→ queue
→ worker
→ domain update
```

## Endpoint
`POST /api/v1/webhooks/{provider}`

## Segurança
Validar assinatura/token conforme o fornecedor.

## Idempotência
Persistir identificador único do evento.

## Retry
Responder rapidamente quando o fornecedor exigir; processamento pesado ocorre no worker.

## Estados
- received;
- validated;
- queued;
- processed;
- failed;
- retrying.

## Observabilidade
Registrar provider, event ID, status, duração e request ID, sem conteúdo secreto.

## Dead letter
Eventos que excederem tentativas devem ser encaminhados para fila de erro para investigação.
