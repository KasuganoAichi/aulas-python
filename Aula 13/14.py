import tkinter as tk

def inversor():
    texto = entrada.get()
    res.config(text=texto[::-1])
    return

janela = tk.Tk()
janela.title("Inversor de Palavras")
janela.geometry("450x500")

tk.Label(janela, text="Digite palavra a ser invertida:").pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(pady=5)
tk.Button(janela, text="Inverter", command=inversor).pack(pady=5)
res = tk.Label(janela, text="")
res.pack(pady=5)

janela.mainloop()