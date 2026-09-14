# FLOW AI — WHATSAPP BUSINESS API

## Objetivo
Conectar o FLOW AI ao WhatsApp Business para recebimento e envio de mensagens dentro das permissões aprovadas.

## Arquitetura
```text
WhatsApp
 → Meta Webhook
 → FLOW API
 → validação
 → fila
 → ConversationService
 → FLOW Agent
 → resposta
 → adapter WhatsApp
```

## Endpoints internos
```http
GET  /api/v1/integrations/whatsapp
GET  /api/v1/integrations/whatsapp/authorize
POST /api/v1/integrations/whatsapp/disconnect
GET  /api/v1/integrations/whatsapp/status
POST /api/v1/webhooks/whatsapp
```

## Dados internos
- external_account_id;
- phone_number_id quando aplicável;
- access credential protegida;
- webhook status;
- scopes;
- timestamps.

## Webhook
O evento deve ser persistido antes do processamento assíncrono quando necessário.

## Idempotência
Usar identificador externo do evento/mensagem para impedir processamento duplicado.

## Mensagens
Normalizar mensagens externas para o modelo interno:
```json
{
  "provider": "whatsapp",
  "external_message_id": "...",
  "conversation_id": "...",
  "sender": "...",
  "content": "...",
  "timestamp": "..."
}
```

## Segurança
Validar autenticidade do webhook e nunca registrar tokens.

## Observação
Templates, janelas de atendimento, tipos de mensagem, permissões e limites dependem das regras atuais do produto WhatsApp Business/Meta.
