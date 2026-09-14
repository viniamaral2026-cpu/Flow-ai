# FLOW AI — flow-ai-backend

## Papel
Backend central, API, autenticação, regras de negócio e integrações.

## Stack
Django + Python

## Ecossistema
PostgreSQL, Redis, WebSocket, workers e integrações externas.

## Produto
**FLOW AI — sua inteligência pessoal que conversa, entende e age.**

Este repositório é um componente do ecossistema FLOW AI. Ele não deve duplicar
responsabilidades de outros repositórios.

## Domínios
- Web: `https://flow-ai.flowsocial.fun`
- API: `https://api-flow-ai.flowsocial.fun`

## Princípios
- segurança por padrão;
- menor privilégio;
- contratos explícitos;
- sem secrets no Git;
- não duplicação;
- testes antes de release;
- documentação sincronizada com o código.

## Estrutura esperada
Consulte `docs/ARCHITECTURE.md` e `docs/development/DEVELOPMENT.md`.
A estrutura exata deve refletir o repositório real; não criar pastas apenas para
satisfazer este documento.

## Desenvolvimento
Leia `docs/development/DEVELOPMENT.md`, `docs/development/AGENTS.md` e
`docs/development/TESTING.md` antes de contribuir.

## Segurança
Consulte `docs/SECURITY.md`. Vulnerabilidades não devem ser abertas como issue
pública antes de seguir o processo de divulgação definido pelo projeto.

## Licença
Consulte `LICENSE`. Dependências de terceiros possuem suas próprias licenças.
