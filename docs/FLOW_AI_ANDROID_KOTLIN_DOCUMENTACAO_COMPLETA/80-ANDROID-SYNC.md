# Synchronization
## Objetivo
Manter dados do usuário consistentes entre Android, web e desktop.

## Estratégia
IDs estáveis, versionamento, timestamps e regras explícitas de conflito.

## Conflitos
Operações críticas devem preferir confirmação server-side.

## Retry
Usar idempotency keys quando aplicável para evitar duplicação.
