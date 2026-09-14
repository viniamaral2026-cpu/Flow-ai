# FLOW AI — REGRAS DE DEPLOY

## Pré-deploy
- CI verde;
- build;
- migrations avaliadas;
- secrets;
- changelog;
- rollback.

## Deploy
```text
validate
→ release
→ migrate safely
→ deploy
→ health
→ smoke
```

## Produção
Alterações críticas exigem autorização.

## Rollback
Deve existir procedimento para código e, quando possível, estratégia de banco compatível.

## Pós-deploy
Monitorar erros e métricas.

## Falha
Interromper promoção ou fazer rollback conforme runbook.
