from core.brain import think, think_stream, ver
from core import acoes, memoria
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from pathlib import Path
import base64, json, os, re, subprocess, sys, threading, time as _time, uuid
from datetime import datetime

BASE = Path(__file__).parent.resolve()
TASKS_FILE = BASE / "tasks.json"
SETTINGS_FILE = BASE / "settings.json"
LOG_FILE = BASE / "acoes.log"

app = FastAPI(title="FLOW Backend", version="3.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def _carregar_sys():
    try:
        with open(os.path.join(os.path.dirname(__file__), "flow_system_prompt.txt")) as f:
            return f.read()
    except Exception:
        return (
            "Você é a Flow, assistente pessoal do usuário em português brasileiro. "
            "Seja objetiva, carismática e direta. Se precisar executar algo no computador, "
            "responda com o comando dentro de um bloco ```bash ... ``` e explique em uma frase. "
            "Não invente fatos — se não souber, diga que não sabe. "
            "Se o usuário mandar uma imagem, analise e descreva o que vê."
        )


SYS = _carregar_sys()


def qlog(msg):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}\n")
    except Exception:
        pass


def carregar_json(p, default):
    try:
        with open(p) as f:
            return json.load(f)
    except Exception:
        return default


def salvar_json(p, data):
    with open(p, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_settings():
    s = carregar_json(SETTINGS_FILE, {})
    s.setdefault("model", "strong")
    s.setdefault("autonomy", True)
    return s


class ChatReq(BaseModel):
    messages: list[dict] | None = None
    prompt: str = ""
    task: str | None = None


class ExecReq(BaseModel):
    command: str
    timeout: int = 120


class TaskCreate(BaseModel):
    title: str
    command: str = ""
    intervalo: int = 0
    hora: str = ""
    active: bool = True


class TimerReq(BaseModel):
    nome: str = ""
    segundos: int = 0
    hora: str = ""
    alarme: bool = True


class RecipeReq(BaseModel):
    query: str


_W = None


def transcrever_arquivo(wav):
    global _W
    if _W is None:
        from faster_whisper import WhisperModel
        _W = WhisperModel("small", device="cpu", compute_type="int8")
    seg, _ = _W.transcribe(wav, language="pt", vad_filter=True)
    return " ".join(s.text.strip() for s in seg).strip()


def tts(texto, voz="pt-BR-FranciscaNeural"):
    out = "/tmp/flow_tts.mp3"
    subprocess.run(
        [sys.executable, "-m", "edge_tts", "--voice", voz, "--text", texto,
         "--write-media", out],
        capture_output=True, check=True, timeout=120,
    )
    return out


def _screen_size():
    import re
    try:
        out = subprocess.check_output(["sh", "-c", "xdpyinfo 2>/dev/null | grep dimensions"], timeout=10, text=True)
        m = re.search(r"(\d+)x(\d+)", out)
        if m:
            return int(m.group(1)), int(m.group(2))
    except Exception:
        pass
    return 1440, 900


def screenshot():
    out = "/tmp/flow_screen.png"
    w, h = _screen_size()
    disco = os.environ.get("DISPLAY", ":0")
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "x11grab",
         "-video_size", f"{w}x{h}", "-i", disco, "-vframes", "1", out],
        timeout=30,
    )
    if not os.path.exists(out):
        raise RuntimeError("falha ao capturar tela (DISPLAY?)")
    return out


def _executar_tarefa(t):
    cmd = t.get("command", "")
    if not cmd:
        return False, "sem comando"
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        ok = r.returncode == 0
        msg = (r.stdout.strip() or r.stderr.strip())[-2000:]
    except Exception as e:
        ok, msg = False, str(e)
    qlog(f"tarefa '{t.get('title')}': {'OK' if ok else 'ERRO'} | {msg[:120]}")
    return ok, msg


# ============================= Timers / alarmes =============================
_TIMERS = {}
_TIMERS_LOCK = threading.Lock()


def _entender_timer(texto):
    """Reconhece pedidos de timer/alarme no texto (PT-BR). Retorna (nome, segundos) ou None."""
    t = re.sub(r"[\.,;!\?]+$", "", (texto or "").strip().lower())
    if not t:
        return None
    m1 = re.search(r"^(?:timer|temporizador|cronometro|cronômetro|alarme|alarma|lembrete|aviso)\s+"
                   r"(\d+)\s*(horas?|h\b|min(?:uto)?s?|m\b|seg(?:undo)?s?|s\b)?\s*(.*)$", t)
    if m1:
        n, un, nome = int(m1.group(1)), (m1.group(2) or "min"), (m1.group(3) or "").strip()
        seg = _un_para_seg(n, un)
        return nome or "alarme", seg
    m2 = re.search(r"\b(?:me\s+)?(?:lembra|lembre|avisa)(?:\s+de|\s+pra)?\s+(.+?)\s+"
                   r"(?:em|daqui a|para\s+daqui a)\s+(\d+)\s*(horas?|h\b|min(?:uto)?s?|m\b|seg(?:undo)?s?|s\b)?\s*$", t)
    if m2:
        nome, n, un = m2.group(1).strip(), int(m2.group(2)), (m2.group(3) or "min")
        return nome, _un_para_seg(n, un)
    m3 = re.search(r"^\s*(?:alarme|me\s+acorde|acorde\s*-?me|acorda|acorde|acordar)\b(.*)$", t)
    if m3:
        resto = m3.group(1)
        mt = (re.search(r"(?:às?|as)\s*(\d{1,2})(?:[:h]\s*(\d{2}))?", resto)
              or re.search(r"(\d{1,2})[:h]\s*(\d{2})?\s*h?", resto))
        if not mt:
            m3 = None
        else:
            hh = int(mt.group(1))
            mm = int(mt.group(2) or 0)
            if hh > 23 or mm > 59:
                return None
            hora_txt = f"{hh}:{mm:02d}"
            nome = resto[mt.end():].strip().lstrip(".,:-").strip()
            nome = re.sub(r"^(para|de|pro|pra)\s+", "", nome).strip() or "alarme"
            seg = _hora_para_seg(hora_txt)
            qlog(f"timer hora: '{hora_txt}' nome '{nome}' seg {seg}")
            return nome, seg if seg else 60
    return None


_UN = {"h": 3600, "hora": 3600, "horas": 3600,
       "min": 60, "m": 60, "minuto": 60, "minutos": 60,
       "s": 1, "seg": 1, "segundo": 1, "segundos": 1}


def _un_para_seg(n, un):
    un = un.strip() or "min"
    return int(n) * _UN.get(un, 60)


def _hora_para_seg(hora):
    """'07', '7h', '07:30', '7:30' -> segundos até a próxima ocorrência."""
    m = re.search(r"(\d{1,2})[:hH]?(\d{2})?", hora)
    if not m:
        return None
    alvo_h, alvo_m = int(m.group(1)), int(m.group(2) or 0)
    if alvo_h > 23 or alvo_m > 59:
        return None
    agora = datetime.now()
    alvo = agora.replace(hour=alvo_h, minute=alvo_m, second=0, microsecond=0)
    if alvo <= agora:
        from datetime import timedelta
        alvo = (alvo + timedelta(days=1)).replace(hour=alvo_h,
                                                  minute=alvo_m, second=0, microsecond=0)
    return max(1, int((alvo - agora).total_seconds()))


def _timer_thread(tid):
    global _TIMERS
    while True:
        with _TIMERS_LOCK:
            if tid not in _TIMERS:
                return
            rest = _TIMERS[tid]["restantes"]
            if rest <= 0:
                info = _TIMERS.pop(tid)
                nome, alarma = info["nome"], info["alarme"]
                _notificar("⏰ Alarme da Flow", f"Timer '{nome}' terminou!")
                qlog(f"timer fim: {nome}")
                if alarma:
                    try:
                        subprocess.Popen(["ffplay", "-nodisp", "-loglevel", "quiet",
                                          "-autoexit", "/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga"])
                    except Exception:
                        pass
                return
        _time.sleep(1)
        with _TIMERS_LOCK:
            if tid in _TIMERS:
                _TIMERS[tid]["restantes"] -= 1


def _notificar(*a, **k):
    return acoes._notificar(*a, **k)


def criar_timer(nome, segundos, alarme=True):
    with _TIMERS_LOCK:
        tid = uuid.uuid4().hex[:8]
        _TIMERS[tid] = {"nome": nome, "segundos": max(1, int(segundos)),
                        "restantes": max(1, int(segundos)),
                        "fim": _time.time() + max(1, int(segundos)),
                        "alarme": alarme}
    threading.Thread(target=_timer_thread, args=(tid,), daemon=True).start()
    qlog(f"timer {nome} {segundos}s")
    return tid


def timers_lista():
    with _TIMERS_LOCK:
        return [{"id": tid, "nome": t["nome"], "segundos": t["segundos"],
                 "restantes": max(0, t["restantes"]),
                 "fim": t["fim"]} for tid, t in _TIMERS.items()]


def _loop_tarefas():
    while True:
        _time.sleep(10)
        if not get_settings().get("autonomy", True):
            continue
        tarefas = carregar_json(TASKS_FILE, [])
        agora = datetime.now()
        mudou = False
        for t in tarefas:
            if not t.get("active"):
                continue
            devido = False
            intervalo = int(t.get("intervalo") or 0)
            if intervalo and (_time.time() - int(t.get("last_run") or 0)) >= intervalo * 60:
                devido = True
            hora = (t.get("hora") or "").strip()
            if hora and agora.strftime("%H:%M") == hora and t.get("last_day") != agora.strftime("%Y-%m-%d"):
                devido = True
                t["last_day"] = agora.strftime("%Y-%m-%d")
            if devido:
                t["last_run"] = _time.time()
                ok, _ = _executar_tarefa(t)
                t["last_result"] = "OK" if ok else "ERRO"
                t["last_em"] = agora.strftime("%d/%m %H:%M")
                mudou = True
        if mudou:
            salvar_json(TASKS_FILE, tarefas)


@app.on_event("startup")
def _inicio():
    threading.Thread(target=_loop_tarefas, daemon=True).start()
    qlog("FLOW Backend iniciado v3.0.0")


def _par_linha(p):
    return {k: v for k, v in zip(["id", "titulo", "texto", "dist"], p)}


def _con_json(texto):
    """Extrai JSON da resposta do modelo (entre ```json ou puro)."""
    texto = (texto or "").strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", texto, re.S)
    if m:
        texto = m.group(1)
    else:
        texto = re.sub(r"^.*?(\[|\{)", r"\1", texto, flags=re.S)
    return json.loads(texto)


class ActReq(BaseModel):
    acao: str = "planejar"
    pergunta: str = ""
    url: str = ""
    texto: str = ""
    campo: str = ""
    tecla: str = ""
    seletor: str = ""
    x: int | None = None
    y: int | None = None
    duplo: bool = False


class MemLearn(BaseModel):
    texto: str
    fonte: str = "manual"
    importancia: float = 0.7


class MemSearch(BaseModel):
    pergunta: str
    k: int = 3


class MusicaReq(BaseModel):
    comando: str
    query: str = ""
    source: str = ""
    player: str = ""
    volume: int | None = None


class FocusReq(BaseModel):
    modo: str
    fechar: list[str] | None = None
    min_: int | None = None


@app.get("/api/health")
def health():
    return {"ok": True, "service": "FLOW Backend", "version": "3.0.0",
            "modelo": get_settings().get("model")}


def _msgs_base(prompt):
    fatos = memoria.buscar(prompt, k=3) if prompt else []
    ctx = ""
    if fatos:
        ctx = "\n\nMemórias que você lembra sobre o usuário (use quando relevante):\n- " + \
              "\n- ".join(f["texto"] for f in fatos)
    return [{"role": "system", "content": SYS + ctx}]


def _processar_intencao(texto):
    """Tenta resolver com integrações locais. Retorna (resposta or None)."""
    from core import integracoes as intg
    intent, t = intg.detectar_intencao(texto)
    if not intent:
        return None
    if intent == "clima":
        m = re.search(r"(?:em|pra|para|de)\s+((?:[A-Za-záéíóúâêôãõç -]{3,}))", t)
        cidade_ok = (m.group(1).strip() if m else "")[:40] or os.getenv("FLOW_CIDADE", "Taquara")
        return intg.clima_resumo(cidade_ok)
    if intent == "hora":
        return intg.data_hora_resumo()
    if intent == "sistema":
        return intg.sistema_resumo()
    if intent == "clipboard":
        if any(w in t for w in ["copiar", "cola", "copie"]):
            alvo = re.sub(r"^(?:me\s+)?(?:clipboard|copiar|copie|cola)\s*", "", t).strip()
            return intg.clipboard_escrever(alvo) if alvo else "Diga o que quer copiar."
        return f"Área de transferência: '{intg.clipboard_ler()[:120]}'"
    if intent == "brilho":
        m = re.search(r"(\d+)", t)
        return intg.brilho_resumo(int(m.group(1))) if m else intg.brilho_resumo()
    if intent == "compras":
        m_add = re.search(r"(?:adiciona|adicionar|coloca|comprar|acrescenta|inclui|anota)\\s+(.+)", t)
        if m_add:
            item = re.sub(r"\\s*(?:na|na lista|de compras|da lista|no mercado)$", "", m_add.group(1).strip())
            return intg.compras_adicionar(item or m_add.group(1).strip())
        m_rm = re.search(r"(?:remove|remover|tira|apagar|apaga)\s+(.+)", t)
        if m_rm:
            return intg.compras_remover(m_rm.group(1).strip())
        if any(w in t for w in ["limpar", "limpa", "zerar", "zera"]):
            return intg.compras_limpar()
        return intg.compras_resumo()
    if intent == "notas":
        m_add = re.search(r"(?:anotar|anota|nota|guardar|guardai|escreve)\s*(?:isso|isso aí|aí)?\s*(?:que|sobre)?\s*(.*)", t)
        if m_add and m_add.group(1).strip():
            return intg.notas_adicionar(m_add.group(1).strip())
        if any(w in t for w in ["concluir", "feita", "done", "pronto"]) or "nota " in t:
            m = re.search(r"(\d+)", t)
            if m:
                return intg.notas_concluir(int(m.group(1)))
        return intg.notas_resumo()
    if intent == "rotinas":
        m = re.search(r"(?:executa|execute|rodar|roda|ativa|ative|ativar)\s+(.+)", t)
        if m:
            nome = m.group(1).strip()
            r = intg.rotinas_executar(nome)
            if not r["ok"]:
                return f"Não achei a rotina '{nome}'. Crie no painel Rotinas."
            return "Rotina executada:\n- " + "\n- ".join(r["resultados"])
        if any(w in t for w in ["listar", "quais", "existem", "list"]):
            return intg.rotinas_resumo()
        return ("Rotinas disponíveis:\n" + intg.rotinas_resumo() +
                "\n\nFale 'execute NOME' ou use o painel Rotinas.")
    if intent == "whatsapp":
        m = re.search(r"(?:enviar|manda|mande|manda msg|enviar msg)\s+(?:uma\s+mensagem\s+)?para\s+([A-Za-z0-9 é]+?)\s*(?:dizendo|avisando|que|:)\s*(?:que\s+)?(.+)", t)
        if m:
            dest, msg = m.group(1).strip(), m.group(2).strip()
            r = intg.whatsapp_enviar(dest, msg)
            return r.get("msg", r.get("error", "Erro ao enviar."))
        m2 = re.search(r"(?:mensagem|msg)\s+pra\s+([A-Za-z0-9 é]+?)\s*[:]\s*(.+)", t)
        if m2:
            dest, msg = m2.group(1).strip(), m2.group(2).strip()
            r = intg.whatsapp_enviar(dest, msg)
            return r.get("msg", r.get("error", "Erro ao enviar."))
        r = intg.whatsapp_abrir()
        return r.get("msg", r.get("error", "Erro ao abrir WhatsApp."))
    if intent == "gmail":
        m = re.search(r"(?:ler|mostra|mostrar|resume|resumir|lê|lê o|ver|abre)\s+(?:meu)?\s*(?:gmail|email|emails|e-mails)?\s*(?:de|do|da|sobre)?\s*(.*)", t)
        query = m.group(1).strip() if m and m.group(1).strip() else "is:unread"
        r = intg.gmail_ler(query)
        if not r["ok"]:
            return f"Não consegui ler o Gmail: {r['error']}"
        if not r["emails"]:
            return "Nenhum email encontrado. Se não estiver logado no Gmail no navegador, ele não consegue ler."
        txt = "\n".join(f"• De {e['de']} — {e['assunto']}: {e['preview'][:60]}" for e in r["emails"])
        return f"Últimos {len(r['emails'])} emails:\n{txt}"
    if intent == "calendario":
        m = re.search(r"(\d+)", t)
        dias = int(m.group(1)) if m else 7
        r = intg.calendario_eventos(dias)
        if not r["ok"]:
            return f"Não consegui ler a agenda: {r['error']}"
        if not r["eventos"]:
            return "Nenhum compromisso encontrado nos próximos dias."
        txt = "\n".join(f"• {e['titulo']}" for e in r["eventos"])
        return f"Próximos compromissos:\n{txt}"
    return None


@app.post("/api/chat")
def chat(req: ChatReq):
    task = req.task or get_settings().get("model", "strong")
    local = _processar_intencao(req.prompt) if req.prompt else None
    if local:
        qlog(f"chat/local: {local[:100]}")
        return {"ok": True, "response": local, "integracao": True}
    timer = _entender_timer(req.prompt)
    if timer:
        nome, seg = timer
        criar_timer(nome, seg)
        min = seg // 60
        resp = (f"Timer '{nome}' criado! ⏰ Anota aí: {min} min e {seg % 60} s. "
                f"Eu te aviso quando terminar.")
        qlog(f"chat timer: {nome} {seg}s")
        return {"ok": True, "response": resp, "timer": True}
    if req.messages:
        msgs = [{"role": "system", "content": SYS}] + req.messages
    else:
        msgs = _msgs_base(req.prompt) + [{"role": "user", "content": req.prompt}]
    try:
        resp = think(msgs, task=task)
        qlog(f"chat({task}): {req.prompt[:120]}")
        return {"ok": True, "response": resp}
    except Exception as e:
        return {"ok": False, "error": str(e)[:400]}


@app.post("/api/chat/stream")
def chat_stream(req: ChatReq):
    task = req.task or get_settings().get("model", "strong")
    local = _processar_intencao(req.prompt) if req.prompt else None
    if local:
        qlog(f"chat/stream/local: {local[:100]}")

        def gen_local():
            for pal in local.split():
                yield f"data: {json.dumps({'token': pal + ' '}, ensure_ascii=False)}\n\n"
            yield "data: [DONE]\n\n"
        return StreamingResponse(gen_local(), media_type="text/event-stream",
                                 headers={"Cache-Control": "no-cache",
                                          "Connection": "keep-alive"})
    timer = _entender_timer(req.prompt)
    if timer:
        nome, seg = timer
        criar_timer(nome, seg)
        text = (f"Timer '{nome}' criado! ⏰ Anota aí: {seg // 60} min e {seg % 60} s. "
                f"Eu te aviso quando terminar.")
        qlog(f"chat/stream timer: {nome} {seg}s")

        def gen_timer():
            for pal in text.split():
                yield f"data: {json.dumps({'token': pal + ' '}, ensure_ascii=False)}\n\n"
            yield "data: [DONE]\n\n"
        return StreamingResponse(gen_timer(), media_type="text/event-stream",
                                 headers={"Cache-Control": "no-cache",
                                          "Connection": "keep-alive"})
    if req.messages:
        msgs = [{"role": "system", "content": SYS}] + req.messages
    else:
        msgs = _msgs_base(req.prompt) + [{"role": "user", "content": req.prompt}]

    def gen():
        try:
            for token in think_stream(msgs, task=task):
                yield f"data: {json.dumps({'token': token}, ensure_ascii=False)}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'erro': str(e)[:300]}, ensure_ascii=False)}\n\n"
        yield "data: [DONE]\n\n"

    qlog(f"chat/stream({task}): {req.prompt[:120]}")
    return StreamingResponse(
        gen(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )


@app.post("/api/execute")
def execute(req: ExecReq):
    cmd = req.command.strip()
    if not cmd:
        return {"ok": False, "error": "comando vazio"}
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                           timeout=req.timeout)
        qlog(f"execute: $ {cmd[:160]} -> exit {p.returncode}")
        return {"ok": p.returncode == 0, "code": p.returncode,
                "stdout": p.stdout[-4000:], "stderr": p.stderr[-4000:]}
    except subprocess.TimeoutExpired:
        qlog(f"execute timeout: $ {cmd[:160]}")
        return {"ok": False, "error": f"timeout após {req.timeout}s"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


@app.post("/api/listen")
async def listen(audio: UploadFile = File(...)):
    src = "/tmp/flow_audio_in.webm"
    with open(src, "wb") as f:
        f.write(await audio.read())
    wav = "/tmp/flow_audio_in.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src,
                    "-ar", "16000", "-ac", "1", wav], check=True, timeout=60)
    texto = transcrever_arquivo(wav)
    qlog(f"listen: '{texto[:120]}'")
    return {"text": texto}


@app.get("/api/tts")
def tts_endpoint(text: str, voz: str = "pt-BR-FranciscaNeural"):
    try:
        arq = tts(text[:2000], voz)
        return FileResponse(arq, media_type="audio/mpeg")
    except Exception as e:
        return JSONResponse({"ok": False, "error": str(e)}, status_code=500)


@app.get("/api/vision")
def vision(pergunta: str = "Descreva o que está na tela do computador do usuário."):
    try:
        arq = screenshot()
        with open(arq, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        descricao = ver(b64, pergunta)
        qlog(f"vision: {descricao[:120]}")
        return {"ok": True, "imagem": "data:image/png;base64," + b64,
                "descricao": descricao}
    except Exception as e:
        return {"ok": False, "error": str(e)[:400]}


@app.post("/api/vision/act")
def vision_act(req: ActReq):
    """Ver a tela e agir: planeja (com vision) e executa no Playwright."""
    try:
        if req.acao == "planejar" and not req.pergunta:
            return {"ok": False, "error": "pergunta vazia"}
        if req.acao in ("clicar_em", "mover", "digitar_tela", "tecla_tela"):
            if req.acao == "clicar_em":
                acoes.clicar(req.x or 0, req.y or 0, req.duplo)
                msg = f"clicou em ({req.x}, {req.y})"
            elif req.acao == "mover":
                acoes.mover_mouse(req.x or 0, req.y or 0)
                msg = f"mouse em ({req.x}, {req.y})"
            elif req.acao == "digitar_tela":
                acoes.digitar(req.texto)
                msg = f"digitou na tela: {req.texto[:40]}"
            else:
                acoes.tecla(req.tecla or "Return")
                msg = f"apertou {req.tecla}"
            qlog("vision/act " + msg)
            return {"ok": True, "mensagem": msg}

        if req.acao == "direct":
            plano = [p for p in [
                {"acao": "abrir", "url": req.url} if req.url else None,
                {"acao": "clicar", "texto": req.texto} if req.texto else None,
                {"acao": "digitar", "campo": req.campo, "texto": req.texto} if req.campo and req.texto else None,
            ] if p]
            if not plano:
                return {"ok": False, "error": "nada a fazer (url/texto/campo)"}
            res = acoes.pw_exec(plano)
            qlog("vision/act direct: " + "; ".join(res.get("passos", []))[:160])
            return {"ok": True, **res}

        arq = screenshot()
        with open(arq, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        prompt = (
            "Analise o screenshot do desktop do usuário e o pedido: "
            f"'{req.pergunta}'. "
            "Retorne APENAS um JSON com uma lista de ações Playwright para cumprir o pedido, "
            "ex: [{\"acao\":\"abrir\",\"url\":\"https://...\"},\n"
            "{\"acao\":\"clicar\",\"texto\":\"Pagar\"},\n"
            "{\"acao\":\"digitar\",\"campo\":\"placeholder ou rótulo do campo\",\"texto\":\"valor\"},\n"
            "{\"acao\":\"tecla\",\"tecla\":\"Enter\"}] "
            "Ações válidas: abrir(url) | clicar(texto) | clicar_seletor(seletor) | "
            "digitar(campo,texto) | tecla(tecla) | esperar(seg). "
            "Se o pedido for apenas descritivo, retorne {\"descricao\":\"...\"}. "
            "Sem texto fora do JSON."
        )
        for tent in range(2):
            try:
                plano = _con_json(ver(b64, prompt))
                break
            except Exception:
                plano = None
                qlog(f"vision/act: plano inválido (tentativa {tent + 1})")
        if not plano or isinstance(plano, dict):
            desc = plano.get("descricao") if isinstance(plano, dict) else ""
            return {"ok": True, "resposta": desc or "Não consegui montar um plano para isso.",
                    "plano": plano}
        res = acoes.pw_exec(plano)
        qlog("vision/act: " + "; ".join(res.get("passos", []))[:160])
        return {"ok": True, **res, "plano": plano}
    except Exception as e:
        return {"ok": False, "error": str(e)[:500]}


@app.post("/api/memory/learn")
def memory_learn(req: MemLearn):
    try:
        did = memoria.aprender(req.texto, fonte=req.fonte, importancia=req.importancia)
        if not did:
            return {"ok": False, "error": "falha ao gerar embedding"}
        qlog(f"memoria/learn: {req.texto[:80]}")
        return {"ok": True, "id": did}
    except Exception as e:
        return {"ok": False, "error": str(e)[:400]}


@app.post("/api/memory/search")
def memory_search(req: MemSearch):
    try:
        res = memoria.buscar(req.pergunta, k=req.k)
        return {"ok": True, "resultados": res}
    except Exception as e:
        return {"ok": False, "error": str(e)[:400]}


@app.post("/api/musica")
def musica(req: MusicaReq):
    try:
        out = acoes.musica(req.comando, req.query, req.source, req.player, req.volume)
        if isinstance(out, tuple):
            _, query, source, player = out
            if not query:
                return {"ok": False, "error": "faltou o nome da música/playlist"}
            res = acoes.pw_exec([{"acao": "abrir",
                                  "url": f"https://music.youtube.com/search?q={query.replace(' ', '+')}"}])
            acoes.pw_exec([{"acao": "clicar_seletor", "seletor": "ytmusic-play-button-renderer"}])
            qlog(f"musica: tocar '{query}' no YouTube")
            return {"ok": True,
                    "mensagem": f"Tocando '{query}' no YouTube Music 🎧",
                    "detalhe": res}
        qlog(f"musica: {req.comando} {req.query[:60]}")
        if isinstance(out, dict):
            return {"ok": True, **out}
        return {"ok": True, "mensagem": out}
    except Exception as e:
        return {"ok": False, "error": str(e)[:400]}


@app.get("/api/musica/players")
def musica_players():
    return {"players": acoes._players()}


@app.get("/api/musica/sons")
def musica_sons():
    return {"sons": acoes.sons_disponiveis()}


@app.post("/api/system/focus")
def focus(req: FocusReq):
    try:
        r = acoes.modo_foco(req.modo, req.fechar, req.min_)
        qlog(f"focus: {req.modo} {r}")
        return {"ok": True, **r}
    except Exception as e:
        return {"ok": False, "error": str(e)[:400]}


@app.get("/api/system/focus/status")
def focus_status():
    return {"ok": True, **acoes.modo_foco("status")}


@app.get("/api/tasks")
def tasks_lista():
    return {"tasks": carregar_json(TASKS_FILE, [])}


@app.post("/api/tasks")
def tasks_criar(t: TaskCreate):
    tarefas = carregar_json(TASKS_FILE, [])
    nova = {
        "id": uuid.uuid4().hex[:8],
        "title": t.title,
        "command": t.command,
        "intervalo": t.intervalo,
        "hora": t.hora,
        "active": t.active,
        "last_result": "nunca",
        "last_em": "-",
        "last_run": 0,
        "last_day": "",
    }
    tarefas.append(nova)
    salvar_json(TASKS_FILE, tarefas)
    qlog(f"rotina criada: {t.title}")
    return {"ok": True, "task": nova}


@app.post("/api/tasks/{tid}/toggle")
def tasks_toggle(tid: str):
    tarefas = carregar_json(TASKS_FILE, [])
    for t in tarefas:
        if t.get("id") == tid:
            t["active"] = not t.get("active", True)
            break
    salvar_json(TASKS_FILE, tarefas)
    return {"ok": True}


@app.post("/api/tasks/{tid}/run")
def tasks_run(tid: str):
    tarefas = carregar_json(TASKS_FILE, [])
    for t in tarefas:
        if t.get("id") == tid:
            ok, msg = _executar_tarefa(t)
            t["last_result"] = "OK" if ok else "ERRO"
            t["last_em"] = datetime.now().strftime("%d/%m %H:%M")
            t["last_run"] = _time.time()
            salvar_json(TASKS_FILE, tarefas)
            return {"ok": True, "resultado": "OK" if ok else "ERRO", "detalhe": msg}
    return {"ok": False, "error": "rotina não encontrada"}


@app.delete("/api/tasks/{tid}")
def tasks_remover(tid: str):
    tarefas = carregar_json(TASKS_FILE, [])
    tarefas = [t for t in tarefas if t.get("id") != tid]
    salvar_json(TASKS_FILE, tarefas)
    return {"ok": True}


@app.get("/api/musica/agora")
def musica_agora():
    return {"ok": True, **acoes.agora_tocando()}


@app.get("/api/musica/local")
def musica_local(pasta: str = ""):
    return {"ok": True, **acoes.listar_locais(pasta)}


@app.get("/api/timer")
def timers_get():
    return {"ok": True, "timers": timers_lista()}


@app.post("/api/timer")
def timers_criar(t: TimerReq):
    seg = t.segundos if t.segundos else (_hora_para_seg(t.hora) or 0)
    if seg <= 0:
        return {"ok": False, "error": "informe segundos ou hora (ex: 30 ou 07:30)"}
    tid = criar_timer(t.nome or "alarme", seg, t.alarme)
    return {"ok": True, "tid": tid, "segundos": seg, "timers": timers_lista()}


@app.post("/api/timer/{tid}/cancel")
def timers_cancelar(tid: str):
    with _TIMERS_LOCK:
        if tid in _TIMERS:
            del _TIMERS[tid]
            return {"ok": True}
    return {"ok": False, "error": "timer não encontrado"}


@app.post("/api/receita/buscar")
def receita_buscar(r: RecipeReq):
    if not r.query.strip():
        return {"ok": False, "error": "busca vazia"}
    qlog(f"receita: buscar '{r.query}'")
    try:
        res = acoes.buscar_receitas(r.query)
        return {"ok": True, "query": r.query, "resultados": res}
    except Exception as e:
        return {"ok": False, "error": str(e)[:400]}


@app.get("/api/logs")
def logs():
    try:
        with open(LOG_FILE) as f:
            linhas = f.read().splitlines()
        return {"logs": linhas[-40:]}
    except Exception:
        return {"logs": []}


@app.get("/api/settings")
def settings_get():
    return {"ok": True, **get_settings()}


@app.post("/api/settings")
def settings_set(req: dict):
    s = get_settings()
    for k in ("model", "autonomy"):
        if k in req:
            s[k] = req[k]
    salvar_json(SETTINGS_FILE, s)
    qlog(f"config: {s}")
    return {"ok": True, **s}


# ============================= Integrações =============================
class ClimaReq(BaseModel):
    cidade: str = "Taquara"


class ComprasReq(BaseModel):
    acao: str = "listar"
    item: str = ""


class NotaReq(BaseModel):
    acao: str = "listar"
    texto: str = ""
    tipo: str = "nota"
    id: int | None = None


class RotinaReq(BaseModel):
    acao: str
    nome: str = ""
    passos: list[dict] = []


class WhatsAppReq(BaseModel):
    destinatario: str
    mensagem: str = ""


class GmailReq(BaseModel):
    query: str = "is:unread"
    max: int = 5


class BrilhoReq(BaseModel):
    nivel: int | None = None


class ClipboardReq(BaseModel):
    escrever: str | None = None


@app.get("/api/integracoes/clima")
@app.post("/api/integracoes/clima")
def integ_clima(cidade: str = "Taquara", req: ClimaReq | None = None):
    from core import integracoes as intg
    if req:
        cidade = req.cidade
    qlog(f"integracoes/clima: {cidade}")
    return intg.clima(cidade)


@app.get("/api/integracoes/sistema")
def integ_sistema():
    from core import integracoes as intg
    return intg.sistema_info()


@app.get("/api/integracoes/datahora")
def integ_datahora():
    from core import integracoes as intg
    return intg.data_hora()


@app.get("/api/integracoes/clipboard")
@app.post("/api/integracoes/clipboard")
def integ_clipboard(req: ClipboardReq | None = None):
    from core import integracoes as intg
    if req and req.escrever:
        return intg.clipboard_escrever(req.escrever)
    return {"ok": True, "conteudo": intg.clipboard_ler()}


@app.post("/api/integracoes/brilho")
def integ_brilho(req: BrilhoReq):
    from core import integracoes as intg
    return intg.brilho(req.nivel)


@app.get("/api/integracoes/brilho")
def integ_brilho_get():
    from core import integracoes as intg
    return intg.brilho(None)


@app.get("/api/integracoes/compras")
@app.post("/api/integracoes/compras")
def integ_compras(req: ComprasReq | None = None):
    from core import integracoes as intg
    acao = req.acao if req else "listar"
    item = req.item if req else ""
    if acao == "adicionar":
        return {"ok": True, "mensagem": intg.compras_adicionar(item)}
    if acao == "remover":
        return {"ok": True, "mensagem": intg.compras_remover(item)}
    if acao == "limpar":
        return {"ok": True, "mensagem": intg.compras_limpar()}
    return {"ok": True, "items": intg.compras_listar()}


@app.get("/api/integracoes/notas")
@app.post("/api/integracoes/notas")
def integ_notas(req: NotaReq | None = None):
    from core import integracoes as intg
    acao = req.acao if req else "listar"
    if acao == "adicionar":
        return {"ok": True, "mensagem": intg.notas_adicionar(req.texto, req.tipo)}
    if acao == "concluir" and req.id:
        return {"ok": True, "mensagem": intg.notas_concluir(req.id)}
    return {"ok": True, "notas": intg.notas_listar()}


@app.get("/api/integracoes/rotinas")
@app.post("/api/integracoes/rotinas")
def integ_rotinas(req: RotinaReq | None = None):
    from core import integracoes as intg
    acao = req.acao if req else "listar"
    if acao == "criar":
        r = intg.rotinas_criar(req.nome, req.passos)
        return r
    if acao == "executar":
        return intg.rotinas_executar(req.nome)
    return {"ok": True, "rotinas": intg.rotinas_listar()}


@app.delete("/api/integracoes/rotinas/{nome}")
def integ_rotinas_remover(nome: str):
    from core import integracoes as intg
    rotinas = [r for r in intg.rotinas_listar() if r["nome"].lower() != nome.lower()]
    _salvar_json = lambda p, d: intg._json_save(p, d)
    _salvar_json(intg.ROTINAS_FILE, rotinas)
    return {"ok": True}


@app.post("/api/integracoes/whatsapp")
def integ_whatsapp(req: WhatsAppReq):
    from core import integracoes as intg
    r = intg.whatsapp_enviar(req.destinatario, req.mensagem)
    return r


@app.post("/api/integracoes/whatsapp/abrir")
def integ_whatsapp_abrir():
    from core import integracoes as intg
    return intg.whatsapp_abrir()


@app.post("/api/integracoes/gmail")
def integ_gmail(req: GmailReq):
    from core import integracoes as intg
    return intg.gmail_ler(req.query, req.max)


@app.post("/api/integracoes/gmail/abrir")
def integ_gmail_abrir():
    from core import integracoes as intg
    return intg.gmail_abrir()


@app.post("/api/integracoes/calendario")
def integ_calendario():
    from core import integracoes as intg
    return intg.calendario_eventos()


@app.post("/api/integracoes/calendario/abrir")
def integ_calendario_abrir():
    from core import integracoes as intg
    return intg.calendario_abrir()