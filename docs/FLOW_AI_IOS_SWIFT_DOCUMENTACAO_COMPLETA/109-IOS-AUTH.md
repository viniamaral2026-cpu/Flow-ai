# iOS Authentication
## Fluxo
Login → sessão → armazenamento seguro → API → renovação → logout.

## Keychain
Credenciais e tokens sensíveis devem usar Keychain ou mecanismo seguro equivalente.

## Sessão
Tratar expiração, renovação, logout e troca de conta.

## Regra
Nunca embutir secrets de backend no aplicativo.
