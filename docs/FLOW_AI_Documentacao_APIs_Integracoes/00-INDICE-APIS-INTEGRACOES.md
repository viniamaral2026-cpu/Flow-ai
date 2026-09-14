# FLOW AI — DOCUMENTAÇÃO DE APIs E INTEGRAÇÕES

## Objetivo
Documentação técnica das integrações externas e dos adapters internos do FLOW AI.

## Domínios
- API interna: `https://api-flow-ai.flowsocial.fun/api/v1`
- Frontend: `https://flow-ai.flowsocial.fun`

## Integrações cobertas
1. Meta/Facebook
2. WhatsApp Business
3. Instagram
4. Google
5. Gmail
6. Google Calendar
7. Google Drive
8. Firebase / FCM
9. NVIDIA AI
10. Cloudflare
11. Webhooks
12. OAuth
13. API Keys / Developer API

## Regra arquitetural
Frontend → API FLOW → Service → Adapter → API externa.

Nenhuma API key ou client secret de servidor deve ser enviada ao frontend.

## Estados padrão de integração
`disconnected`, `authorizing`, `connected`, `syncing`, `expired`, `error`, `revoked`.

## Regras obrigatórias
- timeout;
- retry seguro;
- idempotência;
- logs sem secrets;
- validação de webhooks;
- OAuth com `state`;
- menor privilégio;
- tratamento de rate limit;
- versionamento de contrato.
