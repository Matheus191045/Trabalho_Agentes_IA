from sentence_transformers import SentenceTransformer
import chromadb

# Modelo de embeddings
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Banco vetorial
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="politica_financeira"
)


def consultar_regras(pergunta):

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