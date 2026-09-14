# Prompt para IA Gerar Mapa de Telas

```markdown
# OBJETIVO
Analisar imagens de interfaces de software e criar um mapa estruturado de todas as telas/páginas, incluindo seus componentes, navegação e relações.

# ENTRADA
- [PASTA DE IMAGENS] Contendo prints/mockups/designs das telas do sistema
- [MAPA INICIAL] (opcional) Documento com nome das telas conhecidas

# INSTRUÇÕES PARA A IA

## 1. ANÁLISE DE CADA IMAGEM
Para cada imagem identificada:

### A. Identificação Básica
- **Nome da tela**: Título ou rótulo visível
- **Categoria**: (home, chat, configuracao, ferramenta, etc.)
- **Ícone/símbolo**: Elementos identificadores na interface

### B. Layout e Estrutura
- **Posição do menu lateral**: Lado (esquerda/direita), viscol/não visível
- **Barra superior**: Presente/ausente, contém quais elementos (perfil, busca, notificações)
- **Áreas principais**: Quantas colunas/linhas, disposição dos componentes
- **Rodapé**: Informações exibidas (versão, data, status)

### C. Componentes Identificados
- **Botões**: Tipos (primary, secondary, danger), labels, ações associadas
- **Campos de input**: Tipos (texto, número, select, área), labels, placeholders
- **Tabelas/listas**: Colunas, ordenação, itens exemplificativos
- **Gráficos/KPIs**: Métricas exibidas, indicadores visuais
- **Modais/dialogs**: Quando aparecem, quais botões têm
- **Imagens/ícones**: Lucide icons, fotografias, ilustrações

### D. Navegação e Links
- **Para onde leva cada botão/links**
- **Rotas/urls** associadas (se conhecidas)
- **Estado atual** destacando qual tela está ativa
- **Fluxo de usuário** entre telas

## 2. MAPA GERAL DE TELA

### A. Lista Estruturada
Organizar todas as telas encontradas em ordem hierárquica:

```
1. HOME - Tela principal
   - Componentes: [lista]
   - Rota: /home
   
2. CHAT - Conversas
   - Componentes: [lista]  
   - Rota: /chat
...
```

### B. Matriz de Navegação
Tabela mostrando como se navega entre telas:

| De \ Para | Tela 1 | Tela 2 | Tela 3 |
|-----------|---------|---------|---------|
| **Tela 1** | • | • | • |
| **Tela 2** | • | • | • |
| **Tela 3** | • | • | • |

### C. Grupos e Categorias
Agrupar telas por funcionalidade:
- **Painel de Controle**: telas de visão geral
- **Configurações**: ferramentas de ajuste
- **Funcionalidades**: recursos principais do software

## 3. OUTPUT STRUCTURED (JSON/Markdown)

### Formato recomendado:
```json
{
  "total_telas": N,
  "telas": [
    {
      "id": "home",
      "nome": "Tela Principal",
      "icone": "Home",
      "categoria": "dashboard",
      "componentes": [...],
      "rotas": ["/home"],
      "proximas": ["chat", "configuracao"],
      "anterior": null
    },
    ...
  ],
  "navegacao": {
    "menu_principal": ["home", "chat", "acao", ...],
    "submenus": {
      "configuracao": ["perfil", "configuracoes_sistema"]
    }
  }
}
```

## 4. INFORMAÇÕES ADICIONAIS SOLICITADAS

- **Consistência visual**: Cores, tipografia, estilos repetidos
- **Responsividade**: Como as telas se comportam em diferentes tamanhos
- **Acessibilidade**: Contraste, labels, ordem de tabulação
- **Interações**: Efeitos hover, animações, estados ativos
- **Dados mock**: Tipos de dados apresentados em cada tela

# PARA ESTE PROJETO FLOW ESPECIFICO

Ao analisar as imagens do painel Flow, preste atenção especial em:

1. **Padrão já existente**: O sistema usa React+Vite com icons lucide-react
2. **Paleta de cores**: #0f0f12 (fundo), #1a1a23 (cards), #8b5cf6/06b6d4 (gradients), text-white
3. **Estrutura de menu**: 72px lateral com ícones, botões de gradiente roxo/ciano
4. **Tipos de tela já implementadas**: home, chat, acao, timers, receitas, musica, foco, tasks, vision, settings, logs
5. **Novas a adicionar**: based on your images - integracoes, rotinas, etc.

# EXEMPLO DE SAÍDA ESPERADA

```markdown
# MAPA DE TELAS - FLOW V3.1

## Telas Totais: 15

1. **Home** (já existe)
   - Ícone: Home
   - Componentes: orb, mic, tempo, relógio
   - Rota: /

2. **Chat** (já existe)
   - Ícone: MessageSquare
   - Componentes: mensagem input, botão send, histórico

3. **Integrações** (NOVA)
   - Ícone: CloudSun
   - Componentes: cards clima, sistema, compras, notas, brilho, whatsapp/gmail/calendar
   - Rota: /integracoes

4. **Rotinas** (NOVA)
   - Ícone: Wrench
   - Componentes: builder de rotinas, lista de rotinas, executar/remover
   - Rota: /rotinas

## Navegação Principal
Home → Chat → Ação → Timers → Receitas → Música → Foco → Integrações → Rotinas → Tasks → Vision → Settings → Logs
```
```