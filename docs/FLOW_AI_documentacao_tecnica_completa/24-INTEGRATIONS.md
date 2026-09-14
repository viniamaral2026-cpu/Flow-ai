# FLOW AI — INTEGRATIONS

## Arquitetura
```text
Integration
→ OAuth/credentials
→ Adapter
→ Provider API
→ Normalized service
```

## Estados
- disconnected;
- authorizing;
- connected;
- syncing;
- expired;
- failed;
- unavailable.

## Credenciais
Tokens devem ser protegidos e associados ao usuário correto.

## OAuth
Validar state, redirect URI, scopes e callback.

## Sync
Sincronizações longas devem ser assíncronas.

## Retry
Respeitar limites do fornecedor.

## Providers
Meta/Facebook, Google, Firebase, NVIDIA e outros devem possuir adapters independentes.
