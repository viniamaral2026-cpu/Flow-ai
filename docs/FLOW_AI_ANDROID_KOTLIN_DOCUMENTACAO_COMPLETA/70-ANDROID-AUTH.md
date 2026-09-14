# Android Authentication
## Fluxo
Login → obtenção de sessão → armazenamento seguro → acesso à API → renovação → logout.

## Segurança
Nunca salvar senha em texto puro. Tokens devem usar armazenamento protegido do Android por abstração segura.

## Expiração
Detectar sessão inválida, renovar quando permitido e solicitar login quando necessário.

## Logout
Invalidar sessão no servidor quando aplicável e limpar dados locais sensíveis.
