# Android + Wear OS
## Objetivo
Integrar o FLOW AI ao relógio sem duplicar a lógica central.

## Arquitetura
Wear OS possui UI e recursos próprios, enquanto a conta e regras principais permanecem no backend.

## Funções
Comandos rápidos, timers, notificações, status e interação de voz conforme capacidades do dispositivo.

## Sincronização
Comunicação segura entre telefone/serviço e backend. Não presumir que o telefone estará sempre conectado.

## Bateria
Limitar processamento e sincronização contínua.
