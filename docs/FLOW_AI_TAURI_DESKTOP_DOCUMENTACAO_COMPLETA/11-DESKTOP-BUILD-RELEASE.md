# Build e Release

## Pipeline
```text
commit → lint → typecheck → testes → build → assinatura → artefatos → smoke test → publicação
```

## Versionamento
Adotar SemVer para releases públicas.

## Artefatos
Produzir artefatos por sistema/arquitetura e manter checksums.

## Ambientes
development, staging e production.

## Regra
Build de produção não deve depender de credenciais pessoais do desenvolvedor.

## Release notes
Toda versão deve registrar mudanças, correções, riscos conhecidos e requisitos.
