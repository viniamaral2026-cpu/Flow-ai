# Segurança Desktop

## Princípios
- menor privilégio;
- zero segredos no bundle;
- validação server-side;
- IPC mínimo;
- CSP adequada;
- dependências atualizadas;
- logs sem dados sensíveis.

## Token
Access/refresh tokens devem usar estratégia segura. Nunca registrar Authorization headers em logs.

## Tauri capabilities
Cada janela deve receber apenas capabilities necessárias. Evitar permissões amplas.

## Frontend
Tratar conteúdo remoto como não confiável. Sanitizar conteúdo renderizado e evitar execução dinâmica de código.

## Backend
Mesmo que o desktop esconda botões, o backend deve validar todas as operações.

## Supply chain
Fixar versões quando apropriado, revisar dependências, verificar advisories e assinar artefatos de release.
