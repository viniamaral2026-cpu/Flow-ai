# FLOW AI — DEVOPS

## CI/CD
Stages:
1. checkout;
2. dependency install;
3. lint;
4. unit tests;
5. integration tests;
6. build;
7. security checks;
8. deploy;
9. smoke test.

## Branches
Definir política de branches e proteção de `main`.

## Containers
Se Docker for adotado:
- imagem mínima;
- usuário não-root;
- dependências fixadas;
- healthcheck;
- secrets externos.

## Infraestrutura
Documentar origem da API, banco, Redis, workers, storage e edge.

## Backups
Testar restauração, não apenas criação de backup.

## Migrations
Nunca apagar dados em produção sem procedimento aprovado.

## Observabilidade
Alertas para:
- erro 5xx;
- latência;
- saturação;
- filas;
- banco;
- integrações;
- falha de deploy.

## Disaster recovery
Definir RPO/RTO, responsáveis e procedimento de restauração.
