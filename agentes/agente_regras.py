from sentence_transformers import SentenceTransformer
import chromadb
import os
import sys

_modelo = None
_collection = None

_DB_PATH = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "chroma_db")
)


def _open_collection():
    client = chromadb.PersistentClient(path=_DB_PATH)
    return client.get_collection(name="politica_financeira")


def warmup():
    """Pré-inicializa modelo e banco antes do MCP stdio ser ativado."""
    global _modelo, _collection
    print("[agente_regras] carregando modelo...", file=sys.stderr)
    _modelo = SentenceTransformer("all-MiniLM-L6-v2")
    print("[agente_regras] conectando ao banco vetorial...", file=sys.stderr)
    _collection = _open_collection()
    print("[agente_regras] pronto.", file=sys.stderr)


def _get_deps():
    global _modelo, _collection
    if _modelo is None:
        _modelo = SentenceTransformer("all-MiniLM-L6-v2")
    if _collection is None:
        _collection = _open_collection()
    return _modelo, _collection


def consultar_regras(pergunta):
    global _collection
    modelo, collection = _get_deps()
    embedding_pergunta = modelo.encode(pergunta).tolist()
    try:
        resultado = collection.query(
            query_embeddings=[embedding_pergunta],
            n_results=3
        )
    except Exception:
        _collection = _open_collection()
        resultado = _collection.query(
            query_embeddings=[embedding_pergunta],
            n_results=3
        )
    documentos = resultado["documents"][0]
    contexto = "\n\n".join(documentos)
    return f"""
DOCUMENTOS RECUPERADOS:

{contexto}
"""
