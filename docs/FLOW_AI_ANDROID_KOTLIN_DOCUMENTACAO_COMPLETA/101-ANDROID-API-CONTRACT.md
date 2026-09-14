# Contrato Android ↔ Backend
## Princípios
O cliente Android consome o contrato oficial da API. Não inventar endpoints.

## Requisitos
Versionamento, DTOs tipados, tratamento de null, paginação, erros padronizados e idempotência para operações apropriadas.

## Compatibilidade
Mudanças incompatíveis exigem versionamento ou estratégia de migração.

## WebSocket
Eventos devem possuir tipos e payloads documentados.
