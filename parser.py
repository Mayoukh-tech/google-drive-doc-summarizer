import fitz
import docx


def parse_pdf(path):

    text = ""

    doc = fitz.open(path)

    for page in doc:
        text += page.get_text()

    return text


def parse_docx(path):

    doc = docx.Document(path)

    text = "\n".join([p.text for p in doc.paragraphs])

    return text


def parse_txt(path):

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_text(path):

    if path.endswith(".pdf"):
        return parse_pdf(path)

    if path.endswith(".docx"):
        return parse_docx(path)

    if path.endswith(".txt"):
        return parse_txt(path)

    return ""