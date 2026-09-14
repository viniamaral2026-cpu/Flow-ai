# FLOW AI — REGRAS MCP

## Objetivo
Definir uso seguro de ferramentas MCP.

## Classificação
### READ
Leitura de arquivos, código, logs e metadados.

### ANALYZE
Busca, comparação e inspeção.

### CREATE
Criação de arquivos, registros ou recursos.

### UPDATE
Alteração de recursos existentes.

### DELETE
Exclusão.

### EXECUTE
Execução de comandos/processos.

### DEPLOY
Mudança de ambiente.

### SECRET
Operações envolvendo credenciais.

## Princípio
Quanto maior o impacto, maior o nível de confirmação exigido.

## Regras
1. Descobrir a ferramenta antes de usar.
2. Ler schema/contrato.
3. Validar argumentos.
4. Restringir escopo.
5. Executar.
6. Verificar resultado.
7. Registrar efeito.

## Não fazer
Nunca tentar adivinhar parâmetros de ferramenta MCP.

## Produção
Operações destrutivas ou de deploy exigem autorização explícita quando não estiverem previamente autorizadas no escopo da tarefa.
