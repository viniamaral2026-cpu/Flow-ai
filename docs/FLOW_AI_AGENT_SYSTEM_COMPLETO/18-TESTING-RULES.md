# FLOW AI — REGRAS DE TESTE

## Obrigatório
Toda mudança deve ter nível de teste proporcional ao risco.

## Unit
Regras puras e serviços.

## Integration
Banco, Redis e adapters.

## API
Contrato, auth, permissions e errors.

## E2E
Fluxos críticos.

## Regressão
Bug corrigido deve ganhar teste quando apropriado.

## Testes externos
Mocks em unit/integration; ambiente controlado para testes reais.

## Resultado
Nunca mascarar falha para obter status verde.
