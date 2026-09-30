import tkinter as tk

def dobrar():
    n = float(entrada.get())
    resultado.config(text=n)

janela = tk.Tk()
janela.title("Dobrador de Número")
janela.geometry("500x400")

tk.Label(janela, text="Dobrador de Número", font=("Arial", 20)).pack()

entrada = tk.Entry(janela)
entrada.pack(pady=10)

bt = tk.Button(janela, text="Dobrar", command=dobrar)
bt.pack(pady=10)

resultado = tk.Label(janela, text="", font=("Arial", 12))
resultado.pack(pady=5)

janela.mainloop()