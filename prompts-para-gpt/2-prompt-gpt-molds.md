# PROMPT: Análise de Imagens "molds" e Construção do Painel Flow

```markdown
# CONTEXTO DO PROJETO FLOW V3.1

## Histórico Recentemente Concluído
- **5 docs lidas** da pasta `/home/flow-social/docs/`
- **Integrações locais implementadas** (10 categorias): clima, sistema, clipboard, compras, notas, rotinas multi-step, WhatsApp/Gmail/Calendar via Playwright
- **Bipe removido** do assistente de voz (já estava pronto)
- **Frontend**: 11 telas totais (2 novas: Integrações + Rotinas)
- **Backend**: 20+ endpoints `/api/integracoes/*`
- **Services systemd**: rodando via symlink `~/flow-server`

## Estrutura Atual do Flow
- **Backend**: FastAPI uvicorn em `localhost:8000`
- **Frontend**: React+Vite em `localhost:5173`
- **Menu lateral**: 13 ícones (home, chat, acao, timers, receitas, música, foco, integracoes, rotinas, tasks, vision, settings, logs)
- **Padrão visual**: #0f0f12 (fundo), #1a1a23 (cards), #8b5cf6/06b6d4 (gradients), text-white
- **Ícones**: lucide-react (Home, MessageSquare, AlarmClock, ChefHat, Music, Timer, Brain, Sparkles, X, Link2, CloudSun, Gauge, ShoppingCart, NotebookPen, Wrench, ClipboardCopy)

# OBJETIVO DA IA ATUAL

Analisar imagens na pasta `molds` e construir/continuar o desenvolvimento do painel Flow de acordo com o que está nas imagens e consistente com a implementação v3.1 já feita.

# INSTRUÇÕES

## 1. ANÁLISE DAS IMAGENS

### Pasta de Entrada
- `[PASTA/molds/]` contendo prints/mockups/designs das telas do sistema
- Cada imagem pode representar: uma tela completa, um componente, um estado da interface, ou um fluxo específico

### O Que Identificar Em Cada Imagem
- **Nome da tela/título** visível na interface
- **Categoria** da tela (home, chat, configuracao, integracao, rotina, etc)
- **Componentes visíveis**: botões, inputs, cards, tabelas, áreas destacadas
- **Layout**: disposição dos elementos, sidebar, barra superior, rodapé
- **Cores e estilo**: paleta utilizada (confere com o padrão #0f0f12/1a1a23/8b5cf6/06b6d4)
- **Ícones usados**: lucide-react icons identificados
- **Estado da tela**: ativa/inativa, carregando, erro, vazio
- **Relação com backend**: há referências a endpoints `/api/*`? há dados sendo exibidos?

## 2. MAPA DE TELA E NAVEGAÇÃO

### A. Lista Estruturada de Telas
Organizar todas as telas encontradas em ordem hierárquica, indicando:
- **Status**: Já existe no código / Nova / Requer ajuste
- **Categoria** (dashboard, chat, configuracao, integracao, rotina, etc)
- **Rota** associada (ex: `/`, `/chat`, `/integracoes`, `/rotinas`)
- **Componentes principais** identificados

### B. Matriz de Navegação
Tabela mostrando como se navega entre telas:
```
De \ Para | Home | Chat | Acao | Timers | Receitas | Musica | Foco | Integracoes | Rotinas | Tasks | Vision | Settings | Logs
---------------------------------------------------------------------------------------------------------------------------------
Home       | •      | •     | •      | •      | •        | •      | •      | •      | •            | •       | •     | •      | •        | •
Chat       | •      | •     | •      | •      | •        | •      | •      | •      | •            | •       | •     | •      | •        | •
...
Integracoes| •      | •     | •      | •      | •        | •      | •      | •      | •            | •       | •     | •      | •        | •
Rotinas    | •      | •     | •      | •      | •        | •      | •      | •      | •            | •       | •     | •      | •        | •
```

### C. Relação com Endpoints Backend
Para cada tela, identificar:
- **Endpoint já existente** no `backend/main.py` (ex: `/api/timers`, `/api/receitas`)
- **Endpoint que precisa ser criado** (descrever função lógica)
- **Usa integração local** do `core/integracoes.py` (clima, sistema, compras, etc)
- **Não tem relação** com Flow atual (pode ser descartado ou usado como inspiração)

## 3. O QUE GERAR/construir

### Prioridade 1: Telas Completamente Novas
Para telas que não existem nem no backend nem no frontend:
- **Gerar código React/Vite** no `frontend/src/App.jsx`
  - Novo ícone no menu lateral (usar ícone lucide adequado)
  - Estado `useState` para dados da tela
  - `useEffect` fetch para o endpoint correspondente
  - JSX da tela organizada igual às demais (cards, glass, botões no padrão)
- **Gerar endpoint no backend** em `backend/main.py`
  - Rota `@app.post` ou `@app.get` em `/api/...`
  - Função lógica (usar `core/integracoes.py` se for integração local já existente)
  - Modelo Pydantic se necessário receber/dataset
- **Atualizar menu**: adicionar item no array `screens` no topo do App.jsx

### Prioridade 2: Componentes Individuais
- Botões, inputs, cards ou sections específicos que podem ser reutilizados
- Código fragmentado para copiar/colar em telas existentes (manter padrão de classes `glass rounded-2xl p-4/5 bg-black/40 border border-white/10`)

### Prioridade 3: Atualizações de Lógica
- Se a imagem mostrar fluxo que já tem endpoint parcialmente implementado
- Ajustar a função backend para aceitar novos parâmetros
- Adicionar novo campo no modelo de dados existente

### Prioridade 4: Documentação
- Atualizar `README.md` com novas capacidades (já está escrito, só atualizar)
- Atualizar `flow_system_prompt.txt` com novos prompts de sistema se houver nova funcionalidade de voz
- Adicionar changelog mental do que mudou

## 4. FORMATO DE SAÍDA ESPERADO

### A. Relatório em Markdown (`relatorio-mapes.md`)
```markdown
# Análise de Telas - Flow v3.1

## Total de Telas: N

### Tela 1: "Nome da Tela"
- **Status**: Já existe / Nova / Requer ajuste
- **Arquivo(s) imagem**: `molds/nome.png`
- **Categoria**: dashboard / chat / configuracao / integracao / rotina / etc
- **Componentes identificados**: [lista detalhada]
- **Backend**: Endpoint já existe (`/api/...`) / Precisa criar / Usar integração local
- **Frontend**: Componente já existe no App.jsx / Precisa criar / Ajustar estilo
- **Rota**: `/nome-da-tela` / `/api/endpoint`
- **Código gerado**: [trecho do código gerado]
- **Próximos passos**: [o que fazer para implementar]
```

### B. Matriz de Ações Pendentes (`acoes-pendentes.md`)
```markdown
## Ações para o Próximo Agente

### Código Frontend Pendente
- [ ] Adicionar tela "X" no array `screens` do App.jsx (linha X, coluna Y)
- [ ] Criar estado `useState` para dados da tela (`const [dados, setDados] = useState(null)`)
- [ ] Criar `useEffect` fetch (`fetch('/api/x', {method:'POST', body:JSON.stringify(...)})`)
- [ ] Adicionar JSX da tela no bloco `if(active==='X')` no App.jsx
- [ ] Confirmar que ícone no menu lateral usa `import { Ícone } from 'lucide-react'`

### Código Backend Pendente
- [ ] Criar endpoint `@app.post("/api/x")` em main.py
- [ ] Se for integração local: adicionar função no `core/integracoes.py`
- [ ] Criar modelo Pydantic `class XReq(BaseModel): ...` se precisar de JSON body
- [ ] Testar com: `curl -s -X POST http://localhost:8000/api/x -H 'Content-Type: application/json' -d '{"chave":"valor"}'`

### Documentação Pendente
- [ ] Verificar se README.md precisa de nova seção (provavelmente já está ok v3.1)
- [ ] Testar endpoint recém-criado com `curl` ou no frontend
```
## 5. REGRAS DE CONSISTÊNCIA COM O FLOW V3.1

### Padrões Visuais Obrigatórios
- **Fundo**: cards com `bg-black/40` ou `bg-white/5`
- **Border**: `border border-white/10` ou `border-purple-500/40`
- **Gradientes**: `from-[cor] to-[cor]` (padrão: `from-purple-500 to-cyan-400` ou `from-[8b5cf6] to-[06b6d4]`)
- **Botões**: `bg-gradient-to-br from-[cor] to-[cor] rounded-xl px-4 py-2 text-sm font-semibold flex items-center gap-2`
- **Ícones**: `lucide-react` com size adequado (ex: `size={16}` ou `size={20}`)
- **Classes utilitárias**: `flex items-center justify-between`, `w-full`, `max-w-2xl`, `mx-auto`, `mb-4`, `mt-4`

### Padrões de Código Obrigatórios
- **Hooks React**: `useState`, `useEffect`, `useRef` (nenhum outro pattern)
- **Fetch API**: `fetch('/api/...', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({...})})`
- **Tratamento de resposta**: `.then(r => r.json()).then(d => ...)` com tratamento de `d.ok` / `d.error`
- **Conditional rendering**: `if(active==='X')` / `if(d.ok)` / `if(errors)`
- **List rendering**: `.map((item, i) => <chave key={i}>{item}</chave>)` com fallback `itens.length===0 && <p>texto vazio</p>`

### Padrões de Integração Obrigatória
- **Clima**: `/api/integracoes/clima?cidade=NomeCidade` → retorna objeto com `atual.temp`, `atual.desc`, etc
- **Sistema**: `/api/integracoes/sistema` → retorna `disco`, `ram`, `cpu`, `uptime`
- **Compras**: `/api/integracoes/compras` → `acao: adicionar/remover/listar`
- **Notas**: `/api/integracoes/notas` → `acao: adicionar/concluir/listar`
- **Rotinas**: `/api/integracoes/rotinas` → `acao: criar/executar/listar/remover`
- **WhatsApp**: `/api/integracoes/whatsapp` → envia mensagem (Playwright, precisa de QR Code primeira vez)
- **Gmail/Calendar**: `/api/integracoes/gmail/abrir` e `/api/integracoes/calendario/abrir` → abre navegador

### O Que NÃO Deve Ser Repetido
- Verificar se endpoint já existe antes de criar novo (consultar main.py lines 367-763)
- Verificar se tela já no array `screens` do App.jsx (13 itens: home, chat, acao, timers, receitas, música, foco, tasks, vision, settings, logs, integracoes, rotinas)
- Verificar se função já existe em `core/acoes.py` (música, sistema, timers, receitas, visão, memória)
- Evitar criar tela que já tenha funcionalidade similar (ex: não criar "tela de timers" se já tem "timers e alarmes")

## 6. EXEMPLO PRÁTICO

### Cenário: IA analisa imagem e encontra tela "Modo Foco" com botão "Ativar 25min"

#### Se já existe no código:
- Verificar em `App.jsx` se há `active==='foco'` block
- Verificar em `main.py` se há `/api/system/focus` endpoint
- Se existir: retornar "Já implementado - só precisa visualizar em `active==='foco'`"
- Se não existir: gerar código conforme regra Prioridade 3

#### Se for nova tela:
#### Gerar:
1. **No frontend** (`App.jsx`):
   - Adicionar `'foco'` no array `screens` (ícone: `Timer`, label: `'Modo Foco'`)
   - Adicionar estado `useState` (já existe `foco` e `focoMin` no código)
   - O código já existe para `focoCmd`, `fetchFoco`, renderização do block `active==='foco'`
   - Resultado: "Já tem estrutura, só precisa preencher dados se necessário"

2. **No backend** (`main.py`):
   - Já tem `/api/system/focus` endpoint + `/api/system/focus/status`
   - Resultado: "Já implementado"

#### Se for tela completamente nova tipo "Integrações":
#### Gerar:
1. **Frontend**: já geramos antes - tem array item `{'id':'integracoes', 'label':'Integrações', 'icon':CloudSun}` + bloco `if(active==='integracoes')` com clima, sistema, compras, notas, brilho, whatsapp/gmail/calendar
2. **Backend**: já geramos antes - tem 11 endpoints `/api/integracoes/*`
3. Resultado: "Tela já implementada na versão v3.1 - apenas confirmar se imagens mostram mesma estrutura"

## 6. INPUT ESPECÍFICO PARA ESTE PROJETO

Ao analisar as imagens do Flow, preste atenção especial:

1. **Se a imagem mostra tela de "Integrações"** - deve conter cards de clima (com campo cidade + dados temp/umidade/vento), sistema (disco/RAM/CPU/temp/uptime), lista de compras (itens com botão add/remover), notas (texto + checkbox feita ✓), brilho (slider 0-100%), botões WhatsApp (digitar contato + mensagem + enviar), Gmail (botão ler emails), Calendário (botão ver eventos)
2. **Se a imagem mostra tela de "Rotinas"** - deve conter builder visual (input "Nome da rotina" + linhas de passos com tipos: notificação/comando/musica/timer/clima/esperar + input valor + botão remover linha + botão criar rotina) + lista de rotinas criadas + botões executar/remover cada rotina
3. **Se a imagem mostra tela nova** - comparar com as 11 telas já existentes (home, chat, acao, timers, receitas, música, foco, tasks, vision, settings, logs, integracoes, rotinas) e identificar o que é diferente/novidade
4. **Verificar se há referências a `/api/...`** nas imagens - anotar qual endpoint e verificar se backend já responde (consultar main.py)
5. **Identificar componentes reutilizáveis** - inputs com classe `flex-1 bg-black/40 border border-white/10 rounded-xl px-3 py-2 outline-none focus:border-purple-500`, cards com `glass rounded-2xl p-4`, botõesgradientes `from-purple-500 to-cyan-400`

## 6. FORMATO DE SAÍDA RECOMENDADO

### 1. `relatorio-mapes.md`
```markdown
# Flow v3.1 - Análise de Telas da pasta molds

## Resumo Executivo
- Total de imagens analisadas: N
- Telas já implementadas: M (já existem no código v3.1)
- Telas novas: K (precisam ser criadas)
- Telas removidas/descartadas: R

## Detalhe das Telas
[lista de todas as telhas com status, endpoint, próximo passo]

## Endpoints Backend: Status
- `/api/timers`: ✅ Já implementado
- `/api/receitas`: ✅ Já implementado  
- `/api/musica`: ✅ Já implementado
- `/api/integracoes/*`: ✅ Já implementado (11 endpoints)
- `/api/novo-endpoint`: ❌ Precisa ser criado (descrever)

## Telas para Implementação Imediata
1. Tela X: descrição + próximo passo
2. Tela Y: descrição + próximo passo
```

### 2. `acoes-pendentes.md`
```markdown
# Ações para Continuar o Flow v3.1

## Frontend (editando App.jsx)
- [ ] Inserir nova tela no array `screens` (linha X, coluna Y)
- [ ] Adicionar bloco `if(active==='NomeTela')` no return do componente principal (após o block `active==='logs'`)
- [ ] Criar/verificar estado `useState` necessário (já tem: home/chat/timers/ etc)
- [ ] Adicionar `useEffect` fetch para endpoint backend se houver dados dinâmicos
- [ ] Confirmar que ícone no menu lateral usa `import { Ícone } from 'lucide-react'`

## Backend (editando main.py)
- [ ] Verificar se endpoint já existe na lines 367-763
- [ ] Se não existir: adicionar `@app.post("/api/...")` ou `@app.get("/api/...")`
- [ ] Se for integração local: adicionar função no `core/integracoes.py` (clima/sistema/compras/notas/rotinas)
- [ ] Criar modelo Pydantic se precisar de validação de JSON body
- [ ] Testar endpoint: `curl -s -X POST http://localhost:8000/api/... -H 'Content-Type: application/json' -d '{"chave":"valor"}'`

## Testes
- [ ] Rodar backend: `systemctl --user restart flow-backend.service`
- [ ] Rodar frontend: `node node_modules/vite/bin/vite.js build` (em frontend/)
- [ ] Testar na tela do navegador `localhost:5173`
- [ ] Testar via voz no assistente (se houver fala envolvida)
```
## 7. ORIENTAÇÕES FINAIS PARA A IA

1. **Sempre verificar o código existente primeiro** - o Flow v3.1 tem bastante coisa já feita (70+ endpoints, 11 telas, todas as integrações locais). Criar algo novo só se realmente não existir.

2. **Manter padrão visual** - as classes CSS, cores e ícones já estão definidos. Usar o que já existe ao invés de criar do zero sempre que possível.

3. **Usar integrações locais** - o projeto já tem clima (wttr.in), sistema (disk/RAM/CPU/brilho), compras CRUD, notas CRUD, rotinas multi-step, WhatsApp/Gmail/Calendar. Se a imagem precisar de alguma dessas funcionalidades, usar o que já existe antes de criar algo novo.

4. **Salvar em formatos estruturados** - `relatorio-mapes.md` e `acoes-pendentes.md` facilitam a vida do próximo agente/humano continuar o trabalho.

5. **Comunicar o que já está pronto** - poupar tempo do próximo sistema informando o que já funciona, para que ele só se preocupe no que realmente falta.

Pronto. Este prompt está pronto para ser salvo como `prompt-gpt-molds.md` (ou o nome que preferir) e dado para a próxima IA analisar as imagens da pasta `molds/` e gerar os relatórios e códigos necessários para continuar o desenvolvimento do Flow v3.1.

O próximo passo: colocar as imagens na pasta `molds/` e rodar a IA com este prompt. Ela vai retornar:
1. Quanto já está implementado
2. O que precisa ser criado do zero
3. Código React/Vite para novos components
4. Código FastAPI para novos endpoints
5. Matriz de o que já funciona vs. o que falta

Pronto para usar. Basta colocar as imagens na pasta `molds/` e rodar a IA com este prompt.
```