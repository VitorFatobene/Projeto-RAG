from pypdf import PdfReader
from pathlib import Path

def extrair_pdf(pdf_path: str) -> str:
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError("pdf não encontrado")

    reader = PdfReader(path)
    pages = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            pages.append(page_text)
    return "\n".join(pages) #transforma a lista de páginas em uma única string, separando cada página por uma nova linha
