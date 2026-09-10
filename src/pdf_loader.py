from pathlib import Path

def extrair_txt(txt_path: str) -> str:
    path = Path(txt_path)
    if not path.exists():
        raise FileNotFoundError("arquivo .txt não encontrado")

    return path.read_text(encoding="utf-8")
