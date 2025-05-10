# processamento.py

def calcular_tamanho(material, folha):
    # A lógica de cálculo pode variar conforme o material e folha escolhidos
    if material == "Caneca" and folha == "A4":
        return "5x7 cm"
    elif "Camiseta" in material and folha == "A4":
        return "15x20 cm"
    else:
        return "Tamanho não calculado"
