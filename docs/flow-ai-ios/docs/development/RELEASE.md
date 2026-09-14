# Release

## Fluxo
commit → lint → typecheck/build → testes → auditoria → artefato → publicação.

## Regras
- versionar de forma consistente;
- não publicar artefato não testado;
- registrar commit de origem;
- proteger credenciais de assinatura;
- preparar rollback;
- atualizar changelog/documentação.

## Pós-release
Executar smoke test e observar erros/telemetria.
