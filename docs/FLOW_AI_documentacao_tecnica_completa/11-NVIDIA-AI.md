# FLOW AI — NVIDIA AI

## Objetivo
Isolar o provedor NVIDIA atrás de uma interface de provider para permitir troca de modelo/provedor.

## Configuração
```env
NVIDIA_API_KEY=
NVIDIA_BASE_URL=
NVIDIA_MODEL=
```

## Fluxo
```text
FLOW Agent
→ AIService
→ ModelRouter
→ NvidiaProvider
→ NVIDIA API
```

## Segurança
A API key nunca chega ao navegador.

## Resiliência
- timeout;
- retry apenas em erros transitórios;
- backoff;
- limites;
- fallback quando definido;
- circuit breaker quando necessário.

## Observabilidade
Registrar modelo, latência, status e métricas de uso sem registrar segredo.

## Model routing
O backend valida modelos permitidos e políticas do plano antes da chamada.

## Custos
Limites e orçamento devem ser controlados no backend; quotas reais dependem do contrato/provedor e devem ser verificadas antes da produção.
