# Background e App Lifecycle
## Recursos
WorkManager para trabalho agendado/deferrable. Foreground service somente quando houver requisito legítimo e compatível com as políticas Android.

## Eventos
onCreate, foreground/background, process death, restore e encerramento.

## Regra
Não manter processos contínuos sem necessidade. Voz contínua, sincronização e rotinas devem possuir justificativa e política de bateria.

## Recuperação
Restaurar estado seguro após recriação da Activity/processo.
