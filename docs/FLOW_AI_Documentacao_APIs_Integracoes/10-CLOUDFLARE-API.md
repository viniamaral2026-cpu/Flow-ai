# FLOW AI — CLOUDFLARE API

## Uso
Automação/gestão de DNS, edge, segurança e recursos Cloudflare quando necessário.

## Variáveis
```env
CLOUDFLARE_API_TOKEN=
CLOUDFLARE_ACCOUNT_ID=
CLOUDFLARE_ZONE_ID=
```

## Segurança
Preferir API Tokens com menor privilégio em vez de credenciais globais.

## Operações internas
Exemplo de camada:
```text
CloudflareService
 → CloudflareAdapter
 → Cloudflare API
```

## Domínios
- `flow-ai.flowsocial.fun`
- `api-flow-ai.flowsocial.fun`

## Operações
- DNS;
- zones;
- regras de segurança;
- cache;
- Workers/R2 quando adotados.

## Regra
Automação de DNS deve exigir validação forte e não deve ficar exposta como ferramenta comum da FLOW para usuários finais.

## Observação
Permissões e endpoints exatos devem ser conferidos na API atual da Cloudflare.
