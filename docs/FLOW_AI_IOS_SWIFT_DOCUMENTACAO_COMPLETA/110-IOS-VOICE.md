# iOS Voice Engine
## Pipeline
Microfone → captura → processamento/detecção → serviço de voz → IA → resposta.

## APIs
A implementação deve usar APIs Apple apropriadas para captura/reprodução e respeitar permissões.

## Estados
idle, listening, processing, speaking, error, disabled.

## Privacidade
Indicar claramente quando o microfone estiver ativo e não manter áudio além da retenção definida pelo produto.
