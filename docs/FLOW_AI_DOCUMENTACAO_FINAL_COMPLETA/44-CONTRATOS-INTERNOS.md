# FLOW AI — CONTRATOS INTERNOS ENTRE FRONTEND E BACKEND

## Objetivo
Garantir que frontend e backend evoluam de maneira coordenada.

## Contrato
O backend define:
- schemas;
- status codes;
- erros;
- autenticação;
- paginação;
- eventos.

O frontend não deve inferir formatos instáveis.

## Compatibilidade
Mudanças aditivas são preferíveis.

## Breaking change
Exige:
- nova versão;
- migration;
- comunicação;
- período de compatibilidade quando necessário.

## Request ID
Toda requisição deve possuir correlation/request ID.

## Paginação
Definir um padrão único para coleções.

## Datas
Usar formato ISO 8601 e documentar timezone.

## Upload
Definir:
- tamanho máximo;
- MIME permitido;
- armazenamento;
- processamento;
- status assíncrono.

## Streaming
Documentar protocolo, eventos, encerramento e erros.
