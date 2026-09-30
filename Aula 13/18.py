import tkinter as tk

def calcula_troco():
    try:
        total = float(total_entry.get())
        pago = float(pago_entry.get())
        if total < pago:
            troco = (total - pago) * -1
            res.config(text=f"Faltam R${troco:.2f} para completar o pagamento!")
        else:
            troco = total - pago
            res.config(text=f"Troco a devolver: R${troco:.2f}")
    except ValueError:
        res.config(text="Favor informe apenas valores númericos!")

janela = tk.Tk()
janela.title("Simulador de Troco")
janela.geometry("450x500")

tk.Label(janela, text="Informe valor total da compra: ", font=("Arial", 14)).pack(pady=5)
total_entry = tk.Entry(janela)
total_entry.pack(pady=5)
tk.Label(janela, text="Informe valor entregue pelo cliente: ", font=("Arial", 14)).pack(pady=5)
pago_entry = tk.Entry(janela)
pago_entry.pack(pady=5)
tk.Button(janela, text="Calcular Troco", command=calcula_troco).pack(pady=5)
res = tk.Label(janela, text="", font=("Arial", 12))
res.pack(pady=5)

janela.mainloop()