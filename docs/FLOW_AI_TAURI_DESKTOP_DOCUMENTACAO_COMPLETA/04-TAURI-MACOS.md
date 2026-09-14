# FLOW AI Desktop — macOS

## Objetivo
Disponibilizar o mesmo produto desktop com comportamento nativo consistente no macOS.

## Distribuição
Gerar aplicativo e pacote de distribuição conforme a estratégia de release. Builds devem ser assinadas e notarizadas quando exigido pelo processo de distribuição.

## Permissões
Microfone, câmera, notificações e outros recursos devem seguir as permissões do macOS. O aplicativo deve explicar por que cada permissão é necessária.

## Segurança
Segredos nunca devem ser armazenados em arquivos de configuração do aplicativo. Usar armazenamento seguro do sistema por meio de abstração apropriada.

## Compatibilidade
Manter matriz por versão do macOS e arquitetura de CPU. Validar também WebView, áudio, atalhos, tray/menu bar e notificações.

## Atualização
Validar assinatura, integridade e rollback.
