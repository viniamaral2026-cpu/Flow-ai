# Offline
## Estados
online, degraded, offline, reconnecting, session-expired.

## Offline
Permitir somente operações explicitamente suportadas offline.

## Regra
Nunca mostrar como concluída uma operação que o servidor não confirmou.

## Reconexão
Backoff exponencial, filas limitadas e operações idempotentes.
