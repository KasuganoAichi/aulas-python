import tkinter as tk
from tkinter import ttk, messagebox

def cidade_selecionada():
    messagebox.showinfo("Cidade", cidade.get())


janela = tk.Tk()
janela.title("Checkbutton")
janela.geometry("420x520")

tk.Label(janela, text="Cidades:").grid(row=0, column=0, padx=10, pady=5, sticky="w")

cidade = tk.StringVar(value="São Paulo")
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Curitiba"]

combo_cidades = ttk.Combobox(
    janela,
    textvariable=cidade,
    values=cidades,
    state="readonly"
)
combo_cidades.grid(row=0, column=1, padx=10, pady=5)

tk.Button(
    janela, text="Exibir cidade", command=cidade_selecionada
).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

janela.mainloop()