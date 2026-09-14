# FLOW AI Android — Master Specification
## Objetivo
Definir o aplicativo Android nativo do FLOW AI.

## Stack oficial
- Kotlin
- Jetpack Compose
- Android SDK
- Coroutines + Flow
- Arquitetura recomendada: Clean Architecture + MVVM
- DI: abstração compatível com a arquitetura aprovada
- Rede: cliente HTTPS/REST + WebSocket
- Push: Firebase Cloud Messaging
- Backend: Django + Python
- API: https://api-flow-ai.flowsocial.fun

## Princípios
O Android é cliente. O backend é autoridade para conta, permissões, dados sincronizados, memória, assinatura e regras de negócio.

## Funcionalidades
Chat, voz, Wake Word quando suportado, notificações, memória, arquivos, rotinas, timers, casa inteligente, integrações, Skills, configurações, câmera/visão, sincronização e diagnóstico.

## Regra de desenvolvimento
LER → INSPECIONAR → LOCALIZAR → PLANEJAR → EXECUTAR → TESTAR → AUDITAR → DOCUMENTAR.

Não duplicar telas, APIs, repositories, serviços ou regras existentes.
