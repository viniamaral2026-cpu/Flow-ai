# FLOW AI — FRONTEND

## Arquitetura
O frontend deve consumir a API versionada e concentrar apenas apresentação, estado local e experiência do usuário.

## Camadas
```text
UI
 ↓
Feature components
 ↓
API client
 ↓
REST/WebSocket
```

## Regras
- nunca colocar secrets de servidor no bundle;
- centralizar cliente HTTP;
- tratar 401/403/404/409/422/429/5xx;
- usar estados loading, empty, error e success;
- evitar chamadas duplicadas;
- cancelar requests quando necessário;
- validar permissões antes de exibir ações sensíveis.

## Rotas
As rotas devem corresponder aos módulos documentados no mapa de telas.

## Responsividade
Desktop, tablet e mobile devem usar o mesmo sistema de design com adaptações de navegação.

## Autenticação
O frontend deve receber apenas tokens/cookies apropriados ao mecanismo escolhido e nunca credenciais administrativas.

## Realtime
Usar WebSocket somente quando o estado realmente exigir atualização em tempo real.

## Testes
Componentes críticos, fluxos de autenticação, chat, checkout e integrações devem possuir testes.
