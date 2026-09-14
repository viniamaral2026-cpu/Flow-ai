# FLOW AI — RUNBOOK

## API fora do ar
1. verificar health;
2. verificar Cloudflare;
3. verificar origem;
4. verificar logs;
5. verificar banco/Redis;
6. verificar deploy recente;
7. rollback se necessário.

## NVIDIA indisponível
1. verificar status/erro;
2. verificar timeout;
3. verificar quota/limite;
4. ativar fallback documentado se existir;
5. evitar retry agressivo.

## Firebase indisponível
Push pode ser atrasado. Registrar falhas e reprocessar de forma segura.

## Meta indisponível
Marcar integração como degradada sem apagar credenciais válidas.

## Banco indisponível
Não executar operações destrutivas. Preservar evidências e restaurar conectividade.

## Redis indisponível
Workers e cache podem degradar. Verificar filas e evitar perda de jobs críticos.

## Secret vazado
1. revogar imediatamente;
2. rotacionar;
3. identificar uso;
4. verificar logs;
5. remover do histórico quando possível;
6. registrar incidente.

## Deploy com erro
1. interromper promoção;
2. verificar health;
3. rollback;
4. preservar logs;
5. corrigir em branch;
6. novo deploy.

## Incidentes
Todo incidente relevante deve ter:
- horário;
- impacto;
- causa;
- mitigação;
- correção;
- prevenção.
