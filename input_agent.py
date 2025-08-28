from docx import Document

def extract_cobol_from_docx(docx_path):
    """
    Extracts COBOL code from a DOCX file by reading all non-empty paragraphs.

    Args:
        docx_path (str): Path to the DOCX file.

    Returns:
        str: Combined COBOL code as a single string.
    """
    doc = Document(docx_path)
    cobol_code = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            cobol_code.append(text)

    return "\n".join(cobol_code)
