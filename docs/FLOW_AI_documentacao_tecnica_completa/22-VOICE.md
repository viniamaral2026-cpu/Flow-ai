# FLOW AI — VOICE

## Pipeline
```text
microfone
→ capture
→ speech-to-text
→ intent/context
→ FLOW agent
→ tool/action
→ text-to-speech
→ áudio
```

## Estados
- ouvindo;
- processando;
- respondendo;
- erro;
- offline;
- permissão negada.

## Wake Word
Wake word deve ser tratada como mecanismo de ativação, não como autorização para qualquer ação.

## Permissões
Microfone deve ser solicitado pelo cliente e refletido no backend somente quando necessário.

## Privacidade
Definir retenção de áudio, processamento transitório e controles do usuário.

## Segurança
Ações sensíveis exigem confirmação conforme política de autonomia.
