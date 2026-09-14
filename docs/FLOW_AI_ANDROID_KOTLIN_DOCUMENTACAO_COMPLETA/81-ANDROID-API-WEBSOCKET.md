# Android API + WebSocket
## API
https://api-flow-ai.flowsocial.fun

## REST
HTTPS, autenticação, timeout, tratamento de HTTP errors e retry controlado.

## WebSocket
Usado quando tempo real for necessário: streaming, eventos do assistente e sincronização de estados.

## Reconexão
Backoff com limite e fechamento correto do socket no lifecycle.
