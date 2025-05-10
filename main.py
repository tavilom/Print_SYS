# main.py

import streamlit as st
from PIL import Image
from config import TAMANHOS_MATERIAIS, TAMANHOS_FOLHAS
from processamento import redimensionar_imagem
import os

st.set_page_config(page_title="Sistema de Impressão de Materiais", layout="centered")
st.title("🎨 Sistema de Impressão de Materiais")

# Inputs
material = st.selectbox("Selecione o material", list(TAMANHOS_MATERIAIS.keys()))
folha = st.selectbox("Selecione o tipo de folha", list(TAMANHOS_FOLHAS.keys()))

imagem_upload = st.file_uploader("Envie a imagem que deseja imprimir", type=["png", "jpg", "jpeg"])
if imagem_upload:
    posicao = st.radio("A imagem será impressa na:", ["Frente", "Costas"])
    imagem = Image.open(imagem_upload)

    modelo_path = os.path.join("assets", "camiseta_frente.png" if posicao == "Frente" else "camiseta_costas.png")
    modelo = Image.open(modelo_path).convert("RGBA")
    imagem = imagem.convert("RGBA")

    st.subheader("🔧 Ajuste o tamanho da imagem sobre o modelo")
    largura = st.slider("Largura (cm)", 5, int(TAMANHOS_MATERIAIS[material][0]), 15)
    altura = st.slider("Altura (cm)", 5, int(TAMANHOS_MATERIAIS[material][1]), 15)

    imagem_redimensionada = redimensionar_imagem(imagem, (largura, altura))

    x = (modelo.width - imagem_redimensionada.width) // 2
    y = (modelo.height - imagem_redimensionada.height) // 2

    modelo_overlay = modelo.copy()
    modelo_overlay.paste(imagem_redimensionada, (x, y), imagem_redimensionada)

    st.image(modelo_overlay, caption="Visualização do modelo com a imagem aplicada", use_container_width=True)
