# FLOW AI — AI AGENTS

## Arquitetura
```text
Input
→ Context
→ Memory
→ Permissions
→ Model Router
→ Planner
→ Tools
→ Confirmation
→ Executor
→ Result
```

## Context Builder
Pode combinar:
- conversa atual;
- preferências;
- memória autorizada;
- estado de dispositivos;
- integrações;
- contexto temporal.

Somente dados autorizados entram no contexto.

## Tool Registry
Cada tool declara:
- nome;
- descrição;
- schema;
- permissões;
- risco;
- timeout;
- executor.

## Autonomia
Níveis devem determinar quais ações:
- podem ocorrer automaticamente;
- exigem confirmação;
- são proibidas.

## Segurança
A IA não pode usar linguagem natural como autorização implícita para ações sensíveis.

## Auditoria
Registrar execução de ferramentas de risco relevante.
