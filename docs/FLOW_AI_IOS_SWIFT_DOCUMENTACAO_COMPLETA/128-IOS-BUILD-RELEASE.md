# iOS Build e Release
## Ambientes
development, staging, production.

## Pipeline
lint/build → unit tests → UI tests → archive → assinatura → validação → distribuição.

## Artefato
Archive/IPA conforme processo de distribuição.

## Versionamento
CFBundleShortVersionString e CFBundleVersion devem seguir política documentada.

## Secrets
Certificados e credenciais ficam no CI/secret manager, nunca no Git.
