import tkinter as tk

def converter():
    try:
        temp = (float(entrada.get()) * (9/5)) + 32
        resultado.config(text=f"{temp} °F")
    except ValueError:
        resultado.config(text="Informa uma temperatura válida.")

janela = tk.Tk()
janela.title("Conversor de Temperatura")
janela.geometry("400x500")

tk.Label(janela, text="Conversor de Temperatura", font=("Arial", 20)).pack(pady=5)
tk.Label(janela, text="Informe temperatura em Celsius: ", font=("Arial", 14)).pack(pady=5)

entrada = tk.Entry(janela)
entrada.pack(pady=5)

tk.Button(janela, text="Converter", command=converter).pack(pady=5)

resultado = tk.Label(janela, text="", font=("Arial", 12))
resultado.pack(pady=5)

janela.mainloop()