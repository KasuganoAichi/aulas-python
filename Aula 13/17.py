import tkinter as tk

def converter():
    try:
        brl = float(dl.get()) / 5.2
        res.config(text=f"R${brl:.2f}")
    except ValueError:
        res.config(text="Valor digitado inválido!")

janela = tk.Tk()
janela.title("Conversor de Moeda")
janela.geometry("450x500")

tk.Label(janela, text="Informe valor em Doláres: ", font=("Arial", 14)).pack(pady=5)
dl = tk.Entry(janela)
dl.pack(pady=5)
tk.Button(janela, text="Converter para Reais", command=converter).pack(pady=5)
res = tk.Label(janela, text="", font=("Arial", 12))
res.pack(pady=5)

janela.mainloop()