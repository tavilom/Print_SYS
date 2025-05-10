import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
from processamento import calcular_tamanho
import config

class SistemaImpressao:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Impressão")
        self.root.geometry("400x300")

        # Labels e campos para o material
        self.material_label = tk.Label(self.root, text="Selecione o Material:")
        self.material_label.pack(pady=5)

        self.material_var = tk.StringVar()
        self.material_menu = ttk.Combobox(self.root, textvariable=self.material_var)
        self.material_menu['values'] = list(config.TAMANHOS_MATERIAIS.keys())
        self.material_menu.pack(pady=5)

        # Labels e campos para a folha
        self.folha_label = tk.Label(self.root, text="Selecione o Tipo de Folha:")
        self.folha_label.pack(pady=5)

        self.folha_var = tk.StringVar()
        self.folha_menu = ttk.Combobox(self.root, textvariable=self.folha_var)
        self.folha_menu['values'] = list(config.TAMANHOS_FOLHAS.keys())
        self.folha_menu.pack(pady=5)

        # Labels e campos para o caminho da imagem com botão de procurar
        self.imagem_label = tk.Label(self.root, text="Selecione a Imagem:")
        self.imagem_label.pack(pady=5)

        self.imagem_entry = tk.Entry(self.root)
        self.imagem_entry.pack(pady=5)

        self.procurar_button = tk.Button(self.root, text="Procurar", command=self.procurar_imagem)
        self.procurar_button.pack(pady=5)

        # Botão de calcular
        self.calcular_button = tk.Button(self.root, text="Calcular Tamanho", command=self.calcular_tamanho)
        self.calcular_button.pack(pady=10)

        # Label para mostrar o resultado
        self.resultado_label = tk.Label(self.root, text="")
        self.resultado_label.pack(pady=5)

    def procurar_imagem(self):
        """Abre a janela de diálogo para selecionar um arquivo de imagem."""
        caminho_imagem = filedialog.askopenfilename(
            title="Selecione a Imagem", 
            filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )
        if caminho_imagem:
            self.imagem_entry.delete(0, tk.END)  # Limpa o campo
            self.imagem_entry.insert(0, caminho_imagem)  # Insere o caminho da imagem

    def calcular_tamanho(self):
        material = self.material_var.get()
        folha = self.folha_var.get()
        caminho_imagem = self.imagem_entry.get()

        if not material or not folha or not caminho_imagem:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        # Chama a função de cálculo
        resultado = calcular_tamanho(material, folha)
        
        # Atualiza a label com o resultado
        self.resultado_label.config(text=f"Tamanho na folha: {resultado}")

    def run(self):
        self.root.mainloop()
