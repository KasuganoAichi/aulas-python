import tkinter as tk

janela = tk.Tk()
janela.title("Meu App")
janela.geometry("500x400")

rotulo = tk.Label(janela, text="Sistema de Cadastro", font=("Arial",18))

rotulo.pack()

rotulo2 = tk.Label(janela, text="Início", font=("Arial",18), fg="blue", bg="yellow")

rotulo2.pack(pady=10)

janela.mainloop()