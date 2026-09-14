# Kotlin + Android Architecture
## Camadas
Presentation → Domain → Data → Infrastructure/Platform.

### Presentation
Compose, ViewModel, UI state, navigation e eventos.

### Domain
Use cases, entidades e regras que podem ser compartilhadas sem depender de Android.

### Data
Repositories, DTOs, mapeamento, cache e fontes remotas/locais.

### Platform
Microfone, notificações, câmera, armazenamento, WorkManager, Bluetooth e recursos Android.

## Estado
Usar estado imutável na UI e fluxo observável para dados assíncronos.

## Regra
Regra crítica de autorização e negócio deve ser validada no backend.
