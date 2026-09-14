# FLOW AI — SECURITY

## Modelo
Defesa em profundidade.

## Autenticação
- sessões/tokens;
- expiração;
- revogação;
- 2FA;
- recuperação de conta.

## Autorização
RBAC/permissions + ownership por objeto.

## Secrets
NVIDIA, Firebase, Meta, Cloudflare, pagamentos e OAuth nunca ficam no frontend ou Git.

## Web
- HTTPS;
- HSTS;
- CSP quando compatível;
- CORS restritivo;
- CSRF;
- Secure/HttpOnly cookies;
- proteção contra brute force.

## API
- rate limit;
- validação;
- payload limits;
- autorização;
- audit logging.

## Webhooks
Validar assinatura/autenticidade, timestamp quando aplicável e idempotência.

## API keys
Hash/criptografia conforme modelo; mostrar segredo completo apenas quando necessário na criação; permitir revogação e rotação.

## Incidentes
Registrar, conter, revogar credenciais afetadas, preservar evidências e atualizar documentação.
