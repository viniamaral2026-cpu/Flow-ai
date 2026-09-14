# FLOW AI — REGRA FINAL DE SEPARAÇÃO ENTRE APP E SITE

**Versão:** 1.0  
**Status:** Regra obrigatória para agentes de IA e desenvolvimento

## 1. Regra principal

O **FLOW AI é o produto/aplicativo**. O **site institucional é somente a vitrine pública**.

Não misture as duas coisas.

O site será desenvolvido separadamente, preferencialmente no final do projeto, depois que o produto estiver consolidado.

## 2. O que pertence ao site

O site público pode conter:

- apresentação do FLOW AI;
- proposta de valor;
- recursos;
- planos;
- FAQ;
- contato;
- informações institucionais;
- Termos de Uso;
- Política de Privacidade;
- informações legais;
- chamadas para baixar/abrir o produto;
- conteúdo de marketing.

O site **não deve reproduzir o painel do FLOW AI**.

## 3. O que pertence ao aplicativo/produto

Estas experiências são do produto e não devem ser transformadas em páginas do site:

- login operacional;
- cadastro operacional;
- onboarding;
- dashboard;
- chat e conversas;
- voz e wake word;
- memória;
- arquivos;
- rotinas;
- timers;
- casa inteligente;
- dispositivos;
- integrações;
- Gmail, Calendar, Drive;
- WhatsApp, Instagram e Meta;
- saúde e bem-estar;
- receitas;
- Skills;
- personalidade, comportamento e autonomia da Flow;
- seleção de modelo de IA;
- configurações;
- conta e perfil;
- segurança;
- sessões;
- notificações;
- assinatura e uso;
- pagamentos do produto;
- API/desenvolvedor;
- logs;
- suporte interno;
- estados e funcionalidades autenticadas.

## 4. Web App não é site institucional

Se existir uma experiência web autenticada do produto, ela deve ser tratada como **Web App do FLOW AI**, e não como site institucional.

Regra:

```text
SITE INSTITUCIONAL ≠ WEB APP ≠ APLICATIVOS NATIVOS
```

## 5. Páginas web transitórias permitidas

Algumas operações podem precisar abrir o navegador. Essas páginas são exceções e não fazem parte da experiência normal do site.

### Confirmação de conta/e-mail

Fluxo:

```text
FLOW AI
→ cadastro
→ e-mail
→ link de confirmação
→ navegador
→ página de confirmação
→ conta confirmada
→ retorno ao FLOW AI
```

### Redefinição de senha

Fluxo:

```text
FLOW AI
→ esqueci minha senha
→ e-mail
→ link seguro
→ navegador
→ redefinir senha
→ confirmação
→ retorno ao FLOW AI
```

Essas páginas devem ser simples, funcionais e seguras. Não devem virar um segundo aplicativo.

## 6. O que NÃO criar como página online

Não criar páginas públicas independentes para:

- chat;
- dashboard;
- memória;
- rotinas;
- timers;
- configurações;
- perfil;
- casa inteligente;
- saúde;
- receitas;
- integrações;
- arquivos;
- Skills;
- voz;
- dispositivos;
- API;
- histórico;
- notificações;
- funcionalidades internas do usuário.

Tudo isso pertence ao produto.

## 7. Regra para o inventário antigo

O inventário de telas não deve ser interpretado como inventário do site.

Antes de implementar qualquer item, classifique-o como:

```text
[APP]
[SITE]
[WEB TRANSITÓRIA]
[EXTERNA/TERCEIRO]
[ESTADO/COMPONENTE]
```

Não transforme automaticamente uma tela documentada em uma página do site.

A documentação descreve o projeto; o código real determina o que já existe.

## 8. Regra contra duplicação

É proibido criar:

```text
APP → Dashboard
SITE → Dashboard
```

ou:

```text
APP → Chat
SITE → Chat
```

ou qualquer duplicação semelhante sem requisito explícito.

O site pode ter um botão **Entrar no FLOW AI**, mas isso deve encaminhar o usuário para o produto.

## 9. Autenticação

O login pertence ao produto.

Depois do primeiro login, o aplicativo deve manter uma sessão segura e renovável conforme a arquitetura do backend, evitando exigir usuário e senha a cada abertura.

O site não deve implementar uma segunda autenticação operacional independente.

## 10. Segurança das páginas transitórias

Confirmação de conta e redefinição de senha devem utilizar mecanismos seguros definidos pelo backend, incluindo quando aplicável:

- HTTPS;
- tokens de uso único;
- expiração;
- validação no servidor;
- proteção contra reutilização;
- não exposição de credenciais;
- não registrar tokens sensíveis em logs;
- senhas armazenadas somente de forma segura.

Não inventar mecanismos de autenticação.

## 11. Ordem de desenvolvimento

Prioridade:

```text
1. Backend
2. Produto/Web App
3. Android
4. iOS
5. Desktop
6. IA
7. Voz
8. Integrações
9. Segurança
10. Testes
11. Validação
12. SITE INSTITUCIONAL
```

O site deve ser construído por último para apresentar o produto real, e não funcionalidades hipotéticas.

## 12. Regra para agentes de IA

Antes de criar uma tela, o agente deve verificar:

1. É APP ou SITE?
2. Precisa de usuário autenticado?
3. É funcionalidade operacional do produto?
4. É somente apresentação pública?
5. É uma página transitória de confirmação/recuperação?
6. Já existe rota?
7. Já existe componente?
8. Já existe implementação?
9. Criará duplicação?

Somente depois implementar.

## 13. Regra absoluta

```text
DOCUMENTAÇÃO
    ↓
CLASSIFICAR
    ↓
APP / SITE / WEB TRANSITÓRIA / EXTERNA / ESTADO
    ↓
INSPECIONAR CÓDIGO REAL
    ↓
VERIFICAR DUPLICAÇÃO
    ↓
IMPLEMENTAR NA PLATAFORMA CORRETA
```

Nunca:

```text
DOCUMENTAÇÃO → CRIAR TUDO COMO SITE
```

## 14. Comando curto para o agente

> **NÃO TRATE O INVENTÁRIO OU A DOCUMENTAÇÃO COMO UM MAPA DO SITE. O SITE INSTITUCIONAL É SEPARADO DO PRODUTO FLOW AI E SERÁ DESENVOLVIDO POR ÚLTIMO. LOGIN, CADASTRO, DASHBOARD, CHAT, MEMÓRIA, ROTINAS, TIMERS, VOZ, CASA, INTEGRAÇÕES, ARQUIVOS, SAÚDE, RECEITAS, SKILLS, CONFIGURAÇÕES, CONTA E DEMAIS FUNCIONALIDADES INTERNAS PERTENCEM AO APLICATIVO/PRODUTO. NÃO CRIE ESSAS EXPERIÊNCIAS NO SITE. PÁGINAS WEB SÃO EXCEÇÃO APENAS PARA FLUXOS TRANSITÓRIOS NECESSÁRIOS, COMO CONFIRMAÇÃO DE CONTA/E-MAIL E REDEFINIÇÃO DE SENHA POR LINK DE E-MAIL. ANTES DE IMPLEMENTAR QUALQUER TELA, CLASSIFIQUE-A COMO APP, SITE, WEB TRANSITÓRIA, EXTERNA OU ESTADO/COMPONENTE; INSPECIONE O CÓDIGO REAL E EVITE DUPLICAÇÃO.**
