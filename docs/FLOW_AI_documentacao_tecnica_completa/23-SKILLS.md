# FLOW AI — SKILLS

## Modelo
Uma Skill é uma capacidade extensível com manifesto e permissões.

## Manifesto
```json
{
  "name": "example",
  "version": "1.0.0",
  "description": "...",
  "permissions": [],
  "tools": []
}
```

## Lifecycle
Marketplace → instalação → permissões → execução → logs → atualização → publicação/despublicação.

## Segurança
Skills não devem obter acesso global por padrão.

## Sandbox
Código de terceiros deve ser isolado quando a arquitetura permitir.

## Review
Skills publicadas devem passar por validação automática e/ou revisão definida pelo produto.

## Versionamento
Mudanças incompatíveis exigem versão maior e migração documentada.
