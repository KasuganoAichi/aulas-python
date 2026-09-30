import tkinter as tk

def calcularIMC():
    try:
        imc = float(peso.get()) / (float(altura.get()) * 2)
        res.config(text=f"IMC = {imc:.2f}")
    except ValueError:
        res.config(text="Informe valores válidos.")

janela = tk.Tk()
janela.title("Calculadora IMC")
janela.geometry("450x500")

tk.Label(janela, text="Informe seu Peso(em quilos):", font=("Arial", 14)).pack(pady=5)
peso = tk.Entry(janela)
peso.pack(pady=5)
tk.Label(janela, text="Informe sua Altura(em metros):", font=("Arial", 14)).pack(pady=5)
altura = tk.Entry(janela)
altura.pack(pady=5)
tk.Button(janela, text="Calcular IMC", command=calcularIMC).pack(pady=5)
res = tk.Label(janela, text="", font=("Arial", 12))
res.pack(pady=5)

janela.mainloop()