import tkinter as tk
from tkinter import ttk, messagebox

janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("420x520")

tk.Label(janela, text="Nome").grid(row=0, column=0, padx=10, pady=5)
tk.Label(janela, text="E-mail").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(janela, text="Nome").grid(row=0, column=1, padx=10, pady=5)
tk.Entry(janela, text="E-mail").grid(row=1, column=1, padx=10, pady=5)

janela.mainloop()