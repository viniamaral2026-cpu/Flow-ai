# FLOW AI — NVIDIA AI API

## Objetivo
Conectar o ModelRouter do FLOW a modelos disponibilizados por infraestrutura/API NVIDIA adotada pelo projeto.

## Variáveis
```env
NVIDIA_API_KEY=
NVIDIA_BASE_URL=
NVIDIA_MODEL=
```

## Fluxo
```text
Agent
 → AIService
 → ModelRouter
 → NvidiaProvider
 → NVIDIA endpoint
```

## Interface
```python
class AIProvider:
    async def generate(self, request): ...
    async def stream(self, request): ...
```

## Request interno
```json
{
  "model": "configured-model",
  "messages": [],
  "temperature": 0.7,
  "max_tokens": 2048
}
```

## Segurança
A API key é segredo de servidor.

## Resiliência
- timeout;
- retry em erros transitórios;
- backoff;
- circuit breaker;
- fallback documentado.

## Observabilidade
Registrar:
- provider;
- modelo;
- latência;
- status;
- tokens/uso quando disponibilizado.

Nunca registrar API key.

## Observação
O endpoint, modelo, parâmetros e autenticação concretos dependem do produto NVIDIA escolhido e devem ser confirmados na documentação oficial vigente.
