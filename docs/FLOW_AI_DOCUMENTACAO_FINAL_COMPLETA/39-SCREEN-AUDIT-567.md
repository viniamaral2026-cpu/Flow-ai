# FLOW AI — AUDITORIA DAS 567 TELAS

## Objetivo
Transformar o mapa de 567 telas em especificação implementável.

## Para cada tela registrar
```text
ID
Nome
Categoria
Rota
Shell
Permissão
Componentes
Estados
Endpoint
Entrada
Saída
Navegação
Mobile
Desktop
Acessibilidade
Status
```

## Estados obrigatórios
- loading;
- success;
- empty;
- error;
- disabled;
- permission denied;
- offline quando aplicável.

## Processo
1. localizar rota;
2. localizar componente;
3. localizar API;
4. comparar com imagem/mold;
5. validar design system;
6. validar responsividade;
7. marcar status;
8. eliminar duplicidade.

## Regra de fidelidade
Imagem de referência define intenção visual; código e design system definem implementação final.

## Regra de não duplicação
Antes de criar:
- buscar rota;
- buscar componente;
- buscar endpoint;
- buscar feature existente.

## Resultado
O mapa deve evoluir de inventário para matriz de implementação.
