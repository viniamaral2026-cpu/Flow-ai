# Offline e Recuperação

## Estados
online, degraded, offline, reconnecting, authenticated e session-expired.

## Offline
Permitir apenas operações que tenham suporte local seguro. Não fingir sucesso de uma operação que não foi confirmada pelo servidor.

## Reconexão
Usar backoff e sincronização controlada.

## Conflitos
Usar IDs, versões e timestamps. Operações críticas devem ser idempotentes.

## Recuperação
Após queda do aplicativo, restaurar apenas estado seguro e necessário.
