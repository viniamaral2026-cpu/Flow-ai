# Swift + SwiftUI Architecture
## Camadas
Presentation → Domain → Data → Platform.

### Presentation
SwiftUI Views, estado, navigation e view models/observable models.

### Domain
Entidades, casos de uso e regras independentes de UI.

### Data
Repositories, DTOs, API client, cache e sincronização.

### Platform
AVFoundation, UserNotifications, Photos/Camera, Keychain, BackgroundTasks e APIs Apple.

## Concorrência
Usar async/await e Actors quando necessário. Atualizações de UI devem respeitar o isolamento do MainActor.

## Regra
Regras críticas e autorização continuam no backend.
