# FLOW AI Desktop — Voz

## Objetivo
Permitir interação por voz com baixa fricção sem transformar o cliente desktop em autoridade de segurança.

## Pipeline
```text
Microfone → Captura → Detecção/Wake Word → Áudio → Serviço de voz → IA → Resposta
```

## Wake Word
O processamento pode ser local quando a tecnologia adotada permitir. O aplicativo deve oferecer ativação/desativação e indicador claro de estado.

## Privacidade
Não gravar áudio indefinidamente por padrão. Definir retenção, consentimento, telemetria e processamento no documento de privacidade.

## Falhas
Tratar:
- microfone indisponível;
- permissão negada;
- dispositivo desconectado;
- serviço de voz indisponível;
- rede offline;
- timeout;
- áudio inválido.

## Estados
idle, listening, processing, speaking, error e disabled.

## Regra
A UI deve sempre indicar quando o FLOW está captando/processando voz.
