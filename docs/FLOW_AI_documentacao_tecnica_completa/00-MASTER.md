# FLOW AI — MASTER DOCUMENTATION
## Documento mestre técnico

### Objetivo
Esta documentação é a fonte de organização técnica do FLOW AI. Ela conecta produto, frontend, backend Django/Python, API, infraestrutura, IA, integrações, segurança, dados, pagamentos, observabilidade e operação.

### Fonte de verdade
A documentação deve ser usada junto ao código-fonte e aos contratos reais do ambiente. Onde um valor de infraestrutura ainda não foi validado, ele é tratado como configuração planejada, não como fato operacional.

### Domínios planejados
- Frontend: `https://flow-ai.flowsocial.fun`
- API: `https://api-flow-ai.flowsocial.fun`

### Stack-alvo
- Frontend web/PWA
- Django + Django REST Framework
- Python
- PostgreSQL
- Redis
- workers assíncronos
- Cloudflare
- Firebase
- NVIDIA AI
- Meta/Facebook APIs
- OAuth
- Webhooks

### Princípios
1. API-first.
2. Separação de domínio, transporte e infraestrutura.
3. Secrets exclusivamente no servidor/secret manager.
4. Idempotência para operações críticas.
5. Observabilidade desde o início.
6. Nenhuma funcionalidade duplicada.
7. Compatibilidade documentada entre frontend e backend.
8. Mudanças incompatíveis exigem versionamento.

### Ordem de implementação
Produto → arquitetura → dados → segurança → backend → API → integrações → frontend → testes → deploy → observabilidade.

### Documentos relacionados
Consulte os demais arquivos desta pasta por domínio.
