# FLOW AI — FIREBASE

## Uso
Firebase pode complementar o backend em autenticação, push notifications e serviços mobile conforme a arquitetura adotada.

## Credenciais
Credenciais administrativas ficam exclusivamente no backend/secret manager.

Variáveis exemplificativas:
```env
FIREBASE_PROJECT_ID=
FIREBASE_CLIENT_EMAIL=
FIREBASE_PRIVATE_KEY=
```

## Push
Fluxo:
```text
evento FLOW
→ NotificationService
→ Firebase adapter
→ FCM
→ dispositivo
```

## Autenticação
Se Firebase Auth for utilizado, o backend deve validar tokens no servidor e mapear a identidade para o usuário interno.

## Regras
Não colocar service-account credentials no frontend.

## Ambientes
Projetos/credenciais de desenvolvimento e produção devem ser separados quando aplicável.
