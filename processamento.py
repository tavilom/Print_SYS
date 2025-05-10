def calcular_proporcao(material_tamanho, folha_tamanho):
    largura_material, altura_material = material_tamanho
    largura_folha, altura_folha = folha_tamanho

    proporcao_largura = largura_folha / largura_material
    proporcao_altura = altura_folha / altura_material
    proporcao_final = min(proporcao_largura, proporcao_altura)

    largura_final = largura_material * proporcao_final
    altura_final = altura_material * proporcao_final

    return round(proporcao_final, 2), round(largura_final, 2), round(altura_final, 2)
