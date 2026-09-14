# FLOW AI — META / FACEBOOK

## Escopo
Integrações com produtos Meta devem usar APIs e OAuth oficiais e somente permissões efetivamente aprovadas para o aplicativo.

## Configuração
```env
META_APP_ID=
META_APP_SECRET=
META_REDIRECT_URI=
META_VERIFY_TOKEN=
```

## OAuth
```text
authorize
→ callback
→ validar state
→ trocar código
→ armazenar credencial
→ criar Integration
```

## Segurança
- nunca expor App Secret;
- validar `state`;
- validar redirect URI;
- proteger tokens;
- revogar/desconectar corretamente.

## Webhooks
```text
POST /api/v1/webhooks/meta
```

Validar mecanismo de assinatura/verificação exigido pelo produto Meta.

## Produtos
Instagram, WhatsApp e Facebook podem possuir requisitos e permissões diferentes. Não assumir que uma credencial dá acesso a todos os produtos.

## Limitações
Permissões, revisão de app, quotas e capacidades devem ser confirmadas na documentação atual da Meta antes de implementação final.
