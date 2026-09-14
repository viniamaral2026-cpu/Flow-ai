# FLOW AI — GMAIL API

## Objetivo
Permitir leitura e ações de e-mail autorizadas pelo usuário.

## Arquitetura
```text
FLOW Agent
 → GmailService
 → GoogleAdapter
 → Gmail API
```

## Endpoints internos
```http
GET  /api/v1/integrations/gmail/messages
GET  /api/v1/integrations/gmail/messages/{id}
POST /api/v1/integrations/gmail/send
POST /api/v1/integrations/gmail/drafts
```

## Tool contract
```json
{
  "name": "gmail_send",
  "risk": "high",
  "requires_confirmation": true
}
```

## Segurança
Enviar e-mails pode exigir confirmação dependendo do nível de autonomia configurado.

## Sync
Leitura incremental deve usar mecanismos oficiais da API e evitar polling desnecessário.

## Erros
- token expirado;
- permission denied;
- quota;
- timeout;
- provider unavailable.

## Observação
Scopes e endpoints exatos devem seguir a versão atual da Gmail API.
