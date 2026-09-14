# FLOW AI — AGENTE BACKEND

## Stack
Django + Django REST Framework + Python + PostgreSQL + Redis/workers conforme arquitetura.

## Camadas
```text
HTTP
→ Serializer
→ Service
→ Repository/ORM
→ Database
```

## Regras
- regras de negócio em services/domain;
- serializers para validação de transporte;
- migrations versionadas;
- autorização no backend;
- transações quando necessário;
- logs estruturados.

## Não fazer
- regra crítica somente no frontend;
- SQL improvisado sem necessidade;
- endpoint duplicado;
- acesso direto de domínio a provider externo.

## Testes
Alterações devem ter testes adequados.
