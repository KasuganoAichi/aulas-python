import tkinter as tk

def calcular_tabuada():
    try:
        x = int(entrada.get())
        if 0 < x < 11:
            tabuada_texto = ""
            for i in range (1, 11):
                tabuada_texto = tabuada_texto + f"{x} X {i} = {x*i}\n"
            tabuada.config(text=tabuada_texto)
        else:
            raise ValueError
    except ValueError:
        tabuada.config(text="Informe um número inteiro entre 1 e 10.")

janela = tk.Tk()
janela.title("Tabuada Automática")
janela.geometry("450x700")

tk.Label(janela, text="Informe número para ser calculada a tabuada:", font=("Arial", 12)).pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(pady=5)
tk.Button(janela, text="Calcular", command=calcular_tabuada).pack(pady=5)
tabuada = tk.Label(janela, text="", font=("Arial", 10))
tabuada.pack(pady=5)

janela.mainloop()