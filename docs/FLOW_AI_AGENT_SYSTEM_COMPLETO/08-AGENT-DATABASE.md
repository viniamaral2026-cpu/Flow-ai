# FLOW AI — AGENTE DE BANCO

## Regras
Antes de alterar banco:
1. localizar modelo;
2. verificar migration;
3. verificar relações;
4. verificar consumidores;
5. avaliar dados existentes.

## Migration
Toda alteração estrutural deve possuir migration.

## Segurança
Nunca executar DROP/DELETE amplo em produção sem autorização explícita.

## Integridade
Preferir constraints e foreign keys para invariantes importantes.

## Performance
Avaliar índices e queries.

## Rollback
Toda alteração de risco deve possuir estratégia de reversão.
