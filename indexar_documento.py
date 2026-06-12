from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb

# Ler PDF
reader = PdfReader("Politica_Financeira_Empresa.pdf")

texto = ""

for pagina in reader.pages:
    texto += pagina.extract_text() + "\n"

# Quebrar em partes
chunks = texto.split("\n\n")

# Modelo de embedding
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Banco vetorial
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="politica_financeira"
)

# Inserir chunks
for i, chunk in enumerate(chunks):

    if chunk.strip():

        embedding = modelo.encode(chunk).tolist()

        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embedding]
        )

print("Documento indexado com sucesso!")



