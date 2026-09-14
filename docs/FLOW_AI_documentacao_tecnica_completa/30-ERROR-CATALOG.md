# FLOW AI — ERROR CATALOG

## Formato
```json
{
  "ok": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "...",
    "details": {}
  },
  "request_id": "uuid"
}
```

## Catálogo

### `AUTHENTICATION_REQUIRED`
Credencial ausente ou inválida.

### `PERMISSION_DENIED`
Usuário autenticado sem autorização.

### `RESOURCE_NOT_FOUND`
Recurso inexistente ou inacessível.

### `VALIDATION_ERROR`
Payload inválido.

### `CONFLICT`
Estado incompatível.

### `RATE_LIMITED`
Limite excedido.

### `PROVIDER_ERROR`
Fornecedor externo falhou.

### `PROVIDER_TIMEOUT`
Fornecedor excedeu timeout.

### `INTEGRATION_EXPIRED`
Credencial de integração expirou.

### `AI_UNAVAILABLE`
Provedor de IA indisponível.

### `TOOL_EXECUTION_FAILED`
Ferramenta não conseguiu concluir.

### `CONFIRMATION_REQUIRED`
Ação exige confirmação.

### `PLAN_LIMIT_REACHED`
Limite do plano atingido.

### `INTERNAL_ERROR`
Erro interno não exposto em detalhes ao cliente.

## Regra
Mensagens públicas não devem revelar stack trace, secrets ou detalhes internos.
