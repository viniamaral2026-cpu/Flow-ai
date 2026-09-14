# FLOW AI — AGENTE DE IA

## Pipeline
```text
Input
→ Context
→ Memory
→ Permissions
→ Model Router
→ Agent
→ Tools
→ Confirmation
→ Execution
→ Result
```

## Provider
Usar abstração `AIProvider`.

## NVIDIA
Quando NVIDIA for provider configurado:
- chave somente no backend;
- timeout;
- retry seguro;
- limites;
- observabilidade.

## Tools
Cada tool deve declarar:
- schema;
- permissão;
- risco;
- confirmação;
- timeout.

## Segurança
O modelo não possui autoridade própria. A autorização vem da camada de políticas.

## Prompt injection
Conteúdo externo não deve substituir instruções de sistema ou políticas de segurança.
