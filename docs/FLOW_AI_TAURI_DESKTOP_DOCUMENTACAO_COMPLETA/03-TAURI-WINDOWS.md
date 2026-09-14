# FLOW AI Desktop — Windows

## Plataformas
Windows 10/11 nas arquiteturas oficialmente suportadas pela release.

## Instalação
Usar instalador assinado e versionado. O instalador deve registrar corretamente atalhos, arquivos necessários e mecanismo de atualização.

## Integração
- bandeja do sistema;
- notificações;
- inicialização opcional;
- atalhos globais;
- microfone;
- câmera quando necessária;
- associação de links/protocolos somente se houver requisito aprovado.

## Armazenamento seguro
Credenciais e tokens não devem ser gravados em texto puro. Preferir mecanismos de proteção fornecidos pelo Windows através de biblioteca segura e abstração multiplataforma.

## Firewall/proxy
Erros de conectividade devem informar causa provável sem expor tokens ou dados internos.

## Atualização
Atualizações devem validar assinatura/integridade e permitir recuperação caso uma atualização falhe.

## Testes
Testar instalação limpa, atualização, desinstalação, múltiplas sessões, suspensão/retomada, notificações, áudio, rede e login expirado.
