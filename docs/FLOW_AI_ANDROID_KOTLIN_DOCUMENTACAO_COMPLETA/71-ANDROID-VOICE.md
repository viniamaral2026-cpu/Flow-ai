# Android Voice Engine
## Pipeline
Microfone → captura → detecção/processamento → serviço de voz → IA → resposta de áudio.

## Estados
idle, listening, processing, speaking, error, disabled.

## Requisitos
Indicador visual de captura, tratamento de permissão, dispositivo indisponível, timeout, rede offline e erro do provedor.

## Privacidade
Áudio não deve ser armazenado indefinidamente por padrão. Retenção e processamento devem seguir a documentação de privacidade do FLOW AI.
