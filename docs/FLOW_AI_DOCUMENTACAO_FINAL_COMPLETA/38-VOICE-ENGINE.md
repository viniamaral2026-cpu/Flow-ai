# FLOW AI — ENGINE DE VOZ

## Pipeline
```text
Microphone
→ Audio Capture
→ VAD/Wake Word
→ STT
→ Context
→ Agent
→ Tool
→ TTS
→ Audio Output
```

## Estados
`idle`, `listening`, `processing`, `speaking`, `error`, `permission_denied`, `offline`.

## Wake Word
Ativa o fluxo de voz, mas não equivale a autorização para ações sensíveis.

## STT
Entrada de áudio vira texto com metadados mínimos necessários.

## TTS
Resposta textual é convertida em áudio.

## Streaming
Quando suportado, respostas podem ser transmitidas progressivamente.

## Privacidade
Definir claramente:
- áudio transitório;
- retenção;
- armazenamento;
- exclusão;
- compartilhamento com providers.

## Segurança
Microfone exige permissão do sistema operacional/navegador.

## Ações
Operações sensíveis devem usar confirmação/autenticação conforme política de autonomia.
