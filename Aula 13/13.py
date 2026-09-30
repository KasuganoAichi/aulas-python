import tkinter as tk

def contar():
    tam = len(entrada.get())
    res.config(text=f"Total de Caracteres: {tam}")
    
janela = tk.Tk()
janela.title("Contar de Caraceteres")
janela.geometry("450x500")

tk.Label(janela, text="Digite um texto na caixa abaixo.", font=("Arial", 12)).pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(pady=2)
tk.Button(janela, text="Contar caracteres", command=contar).pack(pady=5)
res = tk.Label(janela, text="", font=("Arial", 12))
res.pack(pady=5)

janela.mainloop()


