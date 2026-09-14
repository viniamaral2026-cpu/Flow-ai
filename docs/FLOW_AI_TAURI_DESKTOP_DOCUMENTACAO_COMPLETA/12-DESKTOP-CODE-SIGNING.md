# Assinatura de Código

## Objetivo
Permitir que usuários e sistemas operacionais validem a origem e integridade dos executáveis.

## Linux
Manter checksums e assinatura dos artefatos conforme canal de distribuição.

## Windows
Usar assinatura Authenticode com certificado apropriado ao processo de distribuição.

## macOS
Usar assinatura Apple Developer e notarização quando exigida.

## CI
Chaves/certificados nunca devem ser commitados. Usar secrets do CI e acesso mínimo.

## Verificação
O pipeline deve falhar se a assinatura não puder ser produzida ou validada.
