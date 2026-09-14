# Estratégia de Testes

## Objetivo
Validar o comportamento real de flow-ai-infrastructure antes de merge/release.

## Níveis
- unitários;
- integração;
- contrato;
- UI/E2E quando aplicável;
- segurança;
- performance;
- smoke de release.

## Regra
Não marcar teste como aprovado sem executá-lo.

## Regressão
Toda correção de bug relevante deve considerar teste de regressão.

## Release
Executar o conjunto mínimo definido pelo pipeline real do repositório e registrar
os resultados.
