# Desktop — REST e WebSocket

## API
Base oficial:
`https://api-flow-ai.flowsocial.fun`

## Web
Aplicação:
`https://flow-ai.flowsocial.fun`

## REST
Usar HTTPS, autenticação, versionamento, timeouts, retry controlado e tratamento de códigos HTTP.

## WebSocket
Usar para experiências em tempo real como streaming, estado do assistente e eventos necessários.

## Reconexão
Backoff exponencial com limite. Evitar loops agressivos.

## Sessão
Detectar token expirado e conduzir reautenticação sem perder a conversa quando possível.

## Erros
Converter respostas de infraestrutura em mensagens úteis para o usuário sem expor stack traces.
