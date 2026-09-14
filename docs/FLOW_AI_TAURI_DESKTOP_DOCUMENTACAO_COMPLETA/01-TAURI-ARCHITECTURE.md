# Tauri 2 — Arquitetura

## Camadas
1. React/TypeScript: telas, componentes, navegação e estado.
2. Tauri: janela, tray, notificações, atalhos, filesystem e APIs nativas autorizadas.
3. Rust: comandos nativos mínimos e seguros.
4. Backend: regras de negócio e dados persistentes do produto.

## Estrutura recomendada
```text
src/
  components/
  pages/
  routes/
  services/
  stores/
  hooks/
  types/
src-tauri/
  src/
  capabilities/
  icons/
  tauri.conf.json
```

## Regra
Não colocar regra de negócio crítica apenas no cliente. O backend deve validar autorização, identidade e operações sensíveis.

## IPC
Comandos Rust devem ter contratos explícitos, validação de entrada, erros tipados e menor privilégio. Evitar comandos genéricos que executem shell ou acesso irrestrito ao sistema.

## WebView
O frontend roda no WebView fornecido pela plataforma. Compatibilidade deve ser validada em cada release.

## Estado
Estado efêmero permanece no cliente. Dados de conta, memória, histórico e recursos sincronizados permanecem no backend, com cache local controlado.
