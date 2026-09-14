# Contrato de Integração

## Regra
Este documento descreve princípios; endpoints concretos devem ser copiados do
contrato OpenAPI/API real do projeto, nunca inventados.

## Requisitos
- autenticação;
- autorização;
- versionamento;
- timeout;
- tratamento padronizado de erros;
- paginação quando aplicável;
- idempotência para operações apropriadas;
- compatibilidade entre versões.

## WebSocket
Eventos devem possuir tipos e payloads documentados.

## Compatibilidade
Mudanças breaking exigem versionamento ou migração coordenada.
