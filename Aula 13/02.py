import tkinter as tk

janela = tk.Tk()
janela.title("Meu App")
janela.geometry("500x400")

rotulo = tk.Label(janela, text="Sistema de Cadastro", font=("Arial",18))

rotulo.pack()

janela.mainloop()