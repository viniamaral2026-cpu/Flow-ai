# FLOW AI — APIS ADICIONAIS E ECOSSISTEMA

## Regra
Somente documentar como integração oficial aquilo que realmente será usado.

## Categorias possíveis
- Microsoft;
- Apple;
- clima;
- mapas/localização;
- IoT;
- armazenamento;
- pagamentos;
- comunicação;
- analytics.

## Microsoft
Possível arquitetura:
```text
Microsoft OAuth
→ adapter
→ Graph API
```
Pode abranger Outlook, Calendar e OneDrive conforme escopos.

## Apple
Integrações dependem do produto Apple específico e da plataforma cliente.

## Clima
```text
WeatherService
→ provider adapter
→ normalized weather model
```

## IoT
Dispositivos devem ser abstraídos por:
```text
Device
Room
Capability
Command
State
```

## Pagamentos
Sempre utilizar provider adapter e webhooks autenticados.

## Regra de provider
Nenhuma integração deve contaminar o domínio com objetos proprietários do fornecedor.
