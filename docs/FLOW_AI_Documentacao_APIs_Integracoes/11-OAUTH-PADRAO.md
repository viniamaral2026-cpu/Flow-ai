# FLOW AI — PADRÃO OAUTH

## Fluxo
```text
1. usuário escolhe integração
2. backend gera state/PKCE quando aplicável
3. usuário autoriza no provider
4. provider retorna callback
5. backend valida state
6. troca código por token
7. valida identidade
8. criptografa credenciais
9. salva Integration
10. redireciona para sucesso
```

## Segurança
Nunca aceitar callback sem validação de state.

## PKCE
Usar quando recomendado/suportado pelo fluxo.

## Redirect
Cada ambiente possui URI registrada e exata.

## Token lifecycle
- issued;
- active;
- refreshed;
- expired;
- revoked.

## Desconexão
Revogar credencial no provider quando suportado e remover/invalidar a credencial interna.

## Auditoria
Registrar conexão/desconexão, provider, usuário e status sem registrar token.
