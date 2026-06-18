from sentence_transformers import SentenceTransformer
import chromadb

_modelo = None
_collection = None


def _get_deps():
    global _modelo, _collection
    if _modelo is None:
        _modelo = SentenceTransformer("all-MiniLM-L6-v2")
    if _collection is None:
        client = chromadb.PersistentClient(path="./chroma_db")
        _collection = client.get_collection(name="politica_financeira")
    return _modelo, _collection


def consultar_regras(pergunta):
    modelo, collection = _get_deps()

    embedding_pergunta = modelo.encode(pergunta).tolist()

    resultado = collection.query(
        query_embeddings=[embedding_pergunta],
        n_results=3
    )

    documentos = resultado["documents"][0]

    contexto = "\n\n".join(documentos)

    return f"""
DOCUMENTOS RECUPERADOS:

{contexto}
"""