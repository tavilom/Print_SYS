import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import config
from processamento import calcular_tamanho, redimensionar_imagem

class SistemaImpressao(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Material
        self.material_select = toga.Selection(items=list(config.TAMANHOS_MATERIAIS.keys()))
        main_box.add(toga.Label("Selecione o Material:"))
        main_box.add(self.material_select)

        # Folha
        self.folha_select = toga.Selection(items=list(config.TAMANHOS_FOLHAS.keys()))
        main_box.add(toga.Label("Selecione o Tipo de Folha:"))
        main_box.add(self.folha_select)

        # Botão de upload
        self.caminho_imagem = ""
        self.upload_button = toga.Button("Selecionar Imagem", on_press=self.selecionar_imagem)
        main_box.add(self.upload_button)

        # Resultado
        self.resultado_label = toga.Label("Tamanho sugerido será exibido aqui.")
        main_box.add(self.resultado_label)

        # Botão de calcular
        calcular_button = toga.Button("Calcular Tamanho", on_press=self.calcular)
        main_box.add(calcular_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def selecionar_imagem(self, widget):
        self.caminho_imagem = self.main_window.select_file_dialog("Selecione a imagem")
        if self.caminho_imagem:
            self.resultado_label.text = f"Imagem selecionada: {self.caminho_imagem}"

    def calcular(self, widget):
        if not self.caminho_imagem:
            self.resultado_label.text = "Por favor, selecione uma imagem."
            return

        material = self.material_select.value
        folha = self.folha_select.value

        tamanho = calcular_tamanho(material, folha, config.TAMANHOS_MATERIAIS, config.TAMANHOS_FOLHAS)
        redimensionar_imagem(self.caminho_imagem, tamanho).save("assets/saida_redimensionada.png")

        self.resultado_label.text = f"Tamanho sugerido: {tamanho[0]} x {tamanho[1]} mm\nImagem salva em assets/saida_redimensionada.png"
