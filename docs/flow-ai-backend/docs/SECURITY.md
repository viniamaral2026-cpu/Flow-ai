# Segurança

## Regras
- Nunca commitar senhas, tokens, API keys, certificados ou chaves privadas.
- Usar secret manager/variáveis protegidas no CI.
- Aplicar menor privilégio.
- Validar autorização no backend.
- Não registrar dados sensíveis em logs.
- Manter dependências atualizadas e revisar vulnerabilidades.
- HTTPS em produção.
- Documentar exceções de segurança.

## Incidentes
Não apagar evidências nem alterar logs para esconder um incidente. Isolar,
preservar informações necessárias e seguir o processo interno de resposta.

## Divulgação
Vulnerabilidades devem ser comunicadas de forma responsável ao mantenedor.
