# FLOW AI --- FLOW_AI_BACKEND_PYTHON.md

## 1. Objetivo

Definir padrões Python, serviços, agentes, integrações, segurança,
execução assíncrona e infraestrutura do FLOW AI.

## 2. Versão e qualidade

Adotar uma versão Python atualmente suportada pelo ambiente de produção
e fixá-la no projeto.

Padrões:

-   type hints;
-   dataclasses quando apropriado;
-   funções pequenas;
-   classes com responsabilidade única;
-   tratamento explícito de exceções;
-   logging estruturado;
-   testes automatizados;
-   lint/format;
-   dependências fixadas.

## 3. Organização

``` text
backend/
├── apps/
├── core/
├── services/
├── integrations/
├── agents/
├── workers/
├── tests/
└── scripts/
```

## 4. Services

Services concentram regras de negócio que atravessam modelos ou
integrações.

Exemplos:

``` text
ChatService
MemoryService
RoutineService
TimerService
AIService
VoiceService
VisionService
IntegrationService
NotificationService
BillingService
```

## 5. Adapters

Integrações externas nunca devem contaminar o domínio.

``` text
integrations/
├── nvidia/
├── firebase/
├── cloudflare/
├── meta/
├── google/
├── microsoft/
└── payments/
```

Cada integração deve possuir:

-   client;
-   configuração;
-   autenticação;
-   adapter;
-   tratamento de erros;
-   timeout;
-   retry quando seguro;
-   logs sem secrets.

## 6. Agente FLOW

Arquitetura conceitual:

``` text
Mensagem
  ↓
Context Builder
  ↓
Memory Resolver
  ↓
Permission Resolver
  ↓
Model Router
  ↓
Agent
  ↓
Tool Planner
  ↓
Confirmation Gate
  ↓
Tool Executor
  ↓
Result
```

A FLOW não deve executar ações sensíveis sem verificar permissões e
confirmação quando necessário.

## 7. Ferramentas

Cada ferramenta deve possuir contrato:

``` text
name
description
input_schema
permission
risk_level
handler
timeout
```

Categorias:

-   chat;
-   memória;
-   arquivos;
-   calendário;
-   e-mail;
-   mensagens;
-   dispositivos;
-   casa inteligente;
-   rotinas;
-   timers;
-   visão;
-   busca;
-   notificações.

## 8. NVIDIA

Criar um provider isolado.

``` python
class AIProvider:
    def generate(self, request):
        raise NotImplementedError
```

Implementação NVIDIA fica separada do restante da aplicação.

Configuração:

``` env
NVIDIA_API_KEY=
NVIDIA_MODEL=
NVIDIA_BASE_URL=
```

A chave deve existir somente no backend.

## 9. Meta / Facebook

Criar:

``` text
MetaOAuthService
MetaTokenService
MetaGraphClient
MetaWebhookService
```

Fluxo:

``` text
usuário autoriza
↓
callback
↓
validar state
↓
trocar código/token
↓
armazenar credencial protegida
↓
associar integração ao usuário
```

Webhooks devem validar autenticidade antes de processar eventos.

## 10. Firebase

Criar adapter próprio.

Possibilidades:

-   autenticação;
-   push notifications;
-   serviços Firebase já utilizados pelo produto.

Nunca expor credenciais administrativas.

## 11. Cloudflare

Usar adapters/clients quando o backend precisar interagir com:

-   DNS;
-   Workers;
-   R2;
-   APIs administrativas;
-   serviços de proteção.

Segredos:

``` env
CLOUDFLARE_API_TOKEN=
CLOUDFLARE_ACCOUNT_ID=
```

## 12. HTTP

Todo cliente externo deve ter:

-   timeout;
-   retry controlado;
-   tratamento de status;
-   circuit breaker quando necessário;
-   logs;
-   correlation ID.

Não usar requests externos sem timeout.

## 13. Assíncrono

Usar tarefas assíncronas para:

-   processamento pesado;
-   IA longa;
-   arquivos;
-   sincronizações;
-   notificações;
-   webhooks;
-   rotinas.

Evitar bloquear requests HTTP.

## 14. Idempotência

Operações que podem ser repetidas devem suportar idempotência:

-   pagamentos;
-   webhooks;
-   execução de rotina;
-   criação de recursos externos;
-   notificações.

## 15. Segurança de secrets

Nunca:

``` python
API_KEY = "chave-real"
```

Sempre:

``` python
import os
API_KEY = os.environ["NVIDIA_API_KEY"]
```

Em produção, preferir secret manager.

## 16. Logs

Logs devem ser estruturados.

Nunca registrar:

-   API keys;
-   access tokens;
-   refresh tokens;
-   passwords;
-   secrets;
-   dados sensíveis desnecessários.

## 17. Tratamento de erros

Definir exceções de domínio:

``` text
ValidationError
PermissionDenied
IntegrationError
ProviderError
RateLimitError
ResourceNotFound
ExternalServiceUnavailable
```

A API converte essas exceções para respostas HTTP consistentes.

## 18. Retries

Retry somente quando a operação for segura.

Usar backoff exponencial e limite de tentativas.

Não repetir automaticamente operações potencialmente duplicadoras sem
idempotency key.

## 19. Configuração

Separar:

``` text
development
test
staging
production
```

Nenhum ambiente deve depender de valores secretos versionados.

## 20. Testes Python

Estrutura:

``` text
tests/
├── unit/
├── integration/
├── api/
├── agents/
├── integrations/
└── security/
```

Testar também falhas de provedores externos.

## 21. Jobs

Exemplos:

``` text
process_file
sync_integration
execute_routine
send_notification
process_ai_task
cleanup_expired_sessions
rotate_expired_tokens
```

## 22. Contratos internos

Services e adapters devem receber objetos/DTOs bem definidos, evitando
dicionários arbitrários espalhados pelo código.

## 23. Regra para agentes de IA que alterarem o backend

Antes de editar:

1.  localizar arquivo;
2.  entender dependências;
3.  procurar implementação equivalente;
4.  verificar testes;
5.  alterar o mínimo necessário;
6.  executar testes;
7.  validar migration;
8.  verificar logs;
9.  atualizar documentação.

Nunca criar uma segunda implementação de uma funcionalidade existente
sem justificativa documentada.
