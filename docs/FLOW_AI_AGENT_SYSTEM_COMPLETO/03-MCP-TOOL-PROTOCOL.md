# FLOW AI — PROTOCOLO DE FERRAMENTAS MCP

## Antes
- identificar objetivo;
- identificar recurso;
- verificar permissão;
- verificar schema;
- avaliar risco.

## Durante
- enviar somente argumentos necessários;
- evitar dados sensíveis;
- respeitar timeout;
- não repetir operação sem verificar se a primeira ocorreu.

## Depois
- ler resposta;
- validar estado;
- confirmar recurso;
- registrar resultado.

## Idempotência
Para operações que podem ser repetidas, usar mecanismo de idempotência quando disponível.

## Erros
Não mascarar erro de ferramenta. Informar:
- ferramenta;
- operação;
- erro;
- impacto;
- próxima ação.

## Ferramentas desconhecidas
Se o schema não estiver disponível, não inventar a chamada.
