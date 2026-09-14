# FLOW AI — META / FACEBOOK API

## Finalidade
Permitir que o FLOW AI integre recursos autorizados do ecossistema Meta.

## Componentes
- Meta App;
- App ID;
- App Secret;
- OAuth;
- Access Tokens;
- Webhooks;
- Graph API;
- permissões/scopes.

## Variáveis
```env
META_APP_ID=
META_APP_SECRET=
META_REDIRECT_URI=
META_VERIFY_TOKEN=
```

## OAuth
```text
FLOW
 → autorização Meta
 → callback
 → validar state
 → trocar código/token
 → armazenar credencial protegida
 → Integration.connected
```

## Endpoints internos
```http
GET  /api/v1/integrations/meta
GET  /api/v1/integrations/meta/authorize
GET  /api/v1/integrations/meta/callback
POST /api/v1/integrations/meta/disconnect
GET  /api/v1/integrations/meta/status
```

## Webhook
```http
POST /api/v1/webhooks/meta
```

O backend deve validar o mecanismo de verificação/assinatura exigido pela Meta antes de processar eventos.

## Segurança
O App Secret permanece exclusivamente no backend.

## Observação
Facebook, Instagram e WhatsApp possuem produtos, permissões e requisitos próprios. Não assumir que uma autorização cobre todos os produtos.

## Produção
As permissões, versões da Graph API, requisitos de revisão do aplicativo e limites devem ser conferidos na documentação oficial vigente antes do go-live.
