# FLOW AI — DATABASE

## Banco
PostgreSQL.

## Entidades
- User
- Profile
- Session
- Conversation
- Message
- Attachment
- Memory
- Routine
- RoutineTrigger
- RoutineCondition
- RoutineAction
- RoutineExecution
- Timer
- Device
- Room
- Scene
- Integration
- OAuthCredential
- Skill
- SkillInstallation
- File
- Folder
- HealthRecord
- HealthGoal
- Notification
- Subscription
- Payment
- Invoice
- ApiKey
- Webhook
- WebhookEvent
- AuditEvent
- SupportTicket

## Regras
- UUID como identificador público recomendado;
- foreign keys;
- índices para consultas frequentes;
- timestamps;
- soft delete somente quando houver requisito de recuperação/auditoria;
- constraints no banco para invariantes importantes.

## Dados sensíveis
Credenciais e tokens devem ser criptografados/protegidos. Não armazenar secrets em texto puro.

## Migrations
Migrations são parte do código e devem passar por CI.

## Backup
Definir RPO/RTO conforme ambiente e criticidade antes de produção.

## Retenção
Dados devem possuir política explícita por categoria.
