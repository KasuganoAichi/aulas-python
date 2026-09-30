import tkinter as tk

def idade():
    try:
        idade = int(entrada.get())
        if idade < 0:
            raise ValueError
        if idade < 18:
            resultado.config(text="Menor de idade.")
        else:
            resultado.config(text="Maior de idade.")
    except ValueError:
        resultado.config(text="Idade precisa ser um valor válido")

janela = tk.Tk()
janela.title("Verificador de idade.")
janela.geometry("400x500")

tk.Label(janela, text="Verificador de Idade.", font=("Arial", 20)).pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack(pady=10)

tk.Button(janela, text="Verificar", command=idade).pack(pady=10)

resultado = tk.Label(janela, text="", font=("Arial", 12))
resultado.pack(pady=10)

janela.mainloop()
