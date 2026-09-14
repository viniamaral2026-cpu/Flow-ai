# Integração com o Sistema Operacional

## Recursos
Tray, notificações, atalhos globais, clipboard, abertura controlada de links, arquivos e inicialização.

## Princípio
Cada recurso nativo deve possuir uma capability explícita e o menor conjunto de permissões possível.

## Tray
Ações sugeridas:
- abrir FLOW;
- nova conversa;
- ativar/desativar voz;
- configurações;
- sair.

## Atalhos
Registrar somente atalhos necessários e detectar conflitos quando possível.

## Notificações
Não incluir conteúdo sensível em notificações sem que o usuário tenha autorizado esse comportamento.

## Arquivos
Acesso deve ser explícito e restrito a operações necessárias. Não conceder acesso global ao filesystem sem requisito.
