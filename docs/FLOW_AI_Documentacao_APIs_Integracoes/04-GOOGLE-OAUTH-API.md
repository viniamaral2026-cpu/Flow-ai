# FLOW AI — GOOGLE OAUTH

## Objetivo
Base comum para Gmail, Calendar, Drive e demais serviços Google.

## Variáveis
```env
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REDIRECT_URI=
```

## Fluxo
```text
FLOW
 → Google OAuth
 → callback
 → validar state
 → token exchange
 → encrypted credential
 → Integration
```

## Segurança
- não expor client secret;
- validar state;
- redirect URI exato;
- scopes mínimos;
- revogação;
- refresh token protegido.

## Modelo
```text
GoogleCredential
- user_id
- provider_account_id
- scopes
- access_token_encrypted
- refresh_token_encrypted
- expires_at
```

## Endpoints internos
```http
GET  /api/v1/integrations/google/authorize
GET  /api/v1/integrations/google/callback
GET  /api/v1/integrations/google/status
POST /api/v1/integrations/google/disconnect
```
