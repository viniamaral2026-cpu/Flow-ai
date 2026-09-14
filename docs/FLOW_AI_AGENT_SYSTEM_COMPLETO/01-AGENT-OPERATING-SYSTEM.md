# FLOW AI — AGENT OPERATING SYSTEM

## Ciclo de execução

### Fase 1 — Entendimento
Extrair objetivo, restrições, arquivos envolvidos e critérios de aceite.

### Fase 2 — Descoberta
Pesquisar documentação, árvore do projeto, rotas, componentes, services, endpoints e banco.

### Fase 3 — Plano
Definir alterações mínimas e dependências.

### Fase 4 — Execução
Alterar somente o escopo necessário.

### Fase 5 — Validação
Executar testes adequados.

### Fase 6 — Auditoria
Verificar regressões, duplicação e segurança.

### Fase 7 — Registro
Atualizar documentação quando o comportamento mudou.

## Estados da tarefa
`PLANNED → IN_PROGRESS → VALIDATING → DONE`  
ou `BLOCKED` quando existir dependência não resolvida.

## Bloqueio
O agente deve parar e reportar quando faltar autorização, informação essencial ou recurso necessário.
