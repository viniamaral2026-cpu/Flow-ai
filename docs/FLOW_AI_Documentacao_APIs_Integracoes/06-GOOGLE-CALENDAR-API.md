# FLOW AI — GOOGLE CALENDAR API

## Recursos
- listar calendários;
- consultar eventos;
- criar eventos;
- atualizar;
- cancelar;
- disponibilidade quando suportada.

## Endpoints internos
```http
GET  /api/v1/calendar/calendars
GET  /api/v1/calendar/events
POST /api/v1/calendar/events
PATCH /api/v1/calendar/events/{id}
DELETE /api/v1/calendar/events/{id}
```

## AI tool
```json
{
  "name": "calendar_create_event",
  "risk": "medium",
  "requires_confirmation": true
}
```

## Timezone
Persistir timezone do evento/usuário conforme necessário. Não assumir UTC para apresentação.

## Idempotência
Criação acionada por agente deve aceitar idempotency key quando a operação puder ser repetida.

## Observação
Disponibilidade, scopes e formato final devem seguir a documentação vigente do Google Calendar API.
