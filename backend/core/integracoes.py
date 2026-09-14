"""Integrações locais da Flow — clima, sistema, compras, rotinas, WhatsApp/Gmail/Calendar via Playwright."""
import json, os, re, subprocess, threading, time as _time
from datetime import datetime, timedelta
from pathlib import Path

BASE = Path(__file__).parent.parent.resolve()
WORKDIR = BASE
COMPRAS_FILE = WORKDIR / "compras.json"
NOTAS_FILE = WORKDIR / "notas.json"
ROTINAS_FILE = WORKDIR / "rotinas.json"

def _run(cmd, timeout=30):
    try:
        r = subprocess.run(cmd, shell=isinstance(cmd, str), capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip()
    except Exception:
        return ""

def _json_load(p, default):
    try:
        with open(p) as f: return json.load(f)
    except: return default

def _json_save(p, data):
    with open(p, "w") as f: json.dump(data, f, ensure_ascii=False, indent=2)

# ============================= Clima (wttr.in) =============================
def clima(cidade="Taquara"):
    import urllib.request
    try:
        url = f"https://wttr.in/{cidade.replace(' ','+')}?format=j1&lang=pt"
        req = urllib.request.Request(url, headers={"User-Agent": "curl/7.88"})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read().decode())
        cc = d["current_condition"][0]
        hoje = d["weather"][0]
        return {
            "ok": True, "cidade": cidade,
            "atual": {
                "temp": cc["temp_C"],
                "sensacao": cc["FeelsLikeC"],
                "umidade": cc["humidity"],
                "vento": cc["windspeedKmph"],
                "desc": cc["lang_pt"][0]["value"] if cc.get("lang_pt") else cc["weatherDesc"][0]["value"],
                "chuva_mm": cc.get("precipMM", "0"),
            },
            "hoje": {
                "max": hoje["maxtempC"], "min": hoje["mintempC"],
                "nascer": hoje["astronomy"][0]["sunrise"],
                "por": hoje["astronomy"][0]["sunset"],
            },
            "previsao": [
                {"dia": w["date"], "max": w["maxtempC"], "min": w["mintempC"],
                 "desc": w["hourly"][4]["lang_pt"][0]["value"] if w["hourly"][4].get("lang_pt") else w["hourly"][4]["weatherDesc"][0]["value"]}
                for w in d.get("weather", [])[:3]
            ]
        }
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}


def clima_resumo(cidade="Taquara"):
    c = clima(cidade)
    if not c["ok"]:
        return f"Não consegui pegar o clima de {cidade}."
    a = c["atual"]
    h = c["hoje"]
    return (f"Clima em {cidade}: {a['desc']}, {a['temp']}°C (sensação {a['sensacao']}°C), "
            f"umidade {a['umidade']}%, vento {a['vento']}km/h. "
            f"Máx {h['max']}°Mín {h['min']}°. "
            f"Nascer do sol: {h['nascer']}, pôr: {h['por']}.")

# ============================= Data/Hora =============================
def data_hora():
    agora = datetime.now()
    dias = ["segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sábado","domingo"]
    meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    return {
        "hora": agora.strftime("%H:%M"),
        "data": agora.strftime("%d/%m/%Y"),
        "dia_semana": dias[agora.weekday()],
        "mes": meses[agora.month - 1],
        "timestamp": int(agora.timestamp()),
        "unix": int(agora.timestamp()),
    }


def data_hora_resumo():
    d = data_hora()
    return f"Agora são {d['hora']}, {d['dia_semana']}, {d['data']} ({d['mes']})."

# ============================= Sistema =============================
def sistema_info():
    disk = _run("df -h / | tail -1 | awk '{print $2,$3,$4,$5}'")
    mem = _run("free -h | awk '/^Mem/{print $2,$3,$4,$7}'")
    cpu = _run("grep -c ^processor /proc/cpuinfo")
    load = _run("cat /proc/loadavg | awk '{print $1,$2,$3}'")
    uptime = _run("uptime -p")
    temp = _run("cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null")
    temp_c = f"{int(temp)/1000:.1f}°C" if temp.isdigit() else "N/A"
    return {
        "ok": True,
        "disco": {"total": disk.split()[0] if disk else "?", "usado": disk.split()[1] if disk else "?",
                  "livre": disk.split()[2] if disk else "?", "uso_pct": disk.split()[3] if disk else "?"},
        "ram": {"total": mem.split()[0] if mem else "?", "usado": mem.split()[1] if mem else "?",
                "livre": mem.split()[2] if mem else "?", "disponivel": mem.split()[3] if mem else "?"},
        "cpu": {"nucleos": cpu, "load_1m": load.split()[0] if load else "?",
                "load_5m": load.split()[1] if load else "?", "temp": temp_c},
        "uptime": uptime,
    }


def sistema_resumo():
    s = sistema_info()
    return (f"Sistema: disco {s['disco']['uso_pct']} usado ({s['disco']['livre']} livre), "
            f"RAM {s['ram']['usado']}/{s['ram']['total']}, "
            f"CPU {s['cpu']['nucleos']} núcleos, carga {s['cpu']['load_1m']}, "
            f"temp {s['cpu']['temp']}. Up {s['uptime']}.")

# ============================= Clipboard =============================
def clipboard_ler():
    return _run("xclip -selection clipboard -o 2>/dev/null") or _run("xsel --clipboard --output 2>/dev/null")

def clipboard_escrever(texto):
    p = subprocess.Popen(["xclip", "-selection", "clipboard"], stdin=subprocess.PIPE)
    p.communicate(texto.encode())
    return f"Copiado para a área de transferência: {texto[:80]}"

# ============================= Brilho =============================
def brilho(nivel=None):
    out = _run("xrandr --verbose 2>/dev/null | grep -i brightness | head -1 | awk '{print $2}'")
    atual = float(out) if out else 1.0
    if nivel is None:
        return {"ok": True, "atual": round(atual * 100), "raw": atual}
    lvl = max(0.1, min(1.0, float(nivel) / 100.0))
    output = _run("xrandr | grep ' connected' | head -1 | awk '{print $1}'")
    if output:
        subprocess.run(["xrandr", "--output", output, "--brightness", str(lvl)], capture_output=True)
    return {"ok": True, "anterior": round(atual * 100), "atual": round(lvl * 100)}


def brilho_resumo(nivel=None):
    r = brilho(nivel)
    if nivel is not None:
        return f"Brilho ajustado para {r['atual']}% (era {r['anterior']}%)."
    return f"Brilho atual: {r['atual']}%."

# ============================= Lista de Compras =============================
def compras_listar():
    return _json_load(COMPRAS_FILE, [])

def compras_adicionar(item, qtd=1):
    items = compras_listar()
    existe = next((i for i in items if i["item"].lower() == item.lower()), None)
    if existe:
        existe["qtd"] += qtd
    else:
        items.append({"item": item, "qtd": qtd, "added": datetime.now().strftime("%d/%m %H:%M")})
    _json_save(COMPRAS_FILE, items)
    return f"Adicionado: {item} x{qtd}. Total na lista: {len(items)} itens."

def compras_remover(item):
    items = compras_listar()
    antes = len(items)
    items = [i for i in items if i["item"].lower() != item.lower()]
    if len(items) < antes:
        _json_save(COMPRAS_FILE, items)
        return f"Removido: {item}. Restam {len(items)} itens."
    return f"'{item}' não encontrado na lista."

def compras_limpar():
    _json_save(COMPRAS_FILE, [])
    return "Lista de compras limpa."

def compras_resumo():
    items = compras_listar()
    if not items:
        return "Lista de compras vazia."
    lista = ", ".join(f"{i['item']} x{i['qtd']}" for i in items)
    return f"Lista de compras ({len(items)} itens): {lista}."

# ============================= Notas / Lembretes =============================
def notas_listar():
    return _json_load(NOTAS_FILE, [])

def notas_adicionar(texto, tipo="nota"):
    notas = notas_listar()
    nota = {"id": len(notas) + 1, "texto": texto, "tipo": tipo,
            "criado": datetime.now().isoformat(), "feito": False}
    notas.append(nota)
    _json_save(NOTAS_FILE, notas)
    return f"Nota #{nota['id']} criada: {texto[:60]}"

def notas_concluir(nid):
    notas = notas_listar()
    for n in notas:
        if n["id"] == nid:
            n["feito"] = True
            _json_save(NOTAS_FILE, notas)
            return f"Nota #{nid} marcada como feita."
    return f"Nota #{nid} não encontrada."

def notas_resumo():
    notas = [n for n in notas_listar() if not n.get("feito")]
    if not notas:
        return "Sem notas pendentes."
    txt = "\n".join(f"#{n['id']}: {n['texto'][:60]}" for n in notas[:5])
    return f"Notas pendentes ({len(notas)}):\n{txt}"

# ============================= Rotinas Multi-Step =============================
def rotinas_listar():
    return _json_load(ROTINAS_FILE, [])

def rotinas_criar(nome, passos):
    rotinas = rotinas_listar()
    rotina = {"id": len(rotinas) + 1, "nome": nome, "passos": passos,
              "criado": datetime.now().isoformat(), "ativa": True}
    rotinas.append(rotina)
    _json_save(ROTINAS_FILE, rotinas)
    return {"ok": True, "rotina": rotina}

def rotinas_executar(nome):
    rotinas = rotinas_listar()
    r = next((x for x in rotinas if x["nome"].lower() == nome.lower()), None)
    if not r:
        return {"ok": False, "error": f"Rotina '{nome}' não encontrada."}
    resultados = []
    for passo in r["passos"]:
        tipo = passo.get("tipo", "")
        acao = passo.get("acao", "")
        try:
            if tipo == "musica":
                from core import acoes
                out = acoes.musica(acao, passo.get("query", ""), passo.get("source", ""))
                resultados.append(f"Música: {acao} → {out.get('msg', out) if isinstance(out, dict) else out}")
            elif tipo == "sistema":
                out = acoes.modo_foco(acao, passo.get("fechar"), passo.get("min", 0))
                resultados.append(f"Sistema: {acao} → {out}")
            elif tipo == "notificacao":
                from core import acoes
                acoes._notificar("Flow", passo.get("mensagem", passo.get("texto", "")))
                resultados.append(f"Notificação: {passo.get('mensagem', passo.get('texto', ''))}")
            elif tipo == "comando":
                out = subprocess.run(passo.get("cmd", ""), shell=True, capture_output=True, text=True, timeout=60)
                resultados.append(f"Comando: {out.stdout[:80]}")
            elif tipo == "timer":
                from main import criar_timer
                tid = criar_timer(passo.get("nome", nome), passo.get("segundos", 300), passo.get("alarme", True))
                resultados.append(f"Timer: {passo.get('nome', nome)} ({passo.get('segundos', 300)}s)")
            elif tipo == "clima":
                resultados.append(f"Clima: {clima_resumo(passo.get('cidade', 'Taquara'))}")
            elif tipo == "esperar":
                _time.sleep(passo.get("segundos", 2))
                resultados.append(f"Esperou {passo.get('segundos', 2)}s")
            else:
                resultados.append(f"(passo desconhecido: {tipo})")
        except Exception as e:
            resultados.append(f"Erro no passo '{tipo}': {e}")
    return {"ok": True, "rotina": nome, "resultados": resultados}


def rotinas_resumo():
    rotinas = rotinas_listar()
    if not rotinas:
        return "Nenhuma rotina criada."
    return "\n".join(f"• {r['nome']} ({len(r['passos'])} passos)" for r in rotinas)

# ============================= WhatsApp Web (Playwright) =============================
def _pw_page():
    from core.acoes import _get_page
    return _get_page()

def whatsapp_enviar(destinatario, mensagem):
    try:
        pg = _pw_page()
        pg.goto("https://web.whatsapp.com", wait_until="domcontentloaded", timeout=60000)
        _time.sleep(5)
        # Check if logged in
        if pg.locator("[data-testid='qrcode']").count() > 0:
            return {"ok": False, "error": "WhatsApp não está logado. Escaneie o QR Code no navegador."}
        # Search contact
        caixa = pg.locator("[data-testid='chat-list-search'], [contenteditable='true'][data-tab='3']")
        if caixa.count() == 0:
            return {"ok": False, "error": "Não encontrei a caixa de busca do WhatsApp."}
        caixa.first.click()
        _time.sleep(0.5)
        caixa.first.fill(destinatario)
        _time.sleep(2)
        # Click first result
        pg.locator(f"[data-testid='cell-frame-title'] >> text='{destinatario}'").first.click(timeout=5000)
        _time.sleep(1)
        # Type and send
        msg_box = pg.locator("[data-testid='conversation-compose-box-input'], [contenteditable='true'][data-tab='10']")
        if msg_box.count() == 0:
            return {"ok": False, "error": "Não encontrei o campo de mensagem."}
        msg_box.first.fill(mensagem)
        _time.sleep(0.3)
        pg.keyboard.press("Enter")
        _time.sleep(1)
        return {"ok": True, "msg": f"Mensagem enviada para {destinatario}!"}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}


def whatsapp_abrir(destinatario=""):
    try:
        pg = _pw_page()
        pg.goto("https://web.whatsapp.com", wait_until="domcontentloaded", timeout=60000)
        return {"ok": True, "msg": f"WhatsApp aberto no navegador. {('Buscando ' + destinatario) if destinatario else ''}"}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}

# ============================= Gmail (Playwright) =============================
def gmail_ler(query="is:unread", max_results=5):
    try:
        pg = _pw_page()
        pg.goto("https://mail.google.com/mail/u/0/#search/" + query.replace(" ", "+"),
                wait_until="domcontentloaded", timeout=60000)
        _time.sleep(4)
        emails = []
        rows = pg.locator("tr.zA").all()[:max_results]
        for row in rows:
            try:
                remetente = row.locator(".yX.xY .yW").first.inner_text().strip()
                assunto = row.locator(".y6 .bog").first.inner_text().strip()
                preview = row.locator(".y6 .y2").first.inner_text().strip()
                emails.append({"de": remetente[:50], "assunto": assunto[:80], "preview": preview[:120]})
            except Exception:
                continue
        return {"ok": True, "emails": emails, "total": len(rows)}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}


def gmail_abrir(query=""):
    try:
        pg = _pw_page()
        url = "https://mail.google.com/mail/u/0/"
        if query:
            url += "#search/" + query.replace(" ", "+")
        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
        return {"ok": True, "msg": "Gmail aberto no navegador."}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}

# ============================= Google Calendar (Playwright) =============================
def calendario_eventos(dias=7):
    try:
        pg = _pw_page()
        pg.goto("https://calendar.google.com/calendar/r/week", wait_until="domcontentloaded", timeout=60000)
        _time.sleep(4)
        eventos = []
        evts = pg.locator("[data-eventid], .fc-event").all()[:10]
        for ev in evts:
            try:
                titulo = ev.inner_text().strip()
                if titulo:
                    eventos.append({"titulo": titulo[:80]})
            except Exception:
                continue
        return {"ok": True, "eventos": eventos}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}


def calendario_abrir():
    try:
        pg = _pw_page()
        pg.goto("https://calendar.google.com", wait_until="domcontentloaded", timeout=60000)
        return {"ok": True, "msg": "Google Calendar aberto no navegador."}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}

# ============================= Detecção de Intenção =============================
_INTENTS = [
    (["clima", "tempo em", "tempo agora", "temperatura", "vai chover", "chuva hoje"], "clima"),
    (["que hora", "hora agora", "que dia", "data hoje", "dia de hoje", "dia da semana"], "hora"),
    (["espaço em disco", "espaço", "disco rígido", "quanto ocupa", "memória ram", "cpu", "como tá o pc", "sistema"], "sistema"),
    (["clipboard", "copiar", "cola", "área de transferência", "o que copiei"], "clipboard"),
    (["brilho", "mais escuro", "mais claro", "tela escura"], "brilho"),
    (["lista de compras", "comprar", "mercado", "supermercado", "lista compras", "adicionar na lista"], "compras"),
    (["nota", "lembrete", "anotar", "lembra de", "anota aí"], "notas"),
    (["rotina", "rotinas", "modo jantar", "modo dormir", "bom dia automático"], "rotinas"),
    (["whatsapp", "mandar msg", "enviar mensagem", "mandar pra"], "whatsapp"),
    (["gmail", "email", "emails", "caixa de entrada", "mensagem"], "gmail"),
    (["calendário", "agenda", "compromisso", "reunião"], "calendario"),
]


def detectar_intencao(texto):
    t = texto.lower()
    for palavras, intent in _INTENTS:
        if any(p in t for p in palavras):
            return intent, t
    return None, t
