import tkinter as tk

def somar():
    try:
        res = int(entrada1.get()) + int(entrada2.get())
        resultado.config(text=res)
    except:
        resultado.config(text="Informe somente números inteiros.")

janela = tk.Tk()
janela.title("Somador")
janela.geometry("400x500")

tk.Label(janela, text="Somador", font=("Arial", 20)).pack(pady=10)

entrada1 = tk.Entry(janela)
entrada1.pack(pady=10)

entrada2 = tk.Entry(janela)
entrada2.pack(pady=10)

tk.Button(janela, text="Somar", command=somar).pack(pady=10)

resultado = tk.Label(janela, text="", font=("Arial", 12))
resultado.pack(pady=10)

janela.mainloop()