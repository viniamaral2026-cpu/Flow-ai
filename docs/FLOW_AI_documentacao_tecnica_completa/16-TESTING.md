# FLOW AI — TESTING

## Pirâmide
- unitários;
- service/domain;
- API;
- integração;
- E2E;
- smoke.

## Unitários
Validar regras sem dependência externa.

## API
Testar:
- autenticação;
- autorização;
- validação;
- paginação;
- erros;
- rate limit;
- idempotência.

## Integrações
Usar mocks/fixtures para testes automatizados e testes reais controlados em staging.

## IA
Testar:
- routing;
- timeout;
- provider error;
- tool selection;
- confirmação;
- respostas estruturadas.

## E2E
Fluxos críticos:
- signup/login;
- onboarding;
- chat;
- ação;
- rotina;
- integração;
- assinatura;
- recuperação.

## Segurança
Testar exposição de secrets, autorização horizontal, CSRF/CORS e uploads.

## Definition of Done
Nenhuma funcionalidade crítica entra em produção sem testes correspondentes.
