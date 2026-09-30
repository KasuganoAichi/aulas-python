import tkinter as tk

def clicar():
    print("Você cliclou!")
    return

def mostrar():
    mostre = entrada.get()
    print(mostre)

janela = tk.Tk()
janela.title("Meu App")
janela.geometry("500x400")

rotulo = tk.Label(janela, text="Sistema de Cadastro", font=("Arial",18))

rotulo.pack()

rotulo2 = tk.Label(janela, text="Início", font=("Arial",18), fg="blue", bg="yellow")

rotulo2.pack(pady=10)

tk.Button(janela, text="Clique aqui", command=clicar).pack()

entrada = tk.Entry(janela)
entrada.pack(pady=5)

tk.Button(janela, text="Mostrar", command=mostrar).pack(pady=10)

resultado = tk.Label(janela, text="")

janela.mainloop()