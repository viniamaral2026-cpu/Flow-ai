# Android Build e Release
## Ambientes
development, staging e production.

## Artefatos
Gerar APK para testes internos e AAB para publicação na Play Store.

## Pipeline
lint → compile → unit tests → instrumentation/E2E → bundle → assinatura → validação → publicação.

## Versionamento
versionCode crescente e versionName seguindo política de release.

## Segurança
Keystore e credenciais nunca devem entrar no Git.
