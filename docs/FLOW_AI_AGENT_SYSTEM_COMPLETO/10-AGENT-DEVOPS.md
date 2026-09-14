# FLOW AI — AGENTE DEVOPS

## Escopo
CI/CD, containers, ambientes, Cloudflare, deploy, observabilidade e rollback.

## Regras
- produção separada;
- secrets externos;
- health check;
- deploy reproduzível;
- rollback conhecido;
- migrations seguras.

## Deploy
```text
CI
→ tests
→ build
→ migration validation
→ deploy
→ health
→ smoke
```

## Proibição
Não alterar DNS, produção ou credenciais críticas sem autorização adequada.
