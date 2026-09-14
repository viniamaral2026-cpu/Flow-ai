# FLOW AI — PLATAFORMA DE IA

## Arquitetura
```text
Input
→ Context Builder
→ Memory Retrieval
→ Permission Engine
→ Model Router
→ Agent
→ Tool Planner
→ Confirmation
→ Executor
→ Result
→ Memory/Event
```

## Model Router
Seleciona provider/modelo conforme:
- capacidade;
- latência;
- custo;
- disponibilidade;
- plano;
- política de segurança.

## Context
Pode incluir:
- conversa atual;
- memória autorizada;
- hora/data;
- preferências;
- integrações;
- estado de dispositivos.

## Tools
Toda ferramenta deve possuir:
- schema;
- permissões;
- risco;
- timeout;
- executor;
- resultado estruturado.

## Autonomia
### Baixa
Quase todas as ações externas exigem confirmação.

### Média
Ações de baixo risco podem ser automáticas.

### Alta
Mais ações podem ser automáticas, mantendo bloqueios de segurança.

## Guardrails
A FLOW não deve executar ação proibida apenas porque o modelo solicitou.

## Fallback
Falha do provider deve produzir erro controlado ou provider alternativo, quando configurado.

## Observabilidade
Métricas de latência, erro e consumo. Nunca registrar secrets.
