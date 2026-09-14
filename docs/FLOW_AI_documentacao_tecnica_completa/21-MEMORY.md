# FLOW AI — MEMORY

## Tipos
- preferências;
- fatos fornecidos pelo usuário;
- contexto útil;
- instruções persistentes;
- memória de tarefas.

## Pipeline
```text
input
→ candidate memory
→ policy
→ save
→ index
→ retrieve
```

## Recuperação
Memórias devem ser filtradas por usuário, permissões e relevância.

## Controles
Usuário pode:
- visualizar;
- editar;
- excluir;
- pesquisar;
- exportar;
- importar quando suportado.

## Privacidade
Não armazenar informação além do necessário. Definir retenção e exclusão.

## Segurança
Isolamento por tenant/user obrigatório. Nunca permitir leitura de memória de outro usuário.
