# iOS Offline
## Estados
online, degraded, offline, reconnecting, session-expired.

## Regra
Não declarar sucesso sem confirmação do servidor.

## Cache
Disponibilizar somente recursos explicitamente suportados offline.

## Reconexão
Retry com backoff e operações idempotentes.
