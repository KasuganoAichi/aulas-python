import tkinter as tk

def validador():
    psswd = senha.get()
    if len(psswd) < 6:
        valid.config(text="Senha fraca (mínimo 6 dígitos.)", fg="red")
    elif any(c.isdigit() for c in psswd):
        valid.config(text="Senha forte e válida!", fg="green")
    else:
        valid.config(text="Senha média (adicione números para melhorar)", fg="orange")

janela = tk.Tk()
janela.title("Validador de Senha Segura")
janela.geometry("450x500")
tk.Label(janela, text="Informe uma senha: ", font=("Arial", 14)).pack(pady=5)
senha = tk.Entry(janela, show="*", font=("Arial", 12))
senha.pack(pady=5)
tk.Button(janela, text="Validar", command=validador).pack(pady=5)
valid = tk.Label(janela, text="", font=("Arial", 14))
valid.pack(pady=5)

janela.mainloop()