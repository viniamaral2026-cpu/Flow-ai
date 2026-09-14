# FLOW AI — AGENTE DE INTEGRAÇÕES

## Providers
Meta/Facebook, WhatsApp, Instagram, Google, Firebase, NVIDIA, Cloudflare e outros providers aprovados.

## Regra
Usar adapters.

```text
Domain
 ↓
Service
 ↓
Provider Adapter
 ↓
External API
```

## OAuth
Validar state, redirect URI e credenciais.

## Tokens
Nunca registrar token em logs.

## Webhooks
Validar autenticidade e idempotência.

## Rate limits
Respeitar respostas do fornecedor.

## Estado
Atualizar integração para `expired`, `revoked` ou `error` quando apropriado.
