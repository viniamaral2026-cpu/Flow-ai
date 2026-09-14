# FLOW AI — SYSTEM ARCHITECTURE

## 1. Visão

```text
Browser / PWA / Wear OS
        |
        v
Cloudflare DNS + TLS + Edge
        |
        +--------------------+
        |                    |
        v                    v
Frontend              api-flow-ai.flowsocial.fun
                           |
                           v
                    Django / DRF
                           |
        +------------------+------------------+
        |                  |                  |
        v                  v                  v
 PostgreSQL             Redis             Workers
        |                                     |
        +------------------+------------------+
                           |
                    Service / Adapter Layer
                           |
       +---------+---------+---------+---------+
       |         |         |         |         |
     NVIDIA   Firebase   Meta      Google   Payments
```

## 2. Boundaries
- Presentation: HTTP/WebSocket.
- Application: services/use cases.
- Domain: regras e entidades.
- Infrastructure: ORM, Redis, providers, storage e APIs externas.

## 3. Resiliência
Provedores externos devem ter timeout, retry seguro, circuit breaking quando necessário e fallback documentado.

## 4. Escalabilidade
Django deve ser stateless sempre que possível. Sessões e jobs compartilhados devem utilizar serviços externos apropriados.

## 5. Realtime
ASGI/WebSockets podem transmitir estado da FLOW, streaming de IA, timers e notificações.

## 6. Ambientes
`development`, `staging`, `production`.

## 7. Decisões
O backend não deve depender diretamente de uma única IA, storage ou provedor de integração.
