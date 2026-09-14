import uuid
from pathlib import Path

import chromadb

DB_PATH = Path(__file__).resolve().parent.parent / "memoria_db"
_col = None


def _collection():
    global _col
    if _col is None:
        c = chromadb.PersistentClient(path=str(DB_PATH))
        _col = c.get_or_create_collection("flow_memoria", metadata={"hnsw:space": "cosine"})
    return _col


def _embed(textos):
    from core.brain import client as nv
    try:
        r = nv.embeddings.create(model="nvidia/nemotron-3-embed-1b", input=textos)
        return [d.embedding for d in r.data]
    except Exception:
        return None


def aprender(texto, fonte="manual", importancia=0.7):
    texto = (texto or "").strip()
    if not texto:
        return None
    emb = _embed([texto])
    if emb is None:
        return None
    doc_id = uuid.uuid4().hex[:12]
    _collection().add(
        ids=[doc_id],
        embeddings=emb,
        documents=[texto],
        metadatas=[{
            "fonte": fonte,
            "importancia": float(importancia),
            "ts": _time_now(),
        }],
    )
    return doc_id


def buscar(query, k=3):
    emb = _embed([query])
    if emb is None:
        return []
    res = _collection().query(query_embeddings=emb, n_results=min(k, 10))
    docs = res.get("documents") or []
    metas = res.get("metadatas") or []
    return [{"texto": d, "meta": m, "dist": 1.0}
            for d, m in zip(docs[0] if docs else [], metas[0] if metas else [])]


def _time_now():
    from datetime import datetime
    return datetime.now().isoformat()