# FLOW AI — OPENAPI / SWAGGER

## Objetivo
A especificação OpenAPI é a fonte técnica do contrato HTTP publicado pelo backend.

## Base
`https://api-flow-ai.flowsocial.fun/api/v1`

## Estrutura
```text
openapi/
├── openapi.yaml
├── schemas/
├── responses/
├── security/
└── examples/
```

## Recursos
A especificação deve documentar:
- accounts;
- conversations;
- messages;
- AI;
- memories;
- voice;
- routines;
- timers;
- devices;
- home;
- integrations;
- skills;
- files;
- health;
- recipes;
- notifications;
- billing;
- developer;
- support;
- system.

## Cada endpoint
Deve possuir:
- método;
- path;
- descrição;
- autenticação;
- parâmetros;
- request body;
- response;
- status codes;
- schema;
- exemplos;
- erros;
- rate limit quando relevante.

## Segurança
Definir esquemas de autenticação de forma explícita.

## CI
O contrato deve ser validado no CI e alterações incompatíveis devem ser detectadas.

## Regra
Documentação não pode declarar endpoint inexistente como implementado. O OpenAPI real deve ser sincronizado com o código.
