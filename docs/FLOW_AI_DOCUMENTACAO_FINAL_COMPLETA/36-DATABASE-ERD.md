# FLOW AI — DATABASE ERD E MODELO

## Núcleo
```text
User
 ├── Profile
 ├── Sessions
 ├── Conversations
 │     └── Messages
 ├── Memories
 ├── Routines
 │     └── Executions
 ├── Timers
 ├── Devices
 ├── Integrations
 ├── Files
 ├── Notifications
 ├── Subscriptions
 ├── API Keys
 └── Audit Events
```

## Entidades principais

### User
Identidade principal.

### Conversation
Contêiner de mensagens.

### Message
Mensagem de usuário, FLOW ou sistema.

### Memory
Informação persistente autorizada.

### Routine
Automação configurável.

### RoutineExecution
Histórico de execução.

### Integration
Conexão com provedor externo.

### OAuthCredential
Credencial protegida de integração.

### File
Metadados de arquivo e referência ao storage.

### Subscription
Estado comercial da conta.

### Payment
Transação financeira.

### ApiKey
Credencial de acesso à Developer API.

### WebhookEvent
Evento externo recebido.

### AuditEvent
Registro de ações relevantes.

## Regras
- IDs públicos preferencialmente UUID;
- foreign keys;
- índices;
- unique constraints;
- timestamps;
- migrations;
- isolamento por usuário.

## Dados sensíveis
Tokens e credenciais devem ser protegidos. Conteúdo sensível deve obedecer política de retenção.

## Integridade
Regras críticas devem ser garantidas pelo banco quando possível, além da aplicação.
