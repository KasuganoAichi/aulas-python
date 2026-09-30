import random
import tkinter as tk


def elogio():
    texto = [("Momontai!"), ("Hakuna Matata!"), ("Eu sou groot!")]
    texto = random.choice(texto)
    frase.config(text=texto)
    return
janela = tk.Tk()
janela.title("Mensagem Inspiradora.")
janela.geometry("450x500")

tk.Label(janela, text="Pressione o botão para receber\n uma frase inspiradora.", font=("Arial", 14)).pack(pady=5)

tk.Button(janela, text="Pressionar", command=elogio).pack(pady=5)

frase = tk.Label(janela, text="", font=("Arial", 12))
frase.pack()

janela.mainloop()