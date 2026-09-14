# FLOW AI iOS — Master Specification
## Objetivo
Definir o aplicativo iOS nativo do FLOW AI para iPhone e iPad, integrado ao ecossistema FLOW.

## Stack oficial
- Swift
- SwiftUI
- Apple SDKs
- async/await, Actors e Observation/Combine conforme necessidade
- REST/HTTPS + WebSocket
- Push Notifications/APNs
- Backend: Django + Python
- API: https://api-flow-ai.flowsocial.fun

## Arquitetura
O iOS é cliente. O backend é autoridade para identidade, autorização, dados sincronizados, memória, assinatura e regras de negócio.

## Funcionalidades
Chat, voz, Wake Word quando tecnicamente e politicamente suportado, notificações, memória, arquivos, rotinas, timers, casa inteligente, integrações, Skills, câmera/visão, sincronização e diagnóstico.

## Regra de desenvolvimento
LER → INSPECIONAR → LOCALIZAR → PLANEJAR → EXECUTAR → TESTAR → AUDITAR → DOCUMENTAR.

Não duplicar recursos existentes.
