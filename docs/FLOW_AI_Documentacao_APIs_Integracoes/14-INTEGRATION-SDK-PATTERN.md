# FLOW AI — PADRÃO DE IMPLEMENTAÇÃO DOS ADAPTERS

## Interface
Cada integração deve implementar contrato semelhante:

```python
class IntegrationAdapter:
    async def connect(self, context): ...
    async def disconnect(self, context): ...
    async def health(self, context): ...
```

## Cliente HTTP
Centralizar:
- timeout;
- headers;
- retry;
- tracing;
- error mapping.

## Error mapping
```text
Provider 401 → IntegrationCredentialExpired
Provider 403 → IntegrationPermissionDenied
Provider 404 → ExternalResourceNotFound
Provider 429 → ProviderRateLimited
Provider 5xx → ProviderUnavailable
timeout → ProviderTimeout
```

## Testes
Cada adapter deve possuir:
- unit tests;
- contract tests;
- mock provider;
- tratamento de erros;
- teste de token expirado;
- teste de retry/idempotência.

## Regra
Nenhum módulo de domínio deve importar diretamente SDK específico do fornecedor.
