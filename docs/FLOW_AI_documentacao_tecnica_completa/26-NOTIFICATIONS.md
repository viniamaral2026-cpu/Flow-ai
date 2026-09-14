# FLOW AI — NOTIFICATIONS

## Canais
- in-app;
- push;
- e-mail;
- voz quando aplicável.

## Pipeline
```text
Domain Event
→ Notification Service
→ Preference check
→ Queue
→ Provider
→ Delivery status
```

## Preferências
Usuário pode controlar categorias e canais permitidos.

## Idempotência
Eventos repetidos não devem criar notificações duplicadas.

## Push
Firebase pode ser usado como adapter FCM quando adotado.

## Segurança
Não incluir dados sensíveis em notificações de lock screen sem necessidade.
