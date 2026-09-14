# FLOW AI — GOOGLE DRIVE API

## Recursos
- listar arquivos;
- buscar;
- metadados;
- download autorizado;
- upload;
- organização quando permitida.

## Endpoints internos
```http
GET  /api/v1/integrations/drive/files
GET  /api/v1/integrations/drive/files/{id}
POST /api/v1/integrations/drive/upload
```

## Segurança
Acesso deve respeitar scopes concedidos e permissões do próprio Drive.

## Arquivos
Validar tamanho, MIME type e política de conteúdo antes de processar.

## IA
Documentos enviados ao contexto da FLOW devem ser filtrados por autorização e relevância.

## Observação
Scopes e limites devem ser validados na documentação atual do Drive API.
