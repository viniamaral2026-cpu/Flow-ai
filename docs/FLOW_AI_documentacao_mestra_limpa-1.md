# FLOW AI --- DOCUMENTAÇÃO MESTRA

## Mapa de Telas, Arquitetura Visual, Navegação, Estados e Plano de Implementação

**Documento:** Especificação consolidada do produto\
**Objetivo:** servir como referência única para análise das telas,
design, implementação e continuidade por agentes de IA.\
**Base:** inventário consolidado de 567 telas + Prompt de Mapa de
Telas + Prompt de análise dos molds.

------------------------------------------------------------------------

# 1. Objetivo

O objetivo deste documento é consolidar o mapa completo do FLOW AI e
estabelecer um processo único para:

-   identificar todas as telas e estados do produto;
-   distinguir telas já produzidas das que ainda precisam ser
    produzidas;
-   documentar componentes, navegação e relações entre telas;
-   evitar duplicação;
-   preservar consistência visual;
-   separar páginas reais de estados da interface;
-   orientar futuras implementações de frontend e backend;
-   permitir que outro agente continue o trabalho sem perder contexto.

O processo de análise deve partir das imagens/mockups quando elas
estiverem disponíveis. Cada imagem pode representar uma tela completa,
componente, estado ou fluxo específico.

------------------------------------------------------------------------

# 2. Princípio fundamental

## NÃO DUPLICAR

Antes de criar qualquer tela, componente ou endpoint:

1.  verificar se a tela já existe;
2.  verificar se existe uma tela equivalente;
3.  verificar se a funcionalidade já está implementada;
4.  verificar se o endpoint correspondente já existe;
5.  verificar se o componente pode ser reutilizado;
6.  somente depois decidir entre:
    -   já implementado;
    -   requer ajuste;
    -   novo;
    -   duplicado;
    -   descartável.

Esse princípio é obrigatório para evitar que o projeto acumule versões
diferentes da mesma funcionalidade.

------------------------------------------------------------------------

# 3. Inventário geral

O inventário consolidado contém aproximadamente **567 telas e estados de
interface**.

É importante diferenciar:

-   **Página:** rota ou área principal do aplicativo.
-   **Tela:** experiência visual específica.
-   **Estado:** variação visual de uma tela, como loading, vazio, erro
    ou sucesso.
-   **Modal:** interação sobre uma tela existente.
-   **Fluxo:** sequência de telas/estados.
-   **Componente:** elemento reutilizável.

Portanto, 567 itens não significam necessariamente 567 URLs.

Exemplo:

`/timers`

pode apresentar:

-   timer criado;
-   timer em execução;
-   timer pausado;
-   timer concluído;
-   timer cancelado;
-   erro;
-   vazio.

Esses estados podem compartilhar uma única rota.

------------------------------------------------------------------------

# 4. Categorias do FLOW AI

O inventário está organizado nos seguintes módulos:

1.  Site / área pública
2.  Autenticação
3.  Onboarding
4.  Dashboard
5.  Chat
6.  Voz / Assistente
7.  Rotinas / Automações
8.  Timers
9.  Casa Inteligente
10. Integrações
11. Integrações específicas
12. Memória
13. Arquivos
14. Saúde e Bem-estar
15. Receitas / Alimentação
16. Personalização da FLOW
17. Skills
18. API / Desenvolvedor
19. Conta / Perfil
20. Segurança
21. Privacidade / Dados
22. Planos / Assinatura
23. Pagamentos
24. Notificações
25. Suporte
26. Status / Sistema
27. Componentes e estados globais
28. Mobile / PWA
29. Wear OS
30. Experiências especiais da FLOW

------------------------------------------------------------------------

# 5. Site e área pública

A área pública deve funcionar sem o shell interno do aplicativo.

Inclui:

-   Home
-   Como funciona
-   Recursos
-   FLOW AI para pessoas
-   FLOW AI para famílias
-   FLOW AI para empresas
-   Inteligência artificial
-   Memória
-   Voz
-   Visão computacional
-   Automação
-   Casa inteligente
-   Saúde
-   Rotinas
-   Integrações
-   Skills
-   API
-   Segurança
-   Privacidade
-   Planos
-   Comparação de planos
-   FAQ
-   Contato
-   Sobre
-   Blog
-   Artigo
-   Termos
-   Política de privacidade
-   Política de cookies
-   Status

## Regra visual

Páginas públicas não devem apresentar o menu lateral interno do
aplicativo.

------------------------------------------------------------------------

# 6. Autenticação

Fluxos:

-   Login
-   Criar conta
-   Confirmação de e-mail
-   Reenvio de confirmação
-   Recuperação de senha
-   Redefinição de senha
-   Senha alterada
-   Conta criada
-   Conta bloqueada
-   Conta suspensa
-   Sessão expirada
-   Login social
-   Verificação de segurança
-   Verificação de identidade
-   Código de acesso
-   Recuperação de conta

## Regra

As telas de autenticação externas devem ser independentes do dashboard
interno.

------------------------------------------------------------------------

# 7. Onboarding

Fluxo inicial:

1.  Boas-vindas
2.  Criar perfil
3.  Nome
4.  Avatar
5.  Idioma
6.  Fuso horário
7.  Personalidade
8.  Nome da FLOW
9.  Voz
10. Wake Word
11. Permissões
12. Microfone
13. Notificações
14. Localização
15. Câmera
16. Arquivos
17. Integrações
18. Dispositivo principal
19. Preferências
20. Objetivos
21. Finalização

O onboarding deve preparar a configuração inicial sem obrigar o usuário
a configurar todos os recursos avançados de uma vez.

------------------------------------------------------------------------

# 8. Dashboard

O dashboard é o centro do aplicativo.

Deve contemplar:

-   visão geral;
-   atalhos;
-   atividade recente;
-   sugestões;
-   favoritos;
-   itens recentes;
-   notificações;
-   status da FLOW;
-   processamento;
-   escuta;
-   resposta;
-   execução;
-   confirmação.

A arquitetura visual deve ser consistente com o restante do aplicativo.

------------------------------------------------------------------------

# 9. Chat

O módulo de chat contempla:

-   nova conversa;
-   conversa em andamento;
-   detalhes;
-   pesquisa;
-   renomear;
-   arquivar;
-   conversas arquivadas;
-   excluir;
-   confirmação;
-   compartilhar;
-   exportar;
-   vazio;
-   offline;
-   erro;
-   anexos;
-   imagens;
-   PDF;
-   visão;
-   resultado da IA;
-   ação executada;
-   confirmação antes da ação;
-   resultado da ação;
-   erro;
-   pesquisa interna;
-   copiar;
-   regenerar;
-   continuar resposta;
-   feedback.

## Fluxo principal

Usuário → mensagem → FLOW processa → resposta → possível ferramenta →
confirmação quando necessária → ação → resultado.

------------------------------------------------------------------------

# 10. Voz e assistente

Estados:

-   ativar voz;
-   ouvindo;
-   processando;
-   respondendo;
-   histórico;
-   configurar voz;
-   testar voz;
-   treinar Wake Word;
-   testar Wake Word;
-   microfone;
-   dispositivos autorizados;
-   diagnóstico;
-   privacidade;
-   dados de áudio;
-   histórico de comandos;
-   indisponível;
-   microfone bloqueado.

A experiência de voz deve comunicar claramente em qual estado a FLOW
está.

------------------------------------------------------------------------

# 11. Rotinas e automações

O construtor deve permitir:

-   criar rotina;
-   editar;
-   visualizar;
-   duplicar;
-   pausar;
-   ativar;
-   excluir;
-   confirmar exclusão;
-   testar;
-   visualizar resultado;
-   criar gatilho;
-   criar condição;
-   criar ação;
-   reordenar ações;
-   horário;
-   recorrência;
-   dispositivo;
-   integração;
-   histórico;
-   execução;
-   falha;
-   rotina vazia;
-   rotina desativada.

Uma rotina pode ser representada como:

`Gatilho → Condições → Ações → Resultado`

------------------------------------------------------------------------

# 12. Timers

Estados e operações:

-   lista;
-   criar;
-   executar;
-   pausar;
-   concluir;
-   cancelar;
-   editar;
-   duplicar;
-   excluir;
-   histórico;
-   detalhes;
-   recorrência;
-   som;
-   vibração;
-   Wear OS;
-   segundo plano;
-   limite do plano.

------------------------------------------------------------------------

# 13. Casa Inteligente

O módulo deve contemplar:

-   casa;
-   cômodos;
-   criação/edição/exclusão de cômodo;
-   dispositivos;
-   descoberta;
-   pareamento;
-   QR Code;
-   conexão;
-   falha;
-   detalhes;
-   edição;
-   remoção;
-   confirmação;
-   cenas;
-   automações;
-   histórico;
-   dispositivo offline;
-   falta de permissão.

------------------------------------------------------------------------

# 14. Integrações

Fluxo padrão:

`Catálogo → Detalhes → Conectar → OAuth/Autorização → Conectada → Configuração`

Estados adicionais:

-   sincronização;
-   concluída;
-   falha;
-   expirada;
-   indisponível;
-   logs;
-   permissões;
-   desconexão.

Integrações específicas podem incluir WhatsApp, Instagram, Gmail,
Calendar, Drive, Microsoft, Discord, Slack, Spotify, Wear OS e serviços
de casa inteligente.

------------------------------------------------------------------------

# 15. Memória

Operações:

-   visualizar memória;
-   adicionar;
-   editar;
-   detalhes;
-   excluir;
-   confirmar;
-   pesquisar;
-   filtrar;
-   categorizar;
-   memória criada;
-   atualizada;
-   protegida;
-   indisponível;
-   importar;
-   exportar;
-   preferências;
-   visualizar o que a FLOW lembra;
-   controle de memória.

A memória deve possuir controles claros de transparência e
gerenciamento.

------------------------------------------------------------------------

# 16. Arquivos

Fluxo:

`Arquivos → Upload → Processamento → Concluído/Falha → Visualização`

Operações:

-   visualizar;
-   detalhes;
-   editar informações;
-   renomear;
-   mover;
-   criar pasta;
-   editar pasta;
-   excluir;
-   compartilhar;
-   permissões;
-   download;
-   pesquisa;
-   filtros.

Estados:

-   upload em andamento;
-   concluído;
-   falhou;
-   não encontrado;
-   armazenamento cheio.

------------------------------------------------------------------------

# 17. Saúde e bem-estar

Módulos:

-   visão geral;
-   indicadores;
-   dados;
-   metas;
-   medicamentos;
-   exames;
-   consultas;
-   dispositivos fitness;
-   sincronização.

Estados de sincronização e indisponibilidade devem ser representados.

------------------------------------------------------------------------

# 18. Receitas e alimentação

Inclui:

-   pesquisa;
-   filtros;
-   detalhes;
-   favoritos;
-   compartilhamento;
-   abertura externa;
-   histórico;
-   preferências alimentares;
-   ingredientes disponíveis;
-   busca por ingredientes;
-   receita gerada pela FLOW;
-   plano alimentar;
-   lista de compras.

------------------------------------------------------------------------

# 19. Personalização da FLOW

Configurações:

-   personalidade;
-   comportamento;
-   autonomia;
-   modelo;
-   visão;
-   voz;
-   memória;
-   permissões;
-   preferências de resposta;
-   criatividade;
-   proatividade;
-   estilo;
-   regras personalizadas.

------------------------------------------------------------------------

# 20. Skills

Fluxo:

`Marketplace → Skill → Detalhes → Instalar → Permissões → Instalada → Executar → Resultado`

Também:

-   minhas Skills;
-   criar;
-   editar;
-   configurar;
-   logs;
-   publicar;
-   revisão;
-   publicada;
-   despublicar;
-   remover.

------------------------------------------------------------------------

# 21. API e desenvolvedor

Área:

-   Developer Dashboard;
-   visão geral;
-   API Keys;
-   criação;
-   visualização;
-   revogação;
-   confirmação;
-   Webhooks;
-   criação;
-   edição;
-   teste;
-   recebimento;
-   falha;
-   logs;
-   requisição;
-   Sandbox;
-   endpoints;
-   resultados;
-   erros;
-   limites;
-   documentação;
-   SDKs;
-   exemplos.

------------------------------------------------------------------------

# 22. Conta

Inclui:

-   minha conta;
-   perfil;
-   editar perfil;
-   foto;
-   dados pessoais;
-   e-mail;
-   telefone;
-   idioma;
-   região;
-   fuso;
-   preferências;
-   acessibilidade.

------------------------------------------------------------------------

# 23. Segurança

Fluxos:

-   segurança;
-   alteração de senha;
-   2FA;
-   autenticador;
-   confirmação;
-   códigos de recuperação;
-   regeneração;
-   dispositivos;
-   sessões;
-   encerramento;
-   login recente;
-   alertas;
-   atividade suspeita;
-   confirmação de identidade;
-   recuperação.

------------------------------------------------------------------------

# 24. Privacidade e dados

Inclui:

-   central de privacidade;
-   central de dados;
-   consentimentos;
-   exportação;
-   exclusão;
-   confirmação;
-   dados da conta;
-   dados da FLOW;
-   histórico;
-   áudio;
-   visão;
-   memórias;
-   integrações.

------------------------------------------------------------------------

# 25. Planos e assinatura

Fluxos:

`Planos → Comparação → Seleção → Checkout → Pagamento → Assinatura`

Também:

-   assinatura atual;
-   gerenciamento;
-   upgrade;
-   downgrade;
-   cancelamento;
-   confirmação;
-   reativação;
-   cancelada;
-   pendente;
-   expirada;
-   recurso bloqueado;
-   consumo.

------------------------------------------------------------------------

# 26. Pagamentos

Inclui:

-   checkout;
-   confirmação;
-   aprovado;
-   pendente;
-   recusado;
-   formas de pagamento;
-   cartão;
-   Pix;
-   boleto;
-   cobrança;
-   fatura;
-   histórico;
-   nota fiscal.

------------------------------------------------------------------------

# 27. Notificações

Inclui:

-   central;
-   preferências;
-   detalhe;
-   marcar como lida;
-   limpar;
-   push;
-   e-mail;
-   FLOW;
-   segurança;
-   integrações.

------------------------------------------------------------------------

# 28. Suporte

Fluxo:

`Ajuda → Pesquisa → Artigo/Tutorial/FAQ → Chamado`

Inclui:

-   abrir chamado;
-   chamado criado;
-   meus chamados;
-   detalhes;
-   resposta;
-   anexos;
-   encerramento;
-   reabertura;
-   status.

------------------------------------------------------------------------

# 29. Sistema

Estados globais:

-   loading;
-   skeleton;
-   vazio;
-   sem resultados;
-   erro de conexão;
-   offline;
-   404;
-   500;
-   permissão negada;
-   sessão expirada;
-   recurso bloqueado;
-   limite atingido;
-   sucesso;
-   falha;
-   indisponibilidade;
-   manutenção;
-   incidente.

Esses estados devem ser componentes reutilizáveis sempre que possível.

------------------------------------------------------------------------

# 30. Mobile / PWA

O aplicativo deve contemplar:

-   instalação;
-   atualização;
-   atualização em andamento;
-   offline;
-   reconexão;
-   permissões;
-   compartilhamento;
-   menu mobile;
-   navegação mobile.

------------------------------------------------------------------------

# 31. Wear OS

Experiências:

-   tela inicial;
-   FLOW no relógio;
-   comando de voz;
-   timer;
-   notificações;
-   rotinas;
-   saúde;
-   dispositivos;
-   configurações;
-   sincronização;
-   desconectado.

------------------------------------------------------------------------

# 32. Estados especiais da FLOW

Estados comportamentais:

1.  Acordada
2.  Ouvindo
3.  Entendendo
4.  Pensando
5.  Respondendo
6.  Executando
7.  Pedindo confirmação
8.  Concluindo ação
9.  Erro
10. Precisa de informação
11. Não entendeu
12. Offline
13. Sem permissão
14. Aprendendo
15. Sugerindo ação
16. Detectando contexto
17. Usando visão
18. Usando memória
19. Usando ferramenta
20. Executando múltiplas ações

Esses estados são fundamentais para representar a personalidade e o
comportamento operacional da FLOW.

------------------------------------------------------------------------

# 33. Padrão de análise de cada imagem

Para cada imagem analisada, registrar:

## Identificação

-   nome;
-   categoria;
-   ícone;
-   finalidade.

## Layout

-   sidebar;
-   header;
-   áreas;
-   colunas;
-   cards;
-   rodapé.

## Componentes

-   botões;
-   inputs;
-   selects;
-   listas;
-   tabelas;
-   gráficos;
-   modais;
-   ícones;
-   imagens.

## Navegação

-   origem;
-   destino;
-   ação;
-   rota;
-   estado ativo;
-   fluxo.

## Estado

-   normal;
-   loading;
-   vazio;
-   erro;
-   offline;
-   sucesso;
-   confirmação;
-   bloqueado.

## Responsividade

Registrar diferenças entre:

-   desktop;
-   tablet;
-   mobile.

------------------------------------------------------------------------

# 34. Matriz de navegação

A matriz deve registrar relações entre módulos.

Formato:

  De              Para           Ação
  --------------- -------------- ------------------------
  Home            Chat           Abrir conversa
  Home            Rotinas        Abrir rotinas
  Home            Timers         Abrir timers
  Chat            Arquivos       Anexar arquivo
  Chat            FLOW           Executar ação
  Rotinas         Dispositivos   Selecionar dispositivo
  Rotinas         Integrações    Selecionar integração
  Configurações   Voz            Configurar voz
  Configurações   Segurança      Abrir segurança
  Configurações   Privacidade    Abrir privacidade

A matriz definitiva deve ser atualizada conforme as imagens e rotas
reais forem analisadas.

------------------------------------------------------------------------

# 35. Regras de implementação

A documentação antiga do projeto especifica React/Vite no frontend e
FastAPI no backend, além de hooks React, Fetch API e integração com
endpoints `/api/*`.

Para o trabalho sobre o código existente:

-   verificar o código antes;
-   reutilizar componentes;
-   reutilizar endpoints;
-   não criar endpoint duplicado;
-   não criar tela duplicada;
-   preservar contratos existentes;
-   testar frontend;
-   testar backend;
-   testar fluxos de voz quando aplicável.

------------------------------------------------------------------------

# 36. Relação com backend

Para cada nova tela, registrar:

-   endpoint existente;
-   endpoint necessário;
-   método HTTP;
-   parâmetros;
-   resposta;
-   estados de erro;
-   autenticação;
-   integração utilizada.

O Prompt 2 também determina verificar endpoints existentes antes de
criar novos e identificar quando uma tela utiliza integrações locais.

------------------------------------------------------------------------

# 37. Integrações legadas documentadas

A documentação do FLOW V3.1 registra integrações locais para:

-   clima;
-   sistema;
-   clipboard;
-   compras;
-   notas;
-   rotinas;
-   WhatsApp;
-   Gmail;
-   Calendar.

Também registra endpoints de integração e recomenda reutilizar essas
capacidades antes de criar novas implementações.

Essas informações pertencem ao contexto V3.1 e devem ser verificadas no
código atual antes de serem consideradas contrato definitivo.

------------------------------------------------------------------------

# 38. Documentação que cada agente deve produzir

## relatorio-mapes.md

Deve conter:

-   total de imagens;
-   total de telas;
-   telas existentes;
-   telas novas;
-   telas que requerem ajuste;
-   telas descartadas;
-   componentes;
-   rotas;
-   backend;
-   frontend;
-   próximos passos.

## acoes-pendentes.md

Deve conter checklists separados:

### Frontend

-   adicionar tela;
-   adicionar item ao menu;
-   criar/verificar estado;
-   criar fetch;
-   criar JSX;
-   confirmar ícone.

### Backend

-   verificar endpoint;
-   criar endpoint somente se necessário;
-   criar função de integração;
-   criar modelo de entrada;
-   testar endpoint.

### Testes

-   build;
-   backend;
-   navegador;
-   voz;
-   integração.

------------------------------------------------------------------------

# 39. Regra para agentes de IA

Um agente que continuar o projeto deve seguir esta ordem:

1.  Ler esta documentação.
2.  Ler o mapa CSV.
3.  Verificar as imagens disponíveis.
4.  Verificar o código existente.
5.  Verificar rotas.
6.  Verificar endpoints.
7.  Verificar componentes.
8.  Comparar imagem × implementação.
9.  Classificar:
    -   pronto;
    -   ajuste;
    -   novo;
    -   duplicado;
    -   descartável.
10. Implementar somente o necessário.
11. Testar.
12. Atualizar documentação.

------------------------------------------------------------------------

# 40. Regra visual atual do FLOW AI

O inventário e os prompts antigos contêm referências visuais do FLOW
V3.1 em tema escuro.

Para o novo FLOW AI, a identidade visual atual deve prevalecer:

-   fundo claro;
-   cards brancos;
-   visual SaaS moderno;
-   cantos arredondados;
-   sombras suaves;
-   gradientes;
-   aparência limpa;
-   sidebar limpa;
-   sem manchas ou artefatos;
-   experiência consistente entre telas.

Paleta atual:

-   Primary: `#6D28FF`
-   Secondary: `#4DA3FF`
-   Accent: `#FF2E9E`
-   Dark: `#11124B`
-   Gray: `#8A8AB0`
-   Gray Light: `#E6E8F0`
-   Background: `#F8F9FF`
-   Card: `#FFFFFF`
-   Border: `#EEF0FF`
-   Input: `#F9FAFF`

Gradientes:

`#6D28FF → #4DA3FF`

e

`#6D28FF → #4DA3FF → #FF2E9E`

------------------------------------------------------------------------

# 41. Regra de shell interno

Telas internas autenticadas devem utilizar o shell principal do FLOW AI:

-   sidebar;
-   header;
-   área de conteúdo;
-   navegação;
-   perfil;
-   notificações;
-   estado da FLOW.

Telas públicas e autenticação externa não devem receber o shell interno.

------------------------------------------------------------------------

# 42. Controle de duplicação

Uma tela só deve ser marcada como nova quando não houver:

-   tela equivalente;
-   estado equivalente;
-   componente reutilizável;
-   fluxo já existente.

Exemplo:

Não criar uma nova página de "Timer" apenas porque existe uma imagem de
timer pausado. Pode ser um estado da página de Timer.

O mesmo vale para:

-   sucesso;
-   erro;
-   loading;
-   vazio;
-   confirmação;
-   offline.

------------------------------------------------------------------------

# 43. Critério de conclusão visual

Uma tela só deve ser considerada concluída quando:

-   estrutura corresponde ao design;
-   hierarquia visual está correta;
-   navegação está definida;
-   estados principais existem;
-   responsividade foi considerada;
-   componentes não apresentam artefatos;
-   sidebar/header seguem o padrão;
-   textos estão coerentes;
-   ações têm feedback;
-   não existe duplicação desnecessária.

------------------------------------------------------------------------

# 44. Critério de conclusão funcional

Quando houver implementação:

-   frontend compila;
-   backend responde;
-   endpoints estão integrados;
-   erros são tratados;
-   loading é tratado;
-   estado vazio é tratado;
-   permissões são tratadas;
-   autenticação é respeitada;
-   integração é testada;
-   fluxo principal funciona.

------------------------------------------------------------------------

# 45. Fonte de verdade

Quando houver conflito entre documentos:

1.  código atual deve ser verificado;
2.  imagens/mockups fornecidos devem ser usados para determinar
    aparência;
3.  documentação do projeto deve determinar arquitetura quando ainda
    válida;
4.  inventário serve para controle de cobertura;
5.  não assumir que um item antigo continua implementado;
6.  não criar funcionalidade apenas porque aparece no inventário.

------------------------------------------------------------------------

# 46. Estado atual do mapa

O CSV consolidado contém 567 itens e classifica o histórico disponível
em:

-   **77 itens identificados como gerados**
-   **490 itens não identificados como gerados**

Essa contagem é uma classificação documental do histórico disponível,
não uma auditoria automática do código-fonte.

Para uma auditoria definitiva de implementação, é necessário comparar o
mapa com o repositório atual.

------------------------------------------------------------------------

# 47. Próxima etapa recomendada

A próxima etapa do projeto é usar este documento + CSV como controle
mestre e, para cada tela ainda não produzida:

**mapa → referência visual → especificação → geração da imagem →
validação → implementação → teste → atualização do mapa.**

A geração das imagens deve continuar **uma por vez**, evitando
duplicações e preservando a ordem definida.

------------------------------------------------------------------------

# 48. Regra final

O FLOW AI deve ser tratado como um produto completo, não como uma
coleção de páginas isoladas.

Cada tela deve pertencer a:

-   um módulo;
-   um fluxo;
-   uma navegação;
-   um estado;
-   uma funcionalidade;
-   eventualmente um endpoint;
-   eventualmente uma integração.

O objetivo final é que qualquer novo agente consiga abrir esta
documentação e entender:

**o que existe, o que falta, onde está, como navega, quais componentes
utiliza, qual estado representa e o que precisa ser implementado.**
