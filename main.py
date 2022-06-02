# import principal
import streamlit as st
# imports relacionados
from PIL import Image
import pytesseract
# metodos internos
import functions.functions as fc


class OCR:

    def __init__(self):
        # altera titulo da pagina
        st.set_page_config(page_title="Python OCR")
        # inicializa variveis
        self.texto = ""
        self.analisar_texto = False

    def inicial(self):
        # conteudo inicial da pagina
        st.title("OCR")
        st.write("Optical Character Recognition (OCR)")
        imagem = st.file_uploader(
            "Upload Image for OCR", type=["png", "jpg"])
        # se selecionar alguma imagem...
        if imagem:
            img = Image.open(imagem)
            st.image(img, width=400)
            st.info("Text")
            self.texto = self.extrair_texto(img)
            st.write("{}".format(self.texto))

    def extrair_texto(self, img):
        # O comando que extrai o texto da imagem
        # texto = pytesseract.image_to_string(img)
        texto = pytesseract.image_to_data(img)
        return texto


ocr = OCR()
ocr.inicial()
