# FLOW AI — CLOUDFLARE

## Domínios
- `flow-ai.flowsocial.fun`
- `api-flow-ai.flowsocial.fun`

## Arquitetura
Cloudflare DNS → proxy/TLS → origem correspondente.

## DNS
Criar registros somente para serviços reais. Validar target antes de ativar proxy.

## TLS
Produção deve usar HTTPS ponta a ponta. Configurar modo TLS compatível com certificado válido na origem.

## WAF
Criar regras para:
- abuso;
- endpoints sensíveis;
- padrões maliciosos;
- bots conforme necessidade.

## Rate limiting
Aplicar especialmente a login, API pública, webhooks e endpoints de alto custo.

## Workers
Usar somente quando houver necessidade clara de lógica na edge.

## R2
Pode ser utilizado para objetos/arquivos se adotado. Credenciais ficam no backend.

## DNS/API
Tokens Cloudflare ficam no secret manager.

## Verificação
Antes de produção:
- DNS resolve;
- certificado válido;
- proxy correto;
- CORS correto;
- API responde;
- health check;
- logs.
