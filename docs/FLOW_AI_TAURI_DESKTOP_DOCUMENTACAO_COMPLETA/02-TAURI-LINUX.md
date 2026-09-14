# FLOW AI Desktop — Linux

## Objetivo
Distribuir o FLOW AI como aplicativo desktop Linux com integração nativa suficiente para uso diário.

## Distribuição
A release pode disponibilizar formatos apropriados à estratégia do projeto, como AppImage e pacotes de distribuição. Cada artefato deve ser testado na matriz oficial antes da publicação.

## Requisitos
Documentar por release:
- arquitetura CPU;
- distribuição suportada;
- versão mínima do sistema;
- dependências;
- WebView/WebKit necessário;
- permissões de áudio;
- espaço em disco.

## Inicialização
Se o usuário habilitar, o aplicativo pode iniciar com o sistema. Deve existir configuração explícita para ativar/desativar.

## Tray
O FLOW pode permanecer minimizado na bandeja quando suportado. O comportamento deve ser consistente e documentado.

## Áudio
Microfone deve ser solicitado pelo mecanismo de áudio do sistema. Falhas devem gerar mensagem clara e diagnóstico.

## Atualização
Atualizações devem ser assinadas e verificadas. Nunca substituir binário sem validação de integridade.

## Testes
Validar instalação, remoção, atualização, áudio, notificações, tray, atalhos, login, WebSocket, offline e recuperação.
