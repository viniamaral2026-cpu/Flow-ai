# FLOW AI — PRODUCT REQUIREMENTS

## 1. Visão
FLOW AI é um assistente pessoal de IA projetado para conversar, compreender contexto e executar ações autorizadas. O produto combina chat, voz, visão, memória, ferramentas, automações, integrações e dispositivos.

## 2. Capacidades
- conversa textual;
- voz;
- visão;
- memória;
- ferramentas;
- rotinas;
- timers;
- casa inteligente;
- arquivos;
- saúde e bem-estar;
- receitas;
- integrações;
- Skills;
- API para desenvolvedores;
- assinatura e pagamentos;
- notificações.

## 3. Requisitos funcionais
Cada capacidade deve possuir:
- entrada;
- validação;
- autorização;
- processamento;
- resultado;
- tratamento de erro;
- auditoria quando relevante.

## 4. Requisitos não funcionais
- HTTPS;
- autenticação;
- autorização por recurso;
- disponibilidade monitorada;
- observabilidade;
- escalabilidade horizontal do backend;
- testes automatizados;
- recuperação de falhas;
- proteção de secrets;
- versionamento de API.

## 5. Critérios de aceite
Uma funcionalidade só é considerada pronta quando:
- fluxo principal funciona;
- estados de loading/erro/vazio são tratados;
- permissões estão implementadas;
- API possui contrato;
- testes críticos existem;
- logs não vazam secrets;
- documentação está atualizada.

## 6. Roadmap técnico
### Fundação
Django, banco, autenticação, API, observabilidade e CI.

### Plataforma
Chat, IA, memória, arquivos, voz e ferramentas.

### Automação
Rotinas, timers, dispositivos e casa inteligente.

### Ecossistema
Skills, integrações, API pública e developer platform.

### Monetização
Planos, assinatura, pagamentos, limites e billing.
