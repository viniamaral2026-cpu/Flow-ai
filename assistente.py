#!/usr/bin/env python3
"""FLOW — assistente de voz PT-BR, estilo Alexa.

Modalidades:
  FLOW_MODO=voz   (padrão)  diga "Flow" para chamar; fale por voz; responde por voz
  FLOW_MODO=tecla            aperte ENTER para falar

Cadeia: arecord -> [vosk wake word] -> faster-whisper -> NVIDIA (deepseek) -> edge-tts -> mpg123
"""

import json
import os
import queue
import re
import struct
import subprocess
import sys
import threading
import wave

NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
NVIDIA_MODEL = os.environ.get("FLOW_MODEL", "openai/gpt-oss-20b")
NVIDIA_KEY = os.environ.get("NVIDIA_API_KEY", "")
EDGE_VOICE = os.environ.get("FLOW_VOZ", "pt-BR-FranciscaNeural")
WHISPER_MODEL = os.environ.get("FLOW_WHISPER", "small")
DURACAO = int(os.environ.get("FLOW_DURACAO", "7"))
MODO = os.environ.get("FLOW_MODO", "voz").lower()
WORKDIR = os.path.expanduser("~/assistente-flow")
VOSK_DIR = os.path.join(WORKDIR, "modelos", "vosk-pt")
RATE = 16000
CHUNK = 4000
SILENCIO_FIM_MS = int(os.environ.get("FLOW_SILENCIO", "1000"))
ATIVACAO = os.environ.get("FLOW_ATIVACAO", '["olá flow", "flow"]')
MAX_FALA_S = 12
VOLUME_LIMIAR = int(os.environ.get("FLOW_VOLUME", "300"))

MODELO_STT = None
Q_FALA = queue.Queue()
jenkins = lambda *_: None

MEMORIA_FILE = os.path.join(WORKDIR, "memoria.txt")
INDICE_FILE = os.path.join(WORKDIR, "indice_conhecimento.txt")
_REINDEXAR = os.environ.get("FLOW_REINDEXAR") == "1"
OBS = str(os.environ.get("FLOW_SABE_CAMINHOS", "")).split(",")
SABE_CAMINHOS = [p.strip() for p in OBS if p.strip()] or [
    os.path.expanduser("~/assistente-flow/sabedoria"),
    "/run/media/flow-social/HD FLOW/FLOW-PROJETOS/FLOW-DESENVOLVIMENTO",
]
IGNORAR_DIRS = {"node_modules", ".git", "venv", "env", "dist", "build", "__pycache__",
                ".cache", "builds", "worktrees", "site-packages", ".venv", "node_modules2"}
EXT_TEXTOS = {".txt", ".md", ".py", ".js", ".ts", ".tsx", ".json", ".jsonc", ".yml",
              ".yaml", ".sh", ".html", ".css", ".sql", ".csv", ".c", ".h", ".conf",
              ".toml", ".ini", ".xml", ".vue", ".astro"}
STOPWORD = {"para", "como", "você", "voce", "vc", "uma", "com", "ela", "ele", "eles",
            "elas", "seu", "sua", "seus", "suas", "nesse", "nesta", "quando", "onde",
            "porque", "por", "que", "são", "sao", "aos", "das", "dos", "tambem",
            "também", "sobre", "muito", "mais", "menos", "está", "esta", "estou",
            "pode", "quer", "fala", "sabe", "dizer", "nome", "dia", "hoje", "todo",
            "toda", "nos", "nós", "meu", "minha", "seus", "mim", "teu", "tua",
            "via", "ben", "ser", "ter", "tem", "como", "qual", "o que", "ever",
            "coisa", "fazer", "abrir", "vocês", "voces"} 
INDICE_CACHE = None
INDICE_TEMPO = None
_PALAVRAS_CACHE = None


def falha(msg):
    print(f"\n[!] {msg}", file=sys.stderr)
    sys.exit(1)


def stream_microfone():
    """Yields chunks raw PCM (16k mono) do microfone."""
    proc = subprocess.Popen(
        ["arecord", "-q", "-D", "default", "-f", "S16_LE", "-r", str(RATE),
         "-c", "1", "-t", "raw"],
        stdout=subprocess.PIPE)
    try:
        while True:
            dados = proc.stdout.read(CHUNK)
            if not dados:
                break
            yield dados
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except Exception:
            pass


def rms(chunk):
    n = len(chunk) // 2
    if n == 0:
        return 0
    s = struct.unpack(f"{n}h", chunk)
    return sum(abs(x) for x in s) / n


def raw_para_wav(raw_path, wav_path):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le",
                    "-ar", str(RATE), "-ac", "1", "-i", raw_path, wav_path],
                   check=True)


def ler_memoria():
    try:
        if not os.path.exists(MEMORIA_FILE):
            return ""
        with open(MEMORIA_FILE) as f:
            linhas = f.read().splitlines()
        return "\n".join(linhas[-14:])
    except Exception:
        return ""


def salvar_memoria(pergunta, resposta):
    try:
        linhas = []
        if os.path.exists(MEMORIA_FILE):
            with open(MEMORIA_FILE) as f:
                linhas = f.read().splitlines()
        from datetime import datetime
        tempo = datetime.now().strftime("%d/%m %H:%M")
        linhas.append(f"• {tempo} | vc: {pergunta[:120]} | flow: {resposta[:160]}")
        linhas = linhas[-60:]
        with open(MEMORIA_FILE, "w") as f:
            f.write("\n".join(linhas) + "\n")
    except Exception:
        pass


def _construir_indice():
    import time as _t
    linhas = []
    for raiz in SABE_CAMINHOS:
        raiz = os.path.expanduser(raiz)
        if not os.path.isdir(raiz):
            continue
        arquivos = 0
        for dirpath, dirs, files in os.walk(raiz, followlinks=False):
            dirs[:] = [d for d in dirs if d not in IGNORAR_DIRS and not d.startswith(".")]
            for fn in files:
                if not any(fn.endswith(e) for e in EXT_TEXTOS):
                    continue
                caminho = os.path.join(dirpath, fn)
                try:
                    sz = os.path.getsize(caminho)
                    if sz < 10 or sz > 400_000:
                        continue
                    with open(caminho, "r", errors="ignore") as arq:
                        for i, l in zip(range(300), arq):
                            l = l.strip()
                            if l:
                                linhas.append(caminho + "\t" + l[:260])
                except Exception:
                    continue
                arquivos += 1
                if arquivos >= 1000 or len(linhas) >= 20000:
                    break
            if arquivos >= 1000 or len(linhas) >= 20000:
                break
    tmp = INDICE_FILE + ".tmp"
    with open(tmp, "w") as f:
        f.write("\n".join(linhas))
    os.replace(tmp, INDICE_FILE)
    return linhas


def buscar_conhecimento(texto):
    import time as _t
    global INDICE_CACHE, INDICE_TEMPO
    pal = [w for w in re.findall(r"[a-zà-úáâãéêíóôõúç]{3,}", texto.lower()) if w not in STOPWORD]
    if not pal:
        return ""
    try:
        if INDICE_CACHE is None:
            if (not os.path.exists(INDICE_FILE)) or _REINDEXAR or \
               (INDICE_TEMPO is None or _t.time() - INDICE_TEMPO > 86400):
                print("   📂 indexando arquivos do projeto...", flush=True)
                INDICE_CACHE = _construir_indice()
                INDICE_TEMPO = _t.time()
            else:
                with open(INDICE_FILE) as f:
                    INDICE_CACHE = f.read().splitlines()
                INDICE_TEMPO = _t.time()
    except Exception:
        return ""
    hits = []
    for l in INDICE_CACHE:
        l_low = l.lower()
        for p in pal:
            if p in l_low:
                hits.append(l)
                break
        if len(hits) >= 12:
            break
    saidas = []
    for l in hits[:8]:
        caminho, _, conteudo = l.partition("\t")
        nome = os.path.basename(caminho) if caminho else "?"
        saidas.append(f"[{nome}] {conteudo[:240]}")
    return "\n".join(saidas)


def criar_mensagens(texto):
    msgs = [{"role": "system", "content": SYS_PROMPT}]
    mem = ler_memoria()
    if mem:
        msgs.append({"role": "system", "content": "Memórias das suas conversas anteriores com o usuário:\n" + mem})
    conc = buscar_conhecimento(texto)
    if conc:
        msgs.append({"role": "system", "content": "Pedaços dos arquivos do projeto do usuário que podem ser relevantes (use se fizer sentido, sem citar o mecanismo):\n" + conc})
    msgs.append({"role": "user", "content": texto})
    return msgs


def transcrever(wav_path):
    global MODELO_STT
    if MODELO_STT is None:
        print("   ⏳ carregando transcrição...", flush=True)
        from faster_whisper import WhisperModel
        MODELO_STT = WhisperModel(WHISPER_MODEL, device="cpu", compute_type="int8")
    seg, _ = MODELO_STT.transcribe(wav_path, language="pt", vad_filter=True)
    texto = " ".join(s.text.strip() for s in seg).strip()
    print(f"   🗣 Você: {texto}")
    return texto


def perguntar_ia_stream(texto, ao_receber_frase):
    import requests, time
    corpo = {
        "model": NVIDIA_MODEL,
        "messages": criar_mensagens(texto),
        "temperature": 0.4,
        "max_tokens": 512,
        "stream": True,
    }
    t0 = time.time()
    for tent in range(1, 4):
        try:
            r = requests.post(NVIDIA_URL,
                              headers={"Authorization": f"Bearer {NVIDIA_KEY}",
                                       "Content-Type": "application/json"},
                              json=corpo, timeout=180, stream=True)
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code}: {r.text[:140]}")
            buf = ""
            texto_total = []
            for linha in r.iter_lines(decode_unicode=True):
                if not linha or not linha.startswith("data:"):
                    continue
                payload = linha[5:].strip()
                if payload == "[DONE]":
                    break
                try:
                    delta = json.loads(payload)["choices"][0]["delta"].get("content", "") or ""
                except Exception:
                    continue
                if not delta:
                    continue
                buf += delta
                texto_total.append(delta)
                partes = re.split(r"(?<=[.!?])\s+", buf)
                if len(partes) > 1:
                    for p in partes[:-1]:
                        p = p.strip()
                        if p:
                            ao_receber_frase(p)
                    buf = partes[-1]
            buf = buf.strip()
            if buf:
                ao_receber_frase(buf)
            resp = "".join(texto_total).strip()
            print(f"   ⏱ {time.time()-t0:.1f}s", flush=True)
            return resp
        except Exception as e:
            print(f"   (tentativa {tent}/3: {e})", flush=True)
            time.sleep(3)
    return ""


def _falar_sync(texto):
    mp3 = os.path.join(WORKDIR, "fala.mp3")
    subprocess.run([sys.executable, "-m", "edge_tts", "--voice", EDGE_VOICE,
                    "--text", texto, "--write-media", mp3],
                   capture_output=True, check=True)
    subprocess.run(["mpg123", "-q", mp3], check=False)


def _worker_fala():
    while True:
        frase = Q_FALA.get()
        if frase is None:
            break
        try:
            _falar_sync(frase)
        except Exception as e:
            print(f"   [!] fala: {e}", file=sys.stderr)


def falar(texto):
    if not texto:
        return
    Q_FALA.put(texto)


def executar_blocos(resposta):
    blocos = re.findall(r"```(?:bash|sh)?\s*([\s\S]*?)```", resposta)
    for bloco in blocos:
        cmd = bloco.strip()
        print(f"\n   ⚙️  Comando: $ {cmd}")
        conf = input("   Executar? (s/N): ").strip().lower()
        if conf not in ("s", "sim"):
            print("   ⏭️  pulado."); continue
        try:
            saida = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            if saida.stdout.strip():
                print("   ─ saída ─\n   " + saida.stdout.strip().replace("\n", "\n   "))
            if saida.returncode != 0 and saida.stderr.strip():
                print("   ─ erro ─\n   " + saida.stderr.strip().replace("\n", "\n   "))
            falar("Comando executado.")
        except Exception as e:
            falar(f"Não consegui executar, erro: {e}")


def timer_pela_voz(texto):
    """Reconhece pedido de timer falado e cria no backend (localhost:8000)."""
    import urllib.request
    t = re.sub(r"[\.,;!\?]+$", "", (texto or "").strip().lower())
    m = re.search(r"^(?:timer|temporizador|cronometro|cronômetro|alarme|alarma|lembrete|aviso)\s+"
                  r"(\d+)\s*(horas?|h\b|min(?:uto)?s?|m\b|seg(?:undo)?s?|s\b)?\s*(.*)$", t)
    if not m:
        return None
    n, un = int(m.group(1)), (m.group(2) or "min").strip()
    nome = (m.group(3) or "alarme").strip() or "alarme"
    un_map = {"h": 3600, "hora": 3600, "horas": 3600,
              "min": 60, "minuto": 60, "minutos": 60, "m": 60,
              "s": 1, "seg": 1, "segundo": 1, "segundos": 1}
    seg = max(1, n * un_map.get(un, 60))
    try:
        req = urllib.request.Request(
            "http://localhost:8000/api/timer",
            data=json.dumps({"nome": nome, "segundos": seg}).encode(),
            headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as r:
            d = json.loads(r.read().decode())
        if d.get("ok"):
            return f"Timer de {n} {un} chamado {nome}, criado! Vou te avisar quando acabar."
        return "Não consegui criar o timer."
    except Exception as e:
        print(f"   [!] timer: {e}", file=sys.stderr)
        return "O servidor da Flow não está ativo, não consegui criar o timer."


def processar(texto):
    if not texto:
        return
    conf = timer_pela_voz(texto)
    if conf:
        print(f"   🤖 Flow: {conf}")
        falar(conf)
        return
    print("   💭 Pensando...", flush=True)
    resposta = []
    perguntar_ia_stream(texto, lambda f: (resposta.append(f + " "), Q_FALA.put(f)))
    if not resposta:
        print("   [!] sem resposta", file=sys.stderr)
        falar("Desculpe, não consegui pensar agora.")
        return
    resp = "".join(resposta).strip()
    print(f"   🤖 Flow: {resp[:180]}")
    salvar_memoria(texto, resp)
    executar_blocos(resp)


def modo_tecla():
    wav = os.path.join(WORKDIR, "mic.wav")
    print("   ⏎  ENTER + fale (Ctrl+C sai)")
    while True:
        try:
            input("\n⏎ ENTER... ")
        except (KeyboardInterrupt, EOFError):
            print("\n👋 até mais!"); return
        try:
            subprocess.run(["arecord", "-q", "-D", "default", "-f", "S16_LE",
                            "-r", str(RATE), "-c", "1", "-t", "wav",
                            "-d", str(DURACAO), wav], check=True)
            texto = transcrever(wav)
            processar(texto)
        except KeyboardInterrupt:
            continue


def _palavras_ativacao():
    try:
        frases = json.loads(ATIVACAO)
    except Exception:
        frases = ["olá flow", "flow"]
    palavras = set()
    for f in frases:
        for w in re.findall(r"[a-zà-ú]+", f.lower()):
            if len(w) > 2 and w not in ("olá", "hey", "ei", "oi"):
                palavras.add(w)
    return palavras


def _foi_chamado(texto):
    global _PALAVRAS_CACHE
    if _PALAVRAS_CACHE is None:
        _PALAVRAS_CACHE = _palavras_ativacao()
    return any(p in texto.lower() for p in _PALAVRAS_CACHE)


def modo_voz():
    import vosk
    print("   🎙  mãos-livres: diga “Flow” (Ctrl+C sai)")
    model_vosk = vosk.Model(VOSK_DIR)
    rec = vosk.KaldiRecognizer(model_vosk, RATE, ATIVACAO)
    silencio_max_chunks = SILENCIO_FIM_MS // (CHUNK * 1000 // RATE)
    while True:
        print("   🟢 escutando...", flush=True)
        acordou = False
        fluxo = stream_microfone()
        janela = []
        try:
            for chunk in fluxo:
                vol = rms(chunk)
                janela.append(vol)
                janela = janela[-8:]
                alguem_fala = any(v > VOLUME_LIMIAR for v in janela)
                if rec.AcceptWaveform(chunk):
                    texto = json.loads(rec.Result()).get("text", "")
                    if _foi_chamado(texto):
                        acordou = True
                        break
                else:
                    parcial = rec.PartialResult()
                    if _foi_chamado(parcial) and alguem_fala:
                        acordou = True
                        break
        except KeyboardInterrupt:
            print("\n👋 até mais!"); return

        print("   🎯 Flow chamado!")
        raw = os.path.join(WORKDIR, "voz.raw")
        wav = os.path.join(WORKDIR, "voz.wav")
        buffer_bytes = bytearray()
        silencio = 0
        falou = False
        inicio = True
        try:
            with open(raw, "wb") as f:
                for chunk in fluxo:
                    f.write(chunk)
                    buffer_bytes += chunk
                    volume = rms(chunk)
                    if volume > VOLUME_LIMIAR:
                        falou = True
                        silencio = 0
                    elif falou:
                        silencio += 1
                        if silencio >= silencio_max_chunks:
                            break
                    if not inicio and len(buffer_bytes) > RATE * 2 * MAX_FALA_S:
                        break
                    inicio = False
        except KeyboardInterrupt:
            print("\n👋 até mais!"); return

        fluxo.close()
        if not falou and not inicio:
            print("   (não ouvi fala)"); continue
        raw_para_wav(raw, wav)
        try:
            texto = transcrever(wav)
            processar(texto)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(f"   [!] {e}"); continue


SYS_PROMPT = (
    "Você é o assistente pessoal de voz da FLOW, chamado Flow. Responda em português brasileiro, "
    "de forma natural e útil, como conversa falada (sem emojis, sem markdown). Seja objetiva, "
    "mas não superficial: se a pergunta pedir explicação, explique bem em algumas frases. "
    "Não invente fatos — se não souber, diga que não sabe. "
    "Aproveite a memória e os arquivos do projeto que forem relevantes. "
    "O usuário fala em voz alta para você. Se for necessário executar algo no computador "
    "(abrir app, rodar comando, ler arquivo), responda com o comando que deve ser rodado "
    "dentro de um bloco ```bash ... ``` e uma frase antes explicando o que vai fazer."
)


def main():
    if not NVIDIA_KEY:
        falha("NVIDIA_API_KEY não está definida. rode: source ~/.bashrc")
    os.makedirs(WORKDIR, exist_ok=True)
    print("=" * 52)
    print("  FLOW Assistente de Voz (PT-BR)")
    print(f"  cérebro: {NVIDIA_MODEL} | modo: {MODO}")
    print("=" * 52)
    threading.Thread(target=_worker_fala, daemon=True).start()
    print("   ⏳ pré-carregando transcrição...", flush=True)
    global MODELO_STT
    if MODELO_STT is None:
        from faster_whisper import WhisperModel
        MODELO_STT = WhisperModel(WHISPER_MODEL, device="cpu", compute_type="int8")
    if MODO == "tecla":
        modo_tecla()
    else:
        modo_voz()


if __name__ == "__main__":
    main()