# Catálogo de Erros Android
## Categorias
AUTH, NETWORK, API, WEBSOCKET, VOICE, MICROPHONE, CAMERA, STORAGE, SYNC, NOTIFICATION, PERMISSION, BACKGROUND, UPDATE.

## Regra
Cada erro deve ter:
- código interno;
- mensagem técnica;
- mensagem segura ao usuário;
- ação recomendada;
- estratégia de retry;
- evento de observabilidade.

Nunca exibir stack trace ao usuário final.
