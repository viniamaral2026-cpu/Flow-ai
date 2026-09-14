# Atualização Automática

## Objetivos
Manter o cliente seguro e atualizado sem quebrar instalações existentes.

## Processo
1. Verificar disponibilidade.
2. Validar versão.
3. Baixar artefato.
4. Validar assinatura/integridade.
5. Instalar.
6. Reiniciar quando necessário.
7. Confirmar versão.
8. Registrar resultado.

## Canais
Definir stable, beta e eventualmente nightly somente se houver processo de manutenção.

## Rollback
Uma atualização que impedir o boot deve ter estratégia documentada de recuperação.

## Segurança
Nunca executar atualização a partir de URL ou arquivo não confiável.
