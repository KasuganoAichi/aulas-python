import tkinter as tk
from tkinter import ttk, messagebox

def enviado():
    messagebox.showinfo("Sucesso", "Dados enviados!")
    return

janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("420x520")

tk.Label(janela, text="Nome").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Label(janela, text="E-mail").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Entry(janela, text="Nome").grid(row=0, column=1, padx=10, pady=5, sticky="w")
tk.Entry(janela, text="E-mail").grid(row=1, column=1, padx=10, pady=5, sticky="w")
tk.Button(janela, text="Enviar", command=enviado).grid(row=2, columnspan=2, padx=10, pady=5, sticky="w")

janela.mainloop()