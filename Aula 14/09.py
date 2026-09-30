import tkinter as tk
from tkinter import messagebox


def sair():
    resposta = messagebox.askyesno(
        "Confirmar",
        "Deseja sair?"
    )

    if resposta:
        janela.quit()


janela = tk.Tk()
janela.title("Sair")
janela.geometry("300x200")

texto_sair = tk.StringVar(value="Sair")

tk.Button(
    janela,
    textvariable=texto_sair,
    command=sair
).pack(pady=70)

janela.mainloop()