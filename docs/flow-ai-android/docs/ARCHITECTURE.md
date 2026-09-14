# Arquitetura — flow-ai-android

## Responsabilidade
Aplicativo Android nativo.

## Tecnologia
Kotlin + Jetpack Compose

## Fronteiras
Este repositório deve possuir somente responsabilidades próprias da sua camada.
Integrações com outros componentes devem usar contratos documentados.

## Contratos
- API: `https://api-flow-ai.flowsocial.fun`
- Web: `https://flow-ai.flowsocial.fun`

## Regras
1. O backend é autoridade para dados e autorização.
2. Clientes não devem conter secrets de backend.
3. Mudanças incompatíveis devem ser versionadas/migradas.
4. Antes de criar uma nova implementação, procurar a existente.
5. Toda integração externa deve possuir adapter/service isolado quando aplicável.

## Diagrama lógico
```text
FLOW AI
   │
   ├── Web/PWA
   ├── Android
   ├── iOS
   ├── Desktop
   │
   └────── HTTPS / WebSocket ──────> Backend
                                      │
                             PostgreSQL / Redis
                                      │
                              IA / Integrações
```
