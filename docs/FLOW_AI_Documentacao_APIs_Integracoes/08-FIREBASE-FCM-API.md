# FLOW AI — FIREBASE / FCM

## Objetivo
Usar Firebase Cloud Messaging para notificações push quando adotado pela plataforma.

## Backend
```env
FIREBASE_PROJECT_ID=
FIREBASE_CLIENT_EMAIL=
FIREBASE_PRIVATE_KEY=
```

## Fluxo
```text
FLOW Event
 → NotificationService
 → FirebaseAdapter
 → FCM
 → device
```

## Registro
```http
POST /api/v1/devices/push-tokens
DELETE /api/v1/devices/push-tokens/{id}
```

## Modelo
```text
PushDevice
- user_id
- device_id
- platform
- token_protected
- enabled
- last_seen_at
```

## Segurança
Credenciais administrativas não ficam no cliente.

## Retry
Falhas transitórias podem ser reprocessadas; tokens inválidos devem ser desativados conforme resposta do provedor.
