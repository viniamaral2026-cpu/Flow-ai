# Guia de Desenvolvimento

## Ambiente
Stack: Swift + SwiftUI

Antes de iniciar, confirme versões oficiais do projeto no arquivo de configuração
real do repositório (por exemplo package.json, Gradle, Package.swift, Cargo.toml
ou requirements/pyproject). Não invente versões.

## Instalação
1. Clone o repositório.
2. Instale as dependências usando o gerenciador oficial do projeto.
3. Copie o arquivo de ambiente de exemplo, se existir.
4. Configure somente credenciais de desenvolvimento.
5. Execute os testes.
6. Inicie o modo de desenvolvimento.

## Configuração
Nunca coloque tokens reais no `.env` versionado. Use `.env.example` apenas com
nomes de variáveis e valores fictícios/seguros.

## Processo de mudança
LER → INSPECIONAR → LOCALIZAR → PLANEJAR → EXECUTAR → TESTAR → AUDITAR → DOCUMENTAR.

## Qualidade
Toda mudança deve considerar:
- funcionalidade;
- segurança;
- performance;
- acessibilidade quando aplicável;
- compatibilidade;
- observabilidade;
- documentação.

## Não fazer
- criar endpoint sem contrato;
- duplicar serviço;
- desabilitar segurança para “fazer funcionar”;
- commitar credenciais;
- declarar testes que não foram executados.
