# FLOW AI — INFRAESTRUTURA DETALHADA

## 1. Objetivo
Definir a infraestrutura necessária para executar o FLOW AI de forma reproduzível, segura e observável.

## 2. Arquitetura
```text
Internet
  ↓
Cloudflare DNS / TLS / Edge
  ↓
Frontend: flow-ai.flowsocial.fun
  ↓
API: api-flow-ai.flowsocial.fun
  ↓
Django/ASGI
  ├── PostgreSQL
  ├── Redis
  └── Workers
        ├── IA
        ├── Webhooks
        ├── Notifications
        ├── Sync
        └── Files
```

## 3. Componentes
### Frontend
Entrega do aplicativo web/PWA.

### Backend
Django + Django REST Framework, com ASGI quando houver WebSockets.

### PostgreSQL
Persistência transacional.

### Redis
Cache, locks e broker/fila quando adotado.

### Workers
Executam tarefas que não devem bloquear requests HTTP.

### Storage
Armazenamento de arquivos e objetos. Pode utilizar serviço compatível com S3/R2 conforme decisão de infraestrutura.

## 4. Ambientes
- development;
- staging;
- production.

Cada ambiente deve possuir configuração, banco, credenciais e recursos isolados.

## 5. Docker
Quando adotado:
- imagens versionadas;
- usuário não-root;
- healthcheck;
- dependências fixadas;
- configuração externa;
- nenhum secret dentro da imagem.

## 6. Rede
Somente portas estritamente necessárias devem ser expostas. PostgreSQL e Redis não devem ficar públicos.

## 7. TLS
Todo tráfego externo deve utilizar HTTPS.

## 8. Backup
Definir:
- frequência;
- retenção;
- RPO;
- RTO;
- criptografia;
- restauração testada.

## 9. Escala
API stateless permite múltiplas instâncias. Workers podem escalar separadamente conforme fila.

## 10. Disaster Recovery
Documentar reconstrução da infraestrutura, restauração do banco, secrets, storage e DNS.

## 11. Health
- `/health`: processo disponível;
- `/ready`: dependências críticas prontas.

Não retornar credenciais ou detalhes internos.
