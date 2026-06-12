from pypdf import PdfReader


def ler_pdf():
    reader = PdfReader("Politica_Financeira_Empresa.pdf")

    texto = ""

    for pagina in reader.pages:
        texto += pagina.extract_text() + "\n"

    return texto


def consultar_regras(pergunta):
    texto = ler_pdf()

    pergunta = pergunta.lower()

    # exemplos simples
    if "limite" in pergunta and "alto risco" in pergunta:
        return texto

    if "regra" in pergunta:
        return texto

    if "política" in pergunta:
        return texto

    if "documento" in pergunta:
        return texto

    return texto


