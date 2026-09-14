# FLOW AI --- FLOW_AI_BACKEND_DJANGO.md

## 1. Objetivo

Este documento define a arquitetura de backend do FLOW AI usando
Django + Python, com PostgreSQL como banco principal, APIs REST,
autenticação, tarefas assíncronas, integrações externas e suporte à
camada de IA.

O backend deve ser modular, seguro, observável e preparado para
crescimento.

## 2. Domínios principais

-   accounts --- usuários, perfis, sessões e segurança
-   chat --- conversas, mensagens e anexos
-   ai --- modelos, agentes, contexto e execução
-   memory --- memórias e preferências
-   voice --- comandos de voz, sessões e configurações
-   vision --- análise de imagens
-   routines --- rotinas, gatilhos, condições e ações
-   timers --- timers e recorrências
-   devices --- dispositivos e Wear OS
-   smart_home --- cômodos, cenas e automações
-   integrations --- OAuth, conexões e sincronização
-   skills --- marketplace, instalação, execução e permissões
-   files --- arquivos, pastas e armazenamento
-   health --- dados, metas e integrações de fitness
-   recipes --- receitas e preferências
-   notifications --- push, e-mail e eventos
-   billing --- planos, assinatura, cobrança e pagamentos
-   developer --- API keys, webhooks, sandbox e logs
-   audit --- auditoria e segurança
-   support --- suporte e chamados
-   system --- status, manutenção e configurações globais

## 3. Estrutura sugerida

``` text
backend/
├── manage.py
├── config/
│   ├── settings/
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── accounts/
│   ├── chat/
│   ├── ai/
│   ├── memory/
│   ├── voice/
│   ├── vision/
│   ├── routines/
│   ├── timers/
│   ├── devices/
│   ├── smart_home/
│   ├── integrations/
│   ├── skills/
│   ├── files/
│   ├── health/
│   ├── recipes/
│   ├── notifications/
│   ├── billing/
│   ├── developer/
│   ├── audit/
│   ├── support/
│   └── system/
├── core/
│   ├── permissions/
│   ├── exceptions/
│   ├── middleware/
│   ├── pagination/
│   └── security/
├── services/
├── workers/
├── tests/
├── requirements/
└── .env.example
```

## 4. Camadas

A regra é separar responsabilidades:

``` text
HTTP/API
   ↓
Serializer / validação
   ↓
Service
   ↓
Repository / ORM
   ↓
PostgreSQL
```

Integrações externas devem passar por services/adapters.

Não colocar regra de negócio complexa diretamente em serializers ou
views.

## 5. Django REST Framework

DRF será a camada principal para APIs HTTP.

Padrão:

-   ViewSet/APIView para transporte HTTP
-   Serializer para entrada/saída
-   Service para regra de negócio
-   Model para persistência
-   Permission para autorização
-   Exception handler centralizado

## 6. Autenticação

O backend deve suportar:

-   sessão/autenticação do aplicativo;
-   tokens de API para desenvolvedores;
-   OAuth para integrações;
-   refresh/revogação conforme mecanismo escolhido;
-   2FA;
-   encerramento de sessões;
-   auditoria.

Nunca armazenar senhas ou secrets em texto puro.

## 7. PostgreSQL

PostgreSQL é o banco transacional recomendado.

Entidades centrais:

-   User
-   Profile
-   Conversation
-   Message
-   Memory
-   Routine
-   RoutineExecution
-   Timer
-   Device
-   Integration
-   Skill
-   File
-   Notification
-   Subscription
-   Payment
-   ApiKey
-   Webhook
-   AuditEvent

## 8. IA

A camada `ai` não deve ficar acoplada a um único provedor.

Criar uma abstração:

``` text
AIProvider
├── NvidiaProvider
├── ProviderB
└── LocalProvider
```

O agente recebe:

-   mensagem;
-   contexto;
-   memória autorizada;
-   ferramentas disponíveis;
-   permissões;
-   modelo selecionado.

E retorna:

-   texto;
-   chamadas de ferramentas;
-   ações;
-   solicitações de confirmação;
-   metadados;
-   erros.

## 9. NVIDIA

As chaves NVIDIA devem ficar exclusivamente em variáveis de
ambiente/secret manager.

Exemplo:

``` env
NVIDIA_API_KEY=
NVIDIA_BASE_URL=
NVIDIA_MODEL=
```

Nunca colocar a chave no React, GitHub, documentação pública ou banco
sem proteção.

O backend será o único responsável por chamar a API de IA.

## 10. Firebase

O Firebase pode ser usado como camada complementar, especialmente para:

-   autenticação;
-   notificações;
-   recursos mobile;
-   analytics;
-   serviços específicos já existentes.

Credenciais administrativas devem ficar apenas no backend.

Exemplo:

``` env
FIREBASE_PROJECT_ID=
FIREBASE_CLIENT_EMAIL=
FIREBASE_PRIVATE_KEY=
```

O frontend nunca recebe credenciais administrativas.

## 11. Cloudflare

A Cloudflare deve ficar na borda da infraestrutura:

``` text
Usuário
  ↓
Cloudflare DNS
  ↓
Cloudflare Proxy / TLS
  ↓
API FLOW AI
  ↓
Django
  ↓
PostgreSQL / Redis / serviços
```

Responsabilidades possíveis:

-   DNS;
-   TLS;
-   proxy;
-   proteção de tráfego;
-   regras de firewall;
-   cache quando apropriado;
-   Workers para funções específicas;
-   R2 para objetos, se adotado.

## 12. Domínios

Domínios fornecidos para o projeto:

``` text
flow-ai.flowsocial.fun
api-flow-ai.flowsocial.fun
```

Arquitetura lógica:

``` text
https://flow-ai.flowsocial.fun
        ↓
Frontend FLOW AI

https://api-flow-ai.flowsocial.fun
        ↓
Backend Django / API
```

O domínio real deve ser configurado no DNS da Cloudflare e apontado para
a infraestrutura efetivamente utilizada.

Não colocar IP fixo ou segredo dentro do código.

## 13. Facebook / Meta

Integrações Meta devem usar OAuth e APIs oficiais.

A arquitetura deve separar:

``` text
Meta OAuth
   ↓
Integration Account
   ↓
Encrypted Token Storage
   ↓
Meta Service Adapter
   ↓
FLOW AI
```

Variáveis:

``` env
META_APP_ID=
META_APP_SECRET=
META_REDIRECT_URI=
META_VERIFY_TOKEN=
```

Nunca enviar `META_APP_SECRET` ao frontend.

O mesmo adapter deve permitir evolução para recursos autorizados do
ecossistema Meta, conforme permissões e produtos aprovados.

## 14. Cloudflare + Django

O Django deve confiar somente nos headers/proxy necessários e
corretamente configurados.

Configurar:

-   HTTPS;
-   hosts permitidos;
-   CORS;
-   CSRF;
-   cookies seguros;
-   HSTS;
-   proxy SSL;
-   limites de upload;
-   rate limiting.

## 15. Redis e tarefas

Para operações demoradas:

``` text
Django
  ↓
Celery
  ↓
Redis
  ↓
Worker
```

Usar para:

-   processamento de arquivos;
-   sincronizações;
-   notificações;
-   execução de rotinas;
-   tarefas de IA;
-   webhooks;
-   tarefas agendadas.

## 16. WebSockets

Quando necessário:

``` text
Django ASGI
   ↓
Channels / camada realtime
   ↓
Cliente
```

Casos:

-   resposta de IA em streaming;
-   estado da FLOW;
-   timers;
-   notificações;
-   execução de rotinas.

## 17. Segurança

Obrigatório:

-   secrets fora do código;
-   HTTPS;
-   validação de entrada;
-   autorização por recurso;
-   rate limiting;
-   proteção contra abuso;
-   logs de auditoria;
-   rotação de API keys;
-   tokens com expiração;
-   criptografia de dados sensíveis;
-   backups;
-   políticas de retenção.

## 18. Observabilidade

Registrar:

-   request ID;
-   usuário;
-   endpoint;
-   latência;
-   status HTTP;
-   erro;
-   integração;
-   modelo de IA;
-   consumo;
-   execução de ferramenta.

Não registrar secrets, tokens ou conteúdo sensível sem necessidade.

## 19. Testes

Camadas:

-   unitários;
-   services;
-   API;
-   integração;
-   autenticação;
-   permissões;
-   webhooks;
-   pagamentos;
-   IA;
-   tarefas assíncronas;
-   smoke tests.

## 20. Deploy

Pipeline recomendado:

``` text
Git
 ↓
CI
 ↓
testes
 ↓
build
 ↓
migration
 ↓
deploy
 ↓
health check
```

Nunca aplicar migration destrutiva sem estratégia de rollback.

## 21. Variáveis de ambiente

Arquivo `.env.example` deve documentar nomes, nunca valores secretos.

Categorias:

-   Django;
-   PostgreSQL;
-   Redis;
-   Cloudflare;
-   Firebase;
-   Meta/Facebook;
-   NVIDIA;
-   storage;
-   e-mail;
-   pagamentos;
-   OAuth;
-   observabilidade.

## 22. Princípio de evolução

O backend deve permitir trocar:

-   provedor de IA;
-   storage;
-   serviço de e-mail;
-   provedor de autenticação;
-   infraestrutura;
-   gateway de pagamento;

sem reescrever o domínio inteiro.
