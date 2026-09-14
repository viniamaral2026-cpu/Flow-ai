# FLOW AI — MATRIZ DE PERMISSÕES MCP

| Operação | Risco | Regra |
|---|---|---|
| READ | baixo | permitida no escopo |
| ANALYZE | baixo | permitida no escopo |
| CREATE | médio | validar escopo |
| UPDATE | médio | validar impacto |
| DELETE | alto | confirmação explícita |
| DATABASE WRITE | alto | validação adicional |
| PRODUCTION DEPLOY | crítico | autorização explícita |
| DNS | crítico | autorização explícita |
| SECRETS | crítico | nunca expor |
| BILLING | alto | validação e auditoria |

## Princípio
Permissão para ler não implica permissão para alterar.

Permissão para alterar código não implica permissão para deploy.

Permissão para executar ferramenta não implica autorização para qualquer recurso acessível por ela.
