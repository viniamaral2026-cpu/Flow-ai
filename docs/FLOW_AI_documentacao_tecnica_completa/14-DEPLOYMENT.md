# FLOW AI — DEPLOYMENT

## Pipeline
```text
Git
→ CI
→ lint
→ testes
→ build
→ migration check
→ deploy
→ health check
```

## Backend
1. preparar ambiente;
2. instalar dependências;
3. configurar secrets;
4. executar migrations;
5. coletar assets quando aplicável;
6. iniciar ASGI/WSGI conforme necessidade;
7. iniciar workers;
8. validar `/health` e `/ready`.

## Frontend
Build de produção apontando para `https://api-flow-ai.flowsocial.fun`.

## Cloudflare
Validar DNS, TLS, proxy e regras.

## Rollback
Manter versão anterior implantável. Migrations incompatíveis exigem estratégia expand/contract.

## Pós-deploy
- smoke test;
- login;
- chat;
- chamada de IA;
- arquivos;
- notificações;
- integração;
- health;
- logs.

## Segredos
Nunca colocar secrets no pipeline em texto exposto ou no repositório.
