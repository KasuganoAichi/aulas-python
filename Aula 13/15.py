import tkinter as tk

def definir():
    res.config(text=entrada.get())
    return

def limpar():
    res.config(text="")
    return

janela = tk.Tk()
janela.title("Limpador de Campos")
janela.geometry("450x500")

tk.Label(janela, text="Informe um texto a ser definido:", font=("Arial", 16)).pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(pady=5)
tk.Button(janela, text="Definir", command=definir).pack(pady=5)
tk.Button(janela, text="Redefinir", command=limpar).pack(pady=5)
res = tk.Label(janela, text="", font=("Arial", 12))
res.pack(pady=5)

janela.mainloop()