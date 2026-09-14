import atexit
import ctypes
import json
import os
import subprocess
import threading
import time as _time
from urllib.parse import quote
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
AMB_DIR = BASE / "sons"  # sons royalty-free (mp3/ogg/wav)

# ============================= X11 input (XTEST) =============================
_DISPLAY = os.environ.get("DISPLAY", ":0").encode()
_libX11 = ctypes.CDLL("libX11.so.6")
_libXtst = ctypes.CDLL("libXtst.so.6")

_libX11.XOpenDisplay.restype = ctypes.c_void_p
_libX11.XOpenDisplay.argtypes = [ctypes.c_char_p]
_libX11.XKeysymToKeycode.restype = ctypes.c_uint
_libX11.XKeysymToKeycode.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
_libX11.XStringToKeysym.restype = ctypes.c_ulong
_libX11.XStringToKeysym.argtypes = [ctypes.c_char_p]
_libX11.XFlush.argtypes = [ctypes.c_void_p]

_libXtst.XTestFakeMotionEvent.argtypes = [
    ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_ulong]
_libXtst.XTestFakeButtonEvent.argtypes = [
    ctypes.c_void_p, ctypes.c_uint, ctypes.c_int, ctypes.c_ulong]
_libXtst.XTestFakeKeyEvent.argtypes = [
    ctypes.c_void_p, ctypes.c_uint, ctypes.c_int, ctypes.c_ulong]

_dpy = _libX11.XOpenDisplay(_DISPLAY)

_SHIFT_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~')
_SIMB = {
    " ": "space", "!": "exclam", '"': "quotedbl", "#": "numbersign", "$": "dollar",
    "%": "percent", "&": "ampersand", "'": "apostrophe", "(": "parenleft",
    ")": "parenright", "*": "asterisk", "+": "plus", ",": "comma", "-": "minus",
    ".": "period", "/": "slash", ":": "colon", ";": "semicolon", "<": "less",
    "=": "equal", ">": "greater", "?": "question", "@": "at", "[": "bracketleft",
    "\\": "backslash", "]": "bracketright", "^": "asciicircum", "_": "underscore",
    "`": "grave", "{": "braceleft", "|": "bar", "}": "braceright", "~": "asciitilde",
    "\n": "Return", "\t": "Tab",
}


def _keysym(ch):
    nome = _SIMB.get(ch)
    if nome:
        return _libX11.XStringToKeysym(nome.encode())
    if ch.isascii():
        return ord(ch)
    return 0


def mover_mouse(x, y):
    _libXtst.XTestFakeMotionEvent(_dpy, -1, int(x), int(y), 0)
    _libX11.XFlush(_dpy)


def clicar(x, y, duplo=False):
    _libXtst.XTestFakeMotionEvent(_dpy, -1, int(x), int(y), 0)
    for _ in range(2 if duplo else 1):
        _libXtst.XTestFakeButtonEvent(_dpy, 1, 1, 0)
        _libXtst.XTestFakeButtonEvent(_dpy, 1, 0, 0)
        _time.sleep(0.05)
    _libX11.XFlush(_dpy)


def _fake_tecla(keycode, shift):
    if shift:
        mod = _libX11.XStringToKeysym(b"Shift_L")
        _libXtst.XTestFakeKeyEvent(_dpy, _libX11.XKeysymToKeycode(_dpy, mod), 1, 0)
    _libXtst.XTestFakeKeyEvent(_dpy, keycode, 1, 0)
    _libXtst.XTestFakeKeyEvent(_dpy, keycode, 0, 0)
    if shift:
        mod = _libX11.XStringToKeysym(b"Shift_L")
        _libXtst.XTestFakeKeyEvent(_dpy, _libX11.XKeysymToKeycode(_dpy, mod), 0, 0)


def tecla(nome):
    ks = _libX11.XStringToKeysym(nome.encode())
    if ks:
        kc = _libX11.XKeysymToKeycode(_dpy, ks)
        _fake_tecla(kc, False)


def digitar(texto):
    for ch in str(texto or ""):
        if ch == "\n":
            tecla("Return")
            continue
        ks = _keysym(ch)
        if not ks:
            continue
        kc = _libX11.XKeysymToKeycode(_dpy, ks)
        if kc:
            _fake_tecla(kc, ch in _SHIFT_CHARS)
            _time.sleep(0.01)
    _libX11.XFlush(_dpy)


# ============================= Playwright browser =============================
_pw = None
_browser = None
_page = None
_pw_lock = threading.Lock()


def _get_page():
    global _pw, _browser, _page
    with _pw_lock:
        if _pw is None:
            from playwright.sync_api import sync_playwright
            _pw = sync_playwright().start()
            _browser = _pw.chromium.launch(
                headless=False,
                args=["--start-maximized", "--disable-blink-features=AutomationControlled"],
            )
        if _page is None or _page.is_closed():
            _page = _browser.new_page(viewport=None)
    return _page


@atexit.register
def _fim():
    global _browser, _pw
    try:
        if _browser:
            _browser.close()
    except Exception:
        pass


def pw_abrir(url, aguardar=1200):
    pg = _get_page()
    pg.goto(url, wait_until="domcontentloaded", timeout=60000)
    if aguardar:
        _time.sleep(aguardar / 1000)
    return pg.title()


def pw_clicar(texto, campo="text"):
    pg = _get_page()
    alvo = pg.get_by_text(texto, exact=False) if campo == "text" else pg.locator(campo)
    alvo.first.click(timeout=15000)
    _time.sleep(1.2)
    return True


def pw_digitar(texto, campo):
    pg = _get_page()
    caixa = pg.get_by_placeholder(campo) if not campo.startswith(("input", "#", ".", "[")) else pg.locator(campo)
    caixa.first.fill(texto)
    return True


def pw_tecla(nome):
    _get_page().keyboard.press(nome)
    return True


def pw_exec(plano):
    """Executa um plano Playwright: lista de {acao, ...}. Retorna resultado."""
    passos = []
    pg = _get_page()
    demo = False
    try:
        pg.locator("body").wait_for(timeout=1500)
    except Exception:
        pass
    for p in plano:
        a = p.get("acao")
        if a == "abrir":
            pg.goto(p["url"], wait_until="domcontentloaded", timeout=60000)
            _time.sleep(1.0)
            passos.append(f"abriu {p['url']}")
        elif a == "clicar":
            alvo = pg.get_by_text(p.get("texto"), exact=False).first
            alvo.click(timeout=15000, force=True)
            _time.sleep(1.2)
            passos.append(f"clicou em '{p.get('texto')}'")
        elif a == "clicar_seletor" and p.get("seletor"):
            pg.locator(p["seletor"]).first.click(timeout=15000, force=True)
            _time.sleep(1.2)
            passos.append(f"clicou em {p.get('seletor')}")
        elif a == "digitar":
            caixa = pg.get_by_placeholder(p.get("campo"))
            if caixa.count() == 0:
                caixa = pg.locator(p.get("campo") or "input[type=text],input:not([type])")
            caixa.first.fill(p.get("texto", ""))
            _time.sleep(0.3)
            passos.append(f"digitou '{p.get('texto')}' em '{p.get('campo')}'")
        elif a == "tecla":
            pg.keyboard.press(p.get("tecla", "Enter"))
            _time.sleep(1.0)
            passos.append(f"apertou {p.get('tecla')}")
        elif a == "esperar":
            _time.sleep(float(p.get("seg", 1)))
            passos.append(f"esperou {p.get('seg', 1)}s")
        else:
            passos.append(f"(ignorou {a})")
    demo = True
    return {"ok": demo, "passos": passos, "titulo": pg.title()}


# ============================= Receitas =============================
_SITES_RECEITA = [
    {"nome": "TudoGostoso",
     "url": "https://www.tudogostoso.com.br/busca?q={q}",
     "sel": "a[href*='/receita/']", "max": 2},
    {"nome": "Panelinha",
     "url": "https://www.panelinha.com.br/busca?q={q}",
     "sel": "a[href*='/receita/']", "max": 2},
]


def buscar_receitas(query, sites=None):
    """Busca receitas em sites confiáveis e devolve apenas títulos + links (crédito)."""
    sites = sites or _SITES_RECEITA
    resultados = []
    try:
        pg = _get_page()
    except Exception:
        return []
    q = quote(query)
    ignores = {"de", "da", "do", "das", "dos", "em", "com", "e", "a", "o", "à",
               "para", "na", "no", "sem", "que"}
    palavras = [p for p in query.lower().split() if p not in ignores]
    for site in sites:
        try:
            pg.goto(site["url"].format(q=q), wait_until="domcontentloaded", timeout=45000)
            pg.wait_for_timeout(2500)
            achados = []
            vistos = set()
            for link in pg.locator(site["sel"]).all():
                href = (link.get_attribute("href") or "").strip()
                if not href.startswith("http"):
                    href = "/".join(site["url"].split("/")[:3]) + href
                titulo = (link.inner_text() or "").strip().splitlines()[0].strip()
                if not titulo or href in vistos or "receit" not in href:
                    continue
                vistos.add(href)
                score = 0 if not palavras else sum(1 for w in palavras if w in titulo.lower())
                achados.append((score, titulo[:90], href))
            per_site = sorted(achados, key=lambda x: -x[0])[: site["max"] or 2]
            relevantes = [a for a in per_site if a[0] > 0] if palavras else per_site
            if not relevantes:
                continue
            for score, titulo, href in relevantes:
                resultados.append({"site": site["nome"], "titulo": titulo, "url": href})
        except Exception:
            continue
    return resultados[:6]


# ============================= Música / MPRIS =============================
def _players():
    try:
        out = subprocess.check_output(["busctl", "--user", "list", "--no-pager"],
                                      text=True, timeout=10)
    except Exception:
        return []
    return [l.split()[0] for l in out.splitlines() if "org.mpris.MediaPlayer2." in l]


def _mpris(player, metodo, *args):
    cmd = ["busctl", "--user", "call", player, "/org/mpris/MediaPlayer2",
           "org.mpris.MediaPlayer2.Player", metodo, *args]
    return subprocess.run(cmd, capture_output=True, text=True, timeout=15)


def _status(player):
    try:
        out = subprocess.check_output(
            ["busctl", "--user", "get-property", player, "/org/mpris/MediaPlayer2",
             "org.mpris.MediaPlayer2.Player", "PlaybackStatus"], text=True, timeout=10)
    except Exception:
        return "?"
    return out.strip().split()[-1]


def agora_tocando():
    """Retorna o que está tocando no primeiro player MPRIS, junto com a lista."""
    out = {"players": _players(), "status": "parado", "titulo": "", "artista": "",
           "volume": None, "player": ""}
    players = out["players"]
    if not players:
        return out
    alvo = players[0]
    out["player"] = alvo
    out["status"] = _status(alvo)
    try:
        meta = subprocess.check_output(
            ["busctl", "--user", "get-property", alvo, "/org/mpris/MediaPlayer2",
             "org.mpris.MediaPlayer2.Player", "Metadata"], text=True, timeout=10)
        titulo = artista = ""
        for linha in meta.splitlines():
            s = linha.strip()
            if "xesam:title" in s and titulo == "":
                i = s.rfind('"')
                j = s.rfind('"', 0, i)
                titulo = s[j + 1:i] if j >= 0 else ""
            elif "xesam:artist" in s and artista == "":
                i = s.rfind('"')
                j = s.rfind('"', 0, i)
                artista = s[j + 1:i] if j >= 0 else ""
        out["titulo"] = titulo or "-"
        out["artista"] = artista or "-"
    except Exception:
        pass
    try:
        v = subprocess.check_output(
            ["busctl", "--user", "get-property", alvo, "/org/mpris/MediaPlayer2",
             "org.mpris.MediaPlayer2.Player", "Volume"], text=True, timeout=10)
        out["volume"] = round(float(v.split()[-1]) * 100)
    except Exception:
        pass
    return out


_ffprocs = []


def _parar_ff():
    for p in _ffprocs[:]:
        try:
            p.terminate()
        except Exception:
            pass
    _ffprocs.clear()


def _tocar_arquivo(caminho):
    _parar_ff()
    p = subprocess.Popen(["ffplay", "-nodisp", "-loglevel", "quiet",
                          "-loop", "0", caminho])
    _ffprocs.append(p)
    return os.path.basename(caminho)


_MUSICA_DIRS = ["/home/flow-social/Música", "/home/flow-social/Musicas",
                "/home/flow-social/Music", "/run/media/flow-social/HD FLOW/Música",
                "/run/media/flow-social/HD FLOW/Musicas", "/run/media/flow-social/HD FLOW/Music"]


def _pasta_musica(caminho=""):
    if caminho and os.path.isdir(caminho):
        return caminho
    for d in _MUSICA_DIRS:
        if os.path.isdir(d):
            return d
    return None


def listar_locais(caminho=""):
    pasta = _pasta_musica(caminho)
    if not pasta:
        return {"pasta": "", "musicas": []}
    exts = (".mp3", ".wav", ".ogg", ".flac", ".m4a", ".opus", ".aac")
    return {"pasta": pasta,
            "musicas": sorted(f.name for f in os.scandir(pasta)
                              if f.is_file() and f.name.lower().endswith(exts))}


def tocar_local(caminho, loop=True):
    if not os.path.isfile(caminho):
        pasta = _pasta_musica()
        if pasta:
            baixo = caminho.lower()
            achou = next((f for f in os.scandir(pasta)
                          if f.is_file() and baixo in f.name.lower()), None)
            if achou:
                caminho = achou.path
    if not os.path.isfile(caminho):
        return None
    _parar_ff()
    args = ["ffplay", "-nodisp", "-loglevel", "quiet"]
    if loop:
        args += ["-loop", "0"]
    p = subprocess.Popen(args + [caminho])
    _ffprocs.append(p)
    return os.path.basename(caminho)


def parar_musica():
    _parar_ff()
    return "Música local/sons parado."


def sons_disponiveis():
    if not AMB_DIR.exists():
        return []
    return sorted(f.name for f in AMB_DIR.iterdir()
                  if f.suffix.lower() in (".mp3", ".wav", ".ogg", ".flac"))


def musica(comando, query="", source="", player=None, volume=None):
    """Retorna resposta de texto do que foi feito."""
    players = _players()
    if comando == "agora":
        return agora_tocando()
    if comando == "lista_local":
        return listar_locais(query)
    if comando == "tocar_local":
        nome = tocar_local(query)
        if nome:
            return {"ok": True, "msg": f"Tocando '{nome}' (ffplay)", "arquivo": nome}
        return {"ok": False, "msg": f"Arquivo '{query}' não encontrado na pasta de música."}
    if comando == "parar":
        _parar_ff()
        return {"ok": True, "msg": "Reprodução local parada."}
    if comando in ("play", "pause", "playpause", "next", "previous"):
        if player:
            cand = [player]
        else:
            pref = [p for p in players if source in p] if source else players
            cand = pref or players
        if not cand:
            return "Nenhum player de música aberto. Abra o Spotify ou um player local."
        alvo = cand[0]
        nome = {"play": "Play", "pause": "Pause", "playpause": "PlayPause",
                "next": "Next", "previous": "Previous"}[comando]
        _mpris(alvo, nome)
        return {"ok": True, "msg": f"{nome} em {alvo.split('.')[-1]} → {_status(alvo)}"}
    if comando == "volume":
        if volume is None:
            return "volume sem valor"
        v = max(0.0, min(1.0, float(volume) / 100.0))
        alvo = player or (players[0] if players else None)
        if not alvo:
            return "nenhum player ativo"
        subprocess.run(["busctl", "--user", "set-property", alvo, "/org/mpris/MediaPlayer2",
                        "org.mpris.MediaPlayer2.Player", "Volume", "d", str(v)],
                       capture_output=True, timeout=10)
        return {"ok": True, "msg": f"Volume {volume}% no player."}
    if comando == "parar_som":
        _parar_ff()
        return "Sons ambiente parados."
    if comando == "tocar":
        baixo = (query or "").lower()
        amb = next((s for s in sons_disponiveis() if baixo in s.lower()), None)
        if amb:
            _tocar_arquivo(str(AMB_DIR / amb))
            return f"Tocando som ambiente '{amb.split('.')[0]}' 🌧 (pausa com 'parar_som')"
        if source == "local":
            feito = tocar_local(query)
            if feito:
                return f"Tocando música local '{feito}'"
            return f"Não achei '{query}' na pasta de música."
        return ("tocar", query, source, player)
    return f"comando '{comando}' não reconhecido"


# ============================= Modo foco =============================
_dnd_orig = None
_foco_ativo = False
_pomodoro_timer = None
_pomodoro_min = 0
_pomodoro_restante = 0


def _notificar(titulo, msg):
    try:
        subprocess.Popen(["notify-send", "-i", "weather-clear",
                          titulo, msg, "-t", "6000"])
    except Exception:
        pass


def _parar_dnd():
    global _dnd_orig
    if _dnd_orig is not None:
        subprocess.run(["gsettings", "set", "org.gnome.desktop.notifications",
                        "show-banners", _dnd_orig], capture_output=True)
        _dnd_orig = None


def mostra_timer():
    if not (_pomodoro_min and _pomodoro_restante):
        return None
    return {"min": _pomodoro_min, "faltando": _pomodoro_restante}


def _loop_timer():
    global _pomodoro_restante
    while _pomodoro_restante > 0:
        _time.sleep(1)
        _pomodoro_restante -= 1
    if _foco_ativo:
        _notificar("🍅 Pomodoro", "Tempo de foco acabou! Hora de pausa.")
        _parar_dnd()


def modo_foco(modo, fechar=None, min_=0):
    global _dnd_orig, _foco_ativo, _pomodoro_min, _pomodoro_restante, _pomodoro_timer
    if modo == "ativar":
        if _dnd_orig is None:
            out = subprocess.run(["gsettings", "get", "org.gnome.desktop.notifications",
                                  "show-banners"], capture_output=True, text=True)
            _dnd_orig = (out.stdout or "true").strip()
        subprocess.run(["gsettings", "set", "org.gnome.desktop.notifications",
                        "show-banners", "false"], capture_output=True)
        subprocess.run(["wpctl", "set-volume", "@DEFAULT_AUDIO_SINK@", "0.5"])
        fechados = []
        for app in (fechar or ["discord", "whatsapp", "telegram-desktop"]):
            r = subprocess.run(["pkill", "-f", app], capture_output=True)
            if r.returncode == 0:
                fechados.append(app)
        _foco_ativo = True
        if min_ and min_ > 0:
            _pomodoro_min = int(min_)
            _pomodoro_restante = int(min_) * 60
            if _pomodoro_timer:
                try:
                    _pomodoro_timer.join(timeout=0.1)
                except Exception:
                    pass
            _pomodoro_timer = threading.Thread(target=_loop_timer, daemon=True)
            _pomodoro_timer.start()
        _notificar("🔕 Modo foco", f"Ativado por {min_ or 25} min. Fechados: "
                   + (", ".join(fechados) or "nenhum"))
        return {"ativo": True, "fechados": fechados, "pomodoro": min_ or None}
    if modo == "desativar":
        _parar_dnd()
        subprocess.run(["wpctl", "set-volume", "@DEFAULT_AUDIO_SINK@", "1.0"])
        _foco_ativo = False
        _notificar("🔔 Modo foco", "Desativado, pode respirar.")
        return {"ativo": False}
    if modo == "status":
        return {"ativo": _foco_ativo, "timer": mostra_timer()}
    return {"erro": "modo deve ser ativar/desativar/status"}