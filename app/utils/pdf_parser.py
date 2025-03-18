import io
import logging

import fitz
import pytesseract
from PIL import Image


def parse_pdf(file):
    text = ""
    with fitz.Document(stream=file.read(), filetype="pdf") as pdf_document:
        try:
            pdf_document.load_page(0)
        except Exception as e:
            raise RuntimeError(f"[extract_text_from_pdf_with_images]: Arquivo corrompido. {str(e)}")
        for page_num in range(min(pdf_document.page_count, 60)):
            page = pdf_document[page_num]
            text += page.get_text()
            for block in page.get_text("dict")["blocks"]:
                try:
                    if block["type"] != 1:
                        continue
                    image = Image.open(io.BytesIO(block["image"]))
                    if (image.width * image.height) >= (0.2 * (page.rect.width * page.rect.height)):
                        texto = pytesseract.image_to_string(image)
                        text += texto
                except Exception as e:
                    logging.info(f"Arquivo[extract_text_from_pdf_with_images]: Erro ao converter imagem: {e}")
    return text
