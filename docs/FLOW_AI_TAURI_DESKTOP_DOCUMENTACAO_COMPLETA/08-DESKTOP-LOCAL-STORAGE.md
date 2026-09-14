# Armazenamento Local

## Usos
Preferências, cache, estado de sessão não sensível e dados temporários.

## Não armazenar em texto puro
Senhas, refresh tokens, chaves privadas, API keys ou outros segredos.

## SQLite
Pode ser utilizado para cache/offline controlado quando necessário. Deve possuir migrações versionadas.

## Sincronização
O servidor é fonte de verdade para dados sincronizados. O cliente deve lidar com conflito, timestamp/versionamento e retry idempotente.

## Limpeza
Usuário deve conseguir limpar cache local. Logout deve invalidar dados locais sensíveis.
