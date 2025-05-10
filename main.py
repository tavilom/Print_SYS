import streamlit as st
from PIL import Image, ImageDraw
from config import TAMANHOS_MATERIAIS, TAMANHOS_FOLHAS
from processamento import calcular_proporcao


def desenhar_camiseta(lado="Frente", largura=400, altura=500):
    imagem = Image.new("RGBA", (largura, altura), (255, 255, 255, 0))
    draw = ImageDraw.Draw(imagem)

    # Corpo da camiseta
    corpo_top = 100
    corpo_bottom = altura - 50
    corpo_left = 100
    corpo_right = largura - 100
    draw.rectangle([corpo_left, corpo_top, corpo_right, corpo_bottom], fill=(200, 200, 200, 255))

    # Mangas
    draw.polygon([(corpo_left, corpo_top),
                  (corpo_left - 60, corpo_top + 80),
                  (corpo_left, corpo_top + 80)], fill=(180, 180, 180, 255))

    draw.polygon([(corpo_right, corpo_top),
                  (corpo_right + 60, corpo_top + 80),
                  (corpo_right, corpo_top + 80)], fill=(180, 180, 180, 255))

    # Indicação de lado
    if lado == "Costas":
        draw.text((180, 20), "COSTAS", fill="black")
    else:
        draw.text((180, 20), "FRENTE", fill="black")

    return imagem


st.title("Sistema de Impressão de Camisetas")

material = st.selectbox("Selecione o Material", list(TAMANHOS_MATERIAIS.keys()))
folha = st.selectbox("Selecione o Tipo de Folha", list(TAMANHOS_FOLHAS.keys()))

uploaded_file = st.file_uploader("Envie a imagem da estampa", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    imagem_estampa = Image.open(uploaded_file).convert("RGBA")

    lado = st.radio("Onde a imagem será aplicada?", ["Frente", "Costas"])
    largura_input = st.slider("Largura da estampa (cm)", 5.0, 50.0, 20.0)
    altura_input = st.slider("Altura da estampa (cm)", 5.0, 50.0, 20.0)

    # Redimensiona estampa proporcionalmente
    largura_px = int(largura_input * 10)
    altura_px = int(altura_input * 10)
    estampa_redimensionada = imagem_estampa.resize((largura_px, altura_px))

    # Desenha modelo da camiseta
    modelo = desenhar_camiseta(lado=lado)

    # Centraliza a estampa
    centro_x = (modelo.width - estampa_redimensionada.width) // 2
    centro_y = 180  # posição fixa no tronco

    modelo.paste(estampa_redimensionada, (centro_x, centro_y), estampa_redimensionada)

    st.markdown("### Prévia da estampa na camiseta:")
    st.image(modelo, use_container_width=True)

    # Sugestão automática
    tamanho_material = TAMANHOS_MATERIAIS[material]
    tamanho_folha = TAMANHOS_FOLHAS[folha]
    escala, largura_final, altura_final = calcular_proporcao(tamanho_material, tamanho_folha)

    st.markdown("### Sugestão automática:")
    st.write(f"Escala sugerida: **{escala:.2f}x**")
    st.write(f"Tamanho ajustado: **{largura_final}cm x {altura_final}cm**")
