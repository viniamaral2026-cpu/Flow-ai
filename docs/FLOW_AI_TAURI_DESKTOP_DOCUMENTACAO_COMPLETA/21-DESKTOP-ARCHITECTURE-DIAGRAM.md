# Diagrama de Arquitetura

```text
                    FLOW AI ECOSYSTEM
                           │
             ┌─────────────┴─────────────┐
             │                           │
          Web/PWA                   Desktop Tauri
             │                           │
          React                    React + Tauri
                                         │
                              ┌──────────┼──────────┐
                              │          │          │
                            Linux      Windows     macOS
                              │          │          │
                              └──────────┼──────────┘
                                         │
                                  HTTPS / WebSocket
                                         │
                                         ▼
                           api-flow-ai.flowsocial.fun
                                         │
                                  Django + Python
                                         │
                   ┌─────────────────────┼─────────────────────┐
                   │                     │                     │
               PostgreSQL              Redis             Serviços IA
```

## Princípio
Desktop é cliente. Backend é autoridade. Dados críticos não dependem do estado local.
