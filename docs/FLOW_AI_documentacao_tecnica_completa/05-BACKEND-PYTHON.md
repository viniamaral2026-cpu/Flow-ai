# FLOW AI — BACKEND PYTHON

## Padrões
- Python com versão suportada e fixada;
- type hints;
- lint;
- formatter;
- testes;
- logging estruturado;
- funções coesas.

## Serviços
`AIService`, `MemoryService`, `RoutineService`, `IntegrationService`, `BillingService`, `NotificationService`.

## Adapters
Cada fornecedor externo possui adapter isolado.

```text
integrations/
├── nvidia/
├── firebase/
├── cloudflare/
├── meta/
├── google/
└── payments/
```

## Agente
```text
input
→ context
→ memory
→ permissions
→ model routing
→ planning
→ confirmation
→ tool execution
→ result
```

## Ferramentas
Cada ferramenta declara schema de entrada, permissão, nível de risco, timeout e handler.

## Confiabilidade
Timeout obrigatório, retries seguros, idempotência e tratamento de indisponibilidade.

## Secrets
Somente environment/secret manager.
