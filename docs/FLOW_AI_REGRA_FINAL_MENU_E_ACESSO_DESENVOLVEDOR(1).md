# FLOW AI — REGRA FINAL DE MENU, CATEGORIAS E ACESSO DE DESENVOLVEDOR

**Versão:** 1.0  
**Status:** Regra obrigatória para UX, frontend, backend e agentes de IA

## 1. OBJETIVO

Esta especificação define como o menu lateral do FLOW AI deve funcionar e como o acesso às funcionalidades de desenvolvedor/API deve ser controlado.

O objetivo é manter a interface organizada mesmo quando o produto crescer muito.

Regra central:

> **O menu lateral não pode crescer indefinidamente. As funcionalidades devem ser organizadas por categorias, com categorias recolhíveis e submenus quando necessário.**

Além disso:

> **Funcionalidades de desenvolvedor/API não devem ficar expostas como parte do menu padrão do consumidor final. O usuário interessado deve solicitar acesso.**

---

## 2. MENU LATERAL — REGRA OBRIGATÓRIA

O menu lateral deve ser estruturado em:

```text
CATEGORIA
   ├── Item
   ├── Item
   └── Item
```

Quando uma categoria possuir muitos recursos:

```text
CATEGORIA
   ├── Subcategoria
   │     ├── Item
   │     ├── Item
   │     └── Item
   └── Subcategoria
         ├── Item
         └── Item
```

A categoria deve possuir controle de:

- expandir;
- recolher;
- indicar estado ativo;
- indicar existência de submenu;
- preservar contexto de navegação.

---

## 3. NÃO CRIAR MENU EXTENSO

É proibido transformar cada funcionalidade em um item de primeiro nível.

Evitar:

```text
Chat
Nova conversa
Conversas
Memória
Arquivos
Rotinas
Timers
Casa
Dispositivos
Integrações
Gmail
Calendar
Drive
WhatsApp
Instagram
Saúde
Receitas
Voz
Skills
API
...
```

Esse modelo não deve ser utilizado.

A arquitetura correta é agrupar.

---

## 4. EXEMPLO DE ESTRUTURA

Uma estrutura conceitual poderá ser:

```text
FLOW
├── Início
├── Conversas
│   ├── Chat
│   ├── Histórico
│   └── Pesquisar
├── Organização
│   ├── Memória
│   ├── Arquivos
│   ├── Rotinas
│   └── Timers
├── Casa
│   ├── Visão geral
│   ├── Cômodos
│   ├── Dispositivos
│   └── Automações
├── Conexões
│   ├── Integrações
│   ├── Gmail
│   ├── Calendar
│   ├── Drive
│   ├── WhatsApp
│   └── Instagram
├── Bem-estar
│   ├── Saúde
│   └── Receitas
├── Flow AI
│   ├── Voz
│   ├── Personalidade
│   ├── Comportamento
│   ├── Autonomia
│   └── Skills
└── Conta
    ├── Perfil
    ├── Segurança
    ├── Privacidade
    ├── Assinatura
    └── Configurações
```

Essa é uma referência de organização, não uma obrigação de usar exatamente esses nomes. O princípio de categorização é obrigatório.

---

## 5. CATEGORIAS RECOLHÍVEIS

Cada categoria deve poder ser expandida ou recolhida.

Exemplo:

```text
▼ Conversas
   Chat
   Histórico
   Pesquisar

▶ Organização

▼ Casa
   Visão geral
   Cômodos
   Dispositivos
```

Quando recolhida:

```text
▶ Conversas
▶ Organização
▶ Casa
```

Isso reduz a altura ocupada pelo menu.

---

## 6. SUBMENUS

Submenus devem ser utilizados quando uma categoria tiver muitos recursos relacionados.

Exemplo:

```text
▼ Conexões
   ▼ Google
      Gmail
      Calendar
      Drive
   ▼ Meta
      WhatsApp
      Instagram
   Outras integrações
```

Não criar uma lista vertical interminável.

---

## 7. SEM BARRA DE ROLAGEM NO MENU PRINCIPAL

Regra visual obrigatória:

> **O menu lateral não deve apresentar uma barra de rolagem visível como solução para excesso de itens.**

Se o menu estiver ficando grande demais, o agente deve primeiro:

1. agrupar;
2. criar categorias;
3. recolher categorias;
4. criar submenus;
5. mover configurações secundárias para níveis apropriados;
6. reorganizar a hierarquia.

Não simplesmente adicionar mais itens e uma scrollbar.

---

## 8. MENU ADAPTATIVO

A estrutura deve funcionar em:

- desktop;
- notebook;
- tablet;
- mobile;
- PWA;
- desktop Tauri.

No mobile, o menu poderá utilizar drawer/hamburger, mas a mesma hierarquia de categorias deve ser preservada.

---

## 9. ESTADO DO MENU

O sistema deve controlar pelo menos:

```text
categoria expandida
categoria recolhida
submenu expandido
submenu recolhido
item ativo
rota atual
permissão do usuário
```

A interface deve evitar perda de contexto durante a navegação.

Quando apropriado, o sistema pode memorizar as categorias abertas para aquele usuário/dispositivo.

---

# PARTE II — DESENVOLVEDOR E APIs

## 10. REGRA DE ACESSO

As funcionalidades de desenvolvedor/API são destinadas a usuários que possuem conhecimento técnico ou necessidade específica de integração.

Portanto:

> **API, chaves, webhooks, SDKs, endpoints, logs técnicos e ferramentas avançadas de desenvolvedor não devem aparecer no menu padrão do consumidor final.**

O consumidor comum não precisa dessa complexidade.

---

## 11. DESENVOLVEDOR COMO ÁREA CONTROLADA

O acesso deve funcionar assim:

```text
Usuário
   ↓
FLOW AI
   ↓
Solicitar acesso de desenvolvedor
   ↓
Formulário
   ↓
Solicitação enviada
   ↓
Painel administrativo
   ↓
Análise
   ↓
Aprovação ou recusa
   ↓
Se aprovado → liberar área Desenvolvedor
```

A aprovação não deve ser presumida.

---

## 12. NOVA PÁGINA — SOLICITAR ACESSO

Deve existir uma página específica:

**Solicitar acesso de desenvolvedor**

Ela deve explicar claramente que:

- a área é destinada a desenvolvedores e integrações;
- o acesso é sujeito à análise;
- nem todo usuário precisa dessa área;
- a solicitação será enviada para análise;
- após aprovação, os recursos serão liberados.

---

## 13. FORMULÁRIO DE SOLICITAÇÃO

O formulário pode conter, conforme definição posterior do produto:

- nome;
- e-mail da conta;
- empresa/projeto, se aplicável;
- finalidade do uso;
- tipo de integração pretendida;
- descrição do projeto;
- recursos desejados;
- informações técnicas necessárias;
- aceite dos termos específicos de desenvolvedor.

Não solicitar dados desnecessários.

O backend deve validar todos os campos.

---

## 14. STATUS DA SOLICITAÇÃO

A solicitação deve possuir estado controlado.

Exemplo:

```text
PENDENTE
   ↓
EM ANÁLISE
   ↓
APROVADA
```

ou:

```text
PENDENTE
   ↓
EM ANÁLISE
   ↓
RECUSADA
```

Também pode existir:

```text
REVOGADA
CANCELADA
```

se esses estados forem necessários.

---

## 15. TELA DE STATUS

Depois de solicitar, o usuário deve conseguir consultar o estado.

Exemplo:

```text
Desenvolvedor

Solicitação enviada

Status: Em análise

Sua solicitação foi recebida.
Quando houver uma decisão, você será informado.
```

Não exibir as ferramentas de desenvolvedor antes da autorização.

---

## 16. APÓS APROVAÇÃO

Somente depois da aprovação o menu deve liberar a categoria:

```text
Desenvolvedor
├── Visão geral
├── API
├── Chaves
├── Endpoints
├── Webhooks
├── SDKs
├── Exemplos
├── Logs
└── Limites de uso
```

Essa categoria também deve ser recolhível.

---

## 17. CONTROLE POR PERMISSÃO

O frontend não deve ser a única camada de segurança.

A autorização deve existir no backend.

Exemplo conceitual:

```text
user
  ↓
developer_access
  ↓
permissions/scopes
  ↓
developer endpoints
```

O backend deve verificar a permissão antes de entregar recursos protegidos.

Esconder o menu não é segurança.

---

## 18. REVOGAÇÃO

Se o acesso for revogado:

```text
Acesso aprovado
      ↓
Revogação
      ↓
Área Desenvolvedor removida
      ↓
Tokens/chaves afetados conforme política
```

O sistema deve invalidar ou restringir credenciais quando necessário.

---

## 19. CONSUMIDOR FINAL

O consumidor final deve ter uma experiência simples.

Ele não precisa visualizar:

- API;
- endpoints;
- SDK;
- webhooks;
- chaves;
- logs técnicos;
- documentação técnica;
- limites técnicos;
- configurações avançadas de integração.

Mas deve poder encontrar uma opção clara para:

> **Solicitar acesso de desenvolvedor**

quando tiver interesse.

---

## 20. REGRA DE UX

O produto deve seguir:

```text
USUÁRIO COMUM
→ interface simples
→ categorias essenciais
→ pouca complexidade visual

DESENVOLVEDOR AUTORIZADO
→ área avançada
→ ferramentas técnicas
→ APIs
→ chaves
→ webhooks
→ SDKs
```

A complexidade deve aparecer somente para quem precisa dela.

---

## 21. REGRA PARA AGENTES DE IA

Antes de adicionar qualquer item ao menu, o agente deve perguntar:

1. É realmente uma área principal?
2. Pode pertencer a uma categoria existente?
3. Precisa de submenu?
4. É uma configuração secundária?
5. É uma função exclusiva de desenvolvedor?
6. O usuário comum precisa enxergar isso?
7. Existe uma permissão necessária?
8. A inclusão aumenta excessivamente a altura do menu?
9. Estou resolvendo o crescimento com hierarquia ou simplesmente adicionando itens?

Se o menu crescer, reorganizar primeiro.

---

## 22. REGRA ABSOLUTA DO MENU

> **NUNCA RESOLVA O CRESCIMENTO DO MENU COM UMA LISTA VERTICAL INFINITA. USE CATEGORIAS RECOLHÍVEIS E SUBMENUS. O MENU DEVE PERMANECER ORGANIZADO, COMPACTO E SEM UMA BARRA DE ROLAGEM VISÍVEL COMO SOLUÇÃO PARA EXCESSO DE ITENS.**

---

## 23. REGRA ABSOLUTA DO DESENVOLVEDOR

> **A ÁREA DE DESENVOLVEDOR NÃO É UMA FUNÇÃO PADRÃO DO CONSUMIDOR. O USUÁRIO PODE SOLICITAR ACESSO, A SOLICITAÇÃO DEVE SER ENVIADA AO PAINEL ADMINISTRATIVO PARA ANÁLISE E, SOMENTE APÓS APROVAÇÃO, AS PÁGINAS E RECURSOS DE DESENVOLVEDOR DEVEM SER LIBERADOS. A AUTORIZAÇÃO DEVE SER VALIDADA NO BACKEND.**

---

## 24. NOVAS EXPERIÊNCIAS NECESSÁRIAS

Com esta regra, o projeto deve prever pelo menos:

### Para qualquer usuário
- Solicitar acesso de desenvolvedor;
- formulário de solicitação;
- confirmação de envio;
- status da solicitação.

### Para usuário aprovado
- categoria Desenvolvedor;
- visão geral;
- API;
- chaves;
- endpoints;
- webhooks;
- SDKs;
- exemplos;
- logs;
- limites;
- documentação técnica.

### Para administração
O painel administrativo posteriormente deverá receber:

- fila de solicitações;
- detalhes da solicitação;
- status;
- aprovação;
- recusa;
- revogação;
- histórico;
- auditoria.

O painel administrativo será especificado em documentação própria quando for implementado.

---

## 25. INTEGRAÇÃO COM A REGRA APP × SITE

Esta especificação deve ser combinada com a regra de separação entre aplicativo e site.

A página **Solicitar acesso de desenvolvedor** é uma funcionalidade do produto, não uma página institucional do site.

O site pode explicar que existe uma plataforma/API para desenvolvedores e direcionar o usuário ao produto para solicitar acesso, mas não deve transformar toda a área de desenvolvedor em páginas públicas.

---

## 26. CHECKLIST FINAL

Antes de finalizar o menu:

- [ ] Está organizado por categorias?
- [ ] As categorias podem ser recolhidas?
- [ ] Existem submenus quando necessário?
- [ ] O menu não está verticalmente excessivo?
- [ ] Não foi usada scrollbar como solução para excesso?
- [ ] O item ativo está claro?
- [ ] A hierarquia é consistente?
- [ ] O comportamento funciona em desktop?
- [ ] O comportamento funciona em mobile?
- [ ] Permissões controlam itens protegidos?
- [ ] Desenvolvedor está oculto para quem não tem acesso?
- [ ] Existe "Solicitar acesso de desenvolvedor"?
- [ ] A solicitação chega ao backend?
- [ ] Existe status da solicitação?
- [ ] A aprovação libera a área?
- [ ] O backend também verifica a permissão?
- [ ] A revogação remove/restringe o acesso?
- [ ] APIs e ferramentas técnicas não estão expostas ao consumidor comum?

---

## 27. INSTRUÇÃO CURTA PARA IA

> **MANTENHA O MENU LATERAL COMPACTO E ORGANIZADO POR CATEGORIAS RECOLHÍVEIS. USE SUBMENUS PARA AGRUPAR FUNCIONALIDADES QUANDO UMA CATEGORIA CRESCER. NÃO CRIE UMA LISTA VERTICAL EXTENSA E NÃO USE BARRA DE ROLAGEM COMO SOLUÇÃO PARA EXCESSO DE ITENS. FUNCIONALIDADES DE DESENVOLVEDOR/API NÃO DEVEM APARECER NO MENU PADRÃO DO CONSUMIDOR. CRIE UMA ÁREA "SOLICITAR ACESSO DE DESENVOLVEDOR", ENVIE A SOLICITAÇÃO AO BACKEND PARA ANÁLISE ADMINISTRATIVA E LIBERE A ÁREA DE DESENVOLVEDOR SOMENTE APÓS APROVAÇÃO. A PERMISSÃO DEVE SER VALIDADA NO BACKEND; OCULTAR MENU NÃO É SEGURANÇA.**
