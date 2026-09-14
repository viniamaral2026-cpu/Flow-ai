# FLOW AI — OBSERVABILITY

## Logs
Estruturados e correlacionados por request ID.

## Métricas
- request count;
- error rate;
- latency;
- queue depth;
- worker failures;
- DB latency;
- provider latency;
- AI usage.

## Tracing
Propagar correlation/request ID entre serviços.

## Alertas
- 5xx elevado;
- API indisponível;
- fila crescendo;
- banco indisponível;
- integração crítica falhando;
- falha de deploy.

## Privacidade
Não registrar passwords, tokens, API keys ou conteúdo sensível sem justificativa.

## Dashboards
Separar:
- aplicação;
- infraestrutura;
- IA;
- integrações;
- billing;
- segurança.
