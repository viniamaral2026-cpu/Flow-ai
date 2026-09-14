# FLOW AI Desktop — Master Specification

## 1. Objetivo
Definir a arquitetura oficial do aplicativo desktop FLOW AI para Linux, Windows e macOS. O desktop é um cliente multiplataforma, não o backend de produção.

## 2. Stack oficial
- Shell desktop: Tauri 2
- Interface: React + TypeScript
- Build frontend: Vite
- Comunicação: HTTPS/REST + WebSocket
- Backend central: Django + Python
- Banco central: PostgreSQL
- Cache/filas: Redis
- IA: camada de provedores/serviços do FLOW AI
- Domínio da API: `api-flow-ai.flowsocial.fun`
- Domínio web: `flow-ai.flowsocial.fun`

## 3. Princípio arquitetural
O React concentra UI e estado de apresentação. O Tauri fornece integração nativa controlada. O backend concentra autenticação, dados, regras de negócio, IA, integrações e sincronização.

## 4. Plataformas
- Linux: plataforma prioritária de desenvolvimento e distribuição.
- Windows: Windows 10/11, com suporte conforme matriz de builds.
- macOS: versões suportadas definidas por cada release.
- O código deve evitar dependências exclusivas de um único sistema sempre que possível.

## 5. Funcionalidades desktop
Chat, voz, Wake Word quando tecnicamente disponível, notificações, tray, atalhos, memória, arquivos, rotinas, timers, integrações, Skills, configurações, sincronização e diagnóstico.

## 6. Segurança
Segredos nunca ficam no código. Tokens devem usar armazenamento seguro do sistema ou mecanismo equivalente. O frontend não recebe credenciais administrativas. IPC/Tauri deve expor somente comandos necessários.

## 7. Regra de desenvolvimento
Antes de criar qualquer módulo, o agente deve pesquisar o repositório, rotas, componentes, comandos Tauri, APIs e documentação existente. Não duplicar funcionalidades.

## 8. Fluxo de execução
LER → INSPECIONAR → LOCALIZAR → PLANEJAR → EXECUTAR → TESTAR → AUDITAR → DOCUMENTAR.

## 9. Critério de pronto
Uma funcionalidade desktop só é considerada concluída após build, testes, tratamento de erro, validação de permissões, comportamento de rede e documentação.
