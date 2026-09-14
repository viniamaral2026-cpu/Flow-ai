# FLOW AI — REGRA FINAL DE LAYOUT RESPONSIVO, JANELA E ÁREAS FIXAS

**Versão:** 1.0  
**Status:** Regra obrigatória para todas as interfaces do FLOW AI

## 1. Objetivo

Esta especificação define como todas as versões do FLOW AI devem se comportar em diferentes tamanhos de monitor, janela e dispositivo.

O objetivo é impedir que uma interface fique estourada, sobreposta, cortada, desalinhada ou visualmente desorganizada quando o espaço disponível diminuir.

Regra principal:

> **Toda interface do FLOW AI deve ser responsiva, autoajustável e possuir limites mínimos e máximos coerentes. Nenhum layout deve depender de uma resolução única.**

---

## 2. Aplicação da regra

Esta regra vale para:

- Web App;
- Desktop Tauri;
- Android;
- iOS;
- tablet;
- PWA;
- diferentes tamanhos de monitor;
- diferentes densidades e escalas de tela;
- modo janela maximizada;
- janela redimensionada;
- múltiplos monitores, quando aplicável.

A implementação específica pode mudar conforme a plataforma, mas os princípios de layout devem permanecer consistentes.

---

# PARTE I — ESTRUTURA DO PAINEL

## 3. Áreas estruturais

O painel principal deve ser dividido conceitualmente em:

```text
┌─────────────────────────────────────────────────────────┐
│                    CABEÇALHO FIXO                       │
├───────────────┬─────────────────────────────────────────┤
│               │                                         │
│ MENU LATERAL  │             ÁREA DE CONTEÚDO            │
│    FIXO       │          RESPONSIVA / FLEXÍVEL           │
│               │                                         │
│               │                                         │
├───────────────┴─────────────────────────────────────────┤
│              elementos conforme necessidade              │
└─────────────────────────────────────────────────────────┘
```

A estrutura real pode variar conforme a tela, mas a separação entre regiões fixas e flexíveis deve ser preservada.

---

# PARTE II — ELEMENTOS FIXOS

## 4. Menu lateral

O menu lateral é uma área estrutural fixa do painel em desktop.

Ele deve:

- permanecer ancorado ao lado esquerdo;
- manter largura controlada;
- não deformar seu conteúdo;
- possuir categorias recolhíveis;
- possuir submenus quando necessário;
- preservar o estado ativo;
- não crescer indefinidamente com a quantidade de funcionalidades.

A largura do menu deve ser definida pelo Design System e não por conteúdo arbitrário.

Quando a viewport ficar pequena demais para manter o menu lateral aberto confortavelmente, a interface deve utilizar o comportamento responsivo definido para a plataforma, como recolhimento/drawer/hamburger.

Não reduzir indefinidamente a largura do menu até quebrar textos e ícones.

---

## 5. Cabeçalho

O cabeçalho principal é uma área estrutural fixa.

Deve:

- permanecer no topo da aplicação;
- manter altura controlada;
- preservar os controles principais;
- não ser empurrado pelo conteúdo;
- não crescer verticalmente por causa de textos longos;
- possuir comportamento responsivo.

Elementos secundários podem desaparecer, agrupar-se ou ir para menus conforme a largura disponível.

O cabeçalho não deve criar uma segunda linha inesperada apenas para acomodar conteúdo.

---

## 6. Navegação estrutural

Elementos de navegação principais são considerados estruturais.

Exemplos:

- menu lateral;
- cabeçalho;
- botão/menu mobile;
- navegação contextual;
- breadcrumbs quando utilizados;
- controles estruturais de navegação.

Esses elementos devem ter dimensões previsíveis.

---

# PARTE III — ELEMENTOS FLEXÍVEIS

## 7. Área de conteúdo

A área de conteúdo é flexível.

Ela deve:

- ocupar o espaço restante;
- adaptar largura;
- adaptar altura;
- reorganizar componentes;
- utilizar grids responsivos;
- evitar overflow horizontal;
- preservar espaçamentos;
- respeitar largura máxima de leitura quando necessário.

A área de conteúdo nunca deve forçar o menu ou cabeçalho a crescer.

---

## 8. Cards

Cards são elementos flexíveis.

Devem:

- adaptar sua largura;
- reorganizar-se conforme o espaço;
- quebrar em novas linhas quando necessário;
- reduzir quantidade de colunas;
- manter proporções coerentes;
- respeitar largura mínima definida pelo componente.

Exemplo:

```text
Desktop grande:
[ CARD ][ CARD ][ CARD ][ CARD ]

Desktop médio:
[ CARD ][ CARD ][ CARD ]

Janela menor:
[ CARD ][ CARD ]

Janela estreita:
[ CARD ]
[ CARD ]
```

Nunca:

```text
[ CARD ESTOURADO →→→→→ ]
```

---

## 9. Grids

Grids devem ser responsivos.

A quantidade de colunas deve depender do espaço disponível e dos limites mínimos dos componentes.

Regra:

```text
largura disponível
        ↓
quantidade de colunas adequada
        ↓
cards sem esmagamento
```

Não fixar quatro, cinco ou seis colunas independentemente da viewport.

---

## 10. Formulários

Formulários são flexíveis, mas devem possuir limites de largura.

Formulários simples não devem ocupar toda uma tela extremamente larga sem necessidade.

Preferir:

```text
container responsivo
+
max-width
+
width: 100%
```

quando apropriado.

Campos devem:

- adaptar largura;
- preservar legibilidade;
- não ultrapassar o container;
- reorganizar-se em telas menores.

---

## 11. Tabelas

Tabelas são conteúdo flexível e potencialmente largo.

Nunca permitir que uma tabela destrua o layout inteiro.

Quando necessário:

- reduzir colunas secundárias;
- permitir expansão contextual;
- utilizar visualização adaptada;
- transformar linhas em cards em telas estreitas;
- utilizar overflow controlado somente dentro da área da tabela, quando inevitável.

A barra de rolagem de uma tabela não deve virar uma barra de rolagem da aplicação inteira.

---

# PARTE IV — LIMITES DE JANELA

## 12. Tamanho mínimo

Cada experiência deve possuir uma largura mínima funcional.

O valor exato deve ser definido por plataforma e tela após implementação e testes.

Regra:

> **Nunca escolher um número arbitrário apenas para fazer o layout caber. O mínimo deve ser tecnicamente validado pela interface.**

Se a janela ficar abaixo do mínimo funcional:

- a aplicação deve impedir dimensões inadequadas quando a plataforma permitir;
- ou mudar para um layout responsivo apropriado;
- ou utilizar navegação compacta;
- ou apresentar uma orientação clara ao usuário.

Nunca deixar a interface simplesmente quebrar.

---

## 13. Desktop

No Desktop Tauri, a janela principal deve possuir:

- tamanho inicial definido;
- largura mínima;
- altura mínima;
- comportamento de maximização;
- comportamento de restauração;
- redimensionamento controlado;
- suporte a diferentes proporções de monitor.

O tamanho mínimo deve ser compatível com:

```text
menu/navegação
+
cabeçalho
+
conteúdo essencial
```

sem sobreposição.

Os valores definitivos devem ser registrados na configuração real do aplicativo depois da validação visual.

---

## 14. Web App

No Web App, não assumir uma resolução específica.

Deve funcionar em:

- notebook;
- monitor pequeno;
- monitor grande;
- janela parcialmente redimensionada;
- tela de alta resolução;
- diferentes escalas do sistema.

A interface deve responder ao espaço disponível, não somente ao tamanho físico do monitor.

---

# PARTE V — RESPONSIVIDADE

## 15. Breakpoints

Breakpoints devem ser definidos pelo comportamento da interface.

Não criar dezenas de breakpoints sem necessidade.

O princípio é:

```text
Espaço suficiente
→ layout completo

Espaço intermediário
→ compactar

Espaço pequeno
→ reorganizar

Espaço muito pequeno
→ navegação alternativa
```

Os breakpoints definitivos devem ser documentados no Design System do projeto.

---

## 16. Não usar "pixel magic"

É proibido resolver problemas de responsividade com dezenas de valores arbitrários.

Evitar:

```text
margin-left: 173px;
width: 847px;
left: 286px;
```

quando esses valores forem utilizados apenas para fazer uma tela específica parecer correta.

Preferir:

- flexbox;
- CSS Grid;
- containers;
- min/max;
- clamp;
- unidades relativas;
- constraints;
- componentes responsivos.

---

# PARTE VI — ÁREAS FIXAS VS FLEXÍVEIS

## 17. Classificação obrigatória

Todo novo componente estrutural deve ser classificado como:

```text
FIXO
FLEXÍVEL
CONDICIONAL
RESPONSIVO
```

### FIXO

Exemplos:

- estrutura do menu;
- cabeçalho;
- controles estruturais;
- elementos de navegação essenciais.

"Fixo" significa estruturalmente ancorado, não necessariamente com largura/altura absolutamente imutáveis em todas as plataformas.

### FLEXÍVEL

Exemplos:

- conteúdo;
- cards;
- grids;
- formulários;
- listas;
- painéis;
- gráficos;
- áreas de texto.

### CONDICIONAL

Pode aparecer ou desaparecer conforme:

- tamanho da tela;
- permissão;
- estado;
- contexto;
- dispositivo.

### RESPONSIVO

Muda sua organização conforme o espaço.

---

## 18. Regra de prioridade espacial

Quando faltar espaço, a ordem de adaptação deve ser:

```text
1. Remover espaçamento excessivo
2. Reduzir quantidade de colunas
3. Reorganizar componentes
4. Recolher elementos secundários
5. Compactar navegação
6. Usar submenu/drawer
7. Adaptar componentes complexos
8. Somente então considerar rolagem local
```

Nunca simplesmente deixar os componentes estourarem.

---

# PARTE VII — MENU E CABEÇALHO

## 19. Menu sem crescimento vertical

O menu lateral deve seguir também a documentação de categorias e submenus.

Não utilizar uma lista infinita.

Quando surgirem novas funcionalidades:

```text
nova funcionalidade
       ↓
categoria existente?
       ↓ sim
adicionar como item/submenu

       ↓ não
nova categoria
       ↓
categoria recolhível
```

O menu deve permanecer compacto.

---

## 20. Cabeçalho sem crescimento

O cabeçalho não deve aumentar indefinidamente conforme novas ações sejam adicionadas.

Quando houver excesso de ações:

- agrupar;
- usar menu contextual;
- mover ações secundárias;
- usar dropdown;
- usar overflow menu;
- manter apenas ações prioritárias visíveis.

---

# PARTE VIII — MOBILE

## 21. Mobile não é desktop espremido

No Android/iOS:

```text
Desktop
→ menu lateral

Mobile
→ drawer / hamburger / navegação apropriada
```

O conteúdo deve ser reorganizado.

Não simplesmente reduzir tudo até ficar ilegível.

---

# PARTE IX — COMPONENTES E ESTADOS

## 22. Estados devem ser responsivos

Componentes precisam prever:

- loading;
- vazio;
- erro;
- sucesso;
- conteúdo longo;
- conteúdo curto;
- ausência de imagem;
- textos grandes;
- listas grandes;
- permissões diferentes.

Um componente que funciona apenas com dados curtos não está pronto.

---

## 23. Texto longo

Nunca assumir que textos terão comprimento fixo.

Botões, títulos, nomes de arquivos, nomes de integrações e mensagens podem crescer.

O layout deve prever:

- truncamento apropriado;
- tooltip quando necessário;
- quebra controlada;
- expansão;
- altura adequada.

Nunca deixar texto atravessar outro componente.

---

# PARTE X — MONITORES GRANDES

## 24. Monitor ultrawide

Monitor maior não deve fazer o conteúdo simplesmente crescer infinitamente.

Usar:

```text
sidebar
+
conteúdo com max-width
+
áreas de espaço controlado
```

quando apropriado.

O objetivo é aproveitar o espaço sem destruir legibilidade.

---

# PARTE XI — MULTIMONITOR

## 25. Mudança de monitor

Quando o aplicativo mudar de monitor ou resolução:

- não deve perder layout;
- não deve ficar fora da área visível;
- deve restaurar posição válida;
- deve respeitar limites;
- deve adaptar escala quando necessário.

No Desktop, posições persistidas devem ser validadas antes de serem reutilizadas.

---

# PARTE XII — REGRA PARA IA

## 26. Antes de criar qualquer tela

A IA deve identificar:

```text
1. Plataforma
2. Tamanho/viewport
3. Estrutura fixa
4. Área flexível
5. Componentes condicionais
6. Largura mínima
7. Altura mínima
8. Comportamento de redução
9. Comportamento mobile
10. Comportamento em monitor grande
```

---

## 27. Antes de aprovar uma tela

Verificar:

- [ ] menu não estoura;
- [ ] cabeçalho não estoura;
- [ ] conteúdo não invade navegação;
- [ ] não existe overflow horizontal inesperado;
- [ ] cards reorganizam;
- [ ] grids reorganizam;
- [ ] formulários cabem;
- [ ] textos longos não quebram o layout;
- [ ] tabelas possuem tratamento;
- [ ] janela pequena continua funcional;
- [ ] monitor grande continua legível;
- [ ] mobile possui composição própria;
- [ ] elementos fixos permanecem estruturais;
- [ ] elementos flexíveis ocupam espaço disponível;
- [ ] não foram utilizados valores arbitrários para mascarar problemas.

---

# PARTE XIII — REGRA ABSOLUTA

> **NENHUMA TELA DO FLOW AI PODE SER CONSIDERADA PRONTA SE FUNCIONAR SOMENTE EM UMA RESOLUÇÃO. TODA INTERFACE DEVE TER ESTRUTURA RESPONSIVA, LIMITES FUNCIONAIS, ÁREAS FIXAS BEM DEFINIDAS E ÁREAS FLEXÍVEIS BEM DEFINIDAS. MENU E CABEÇALHO SÃO ELEMENTOS ESTRUTURAIS; CONTEÚDO É FLEXÍVEL; ELEMENTOS SECUNDÁRIOS DEVEM SE ADAPTAR. QUANDO FALTAR ESPAÇO, REORGANIZAR ANTES DE CRIAR OVERFLOW OU QUEBRAR O LAYOUT.**

---

# PARTE XIV — INSTRUÇÃO CURTA PARA AGENTE

> **CONSTRUA TODAS AS TELAS DO FLOW AI COMO INTERFACES RESPONSIVAS E AUTOAJUSTÁVEIS. DEFINA CLARAMENTE O QUE É FIXO, FLEXÍVEL, CONDICIONAL E RESPONSIVO. MENU LATERAL E CABEÇALHO SÃO ESTRUTURAIS E DEVEM PERMANECER ORGANIZADOS. A ÁREA DE CONTEÚDO DEVE OCUPAR O ESPAÇO RESTANTE E SE ADAPTAR. TODA JANELA DE DESKTOP DEVE TER LIMITES MÍNIMOS FUNCIONAIS E NÃO PODE SER DEIXADA CHEGAR A UM TAMANHO QUE QUEBRE A INTERFACE. EM TELAS MENORES, REORGANIZE COMPONENTES, REDUZA COLUNAS, RECOLHA ELEMENTOS SECUNDÁRIOS E USE NAVEGAÇÃO COMPACTA. EM MONITORES GRANDES, NÃO ESTIQUE O CONTEÚDO INDEFINIDAMENTE. NÃO USE 'PIXEL MAGIC' PARA CORRIGIR RESPONSIVIDADE. TESTE JANELAS PEQUENAS, MÉDIAS, GRANDES, MOBILE E MONITORES ULTRAWIDE ANTES DE CONSIDERAR A TELA PRONTA.**
