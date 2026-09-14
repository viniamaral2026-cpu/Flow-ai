# FLOW AI — PAYMENTS

## Entidades
- Plan
- Subscription
- Payment
- Invoice
- PaymentMethod
- PaymentEvent

## Fluxo
```text
Plan
→ Checkout
→ Payment Provider
→ Webhook
→ Payment
→ Subscription
```

## Segurança
Dados completos de cartão não devem ser armazenados pelo FLOW se um PSP/tokenização puder ser usado.

## Idempotência
Checkout e webhooks devem ser idempotentes.

## Estados
- pending;
- approved;
- failed;
- refunded;
- canceled.

## Assinatura
Upgrade/downgrade/cancelamento devem gerar eventos auditáveis.

## Webhook
Validar autenticidade antes de alterar o estado financeiro.
