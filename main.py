import tkinter as tk
from tkinter import messagebox
from interface import SistemaImpressao

def main():
    root = tk.Tk()
    app = SistemaImpressao(root)
    app.run()

if __name__ == "__main__":
    main()
