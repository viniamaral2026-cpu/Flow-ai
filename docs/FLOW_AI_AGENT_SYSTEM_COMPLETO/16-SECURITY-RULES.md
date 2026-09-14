# FLOW AI — REGRAS DE SEGURANÇA PARA AGENTES

## Nunca expor
- API keys;
- passwords;
- OAuth tokens;
- App Secrets;
- private keys;
- session secrets.

## Nunca commitar
`.env`, dumps sensíveis, credenciais ou tokens.

## Backend
Autorização deve ser verificada no servidor.

## Upload
Validar tamanho, tipo, nome e conteúdo conforme política.

## Webhooks
Validar autenticidade.

## Logs
Sanitizar dados sensíveis.

## Dependências
Não adicionar biblioteca sem avaliar necessidade e risco.

## Destruição
Operações destrutivas devem ser explicitamente identificadas.
