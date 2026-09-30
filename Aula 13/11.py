import tkinter as tk

janela = tk.Tk()
janela.title("Cartão Digital")
janela.geometry("350x220")

tk.Label(janela, text="Tech Soluções",
        font=("Verdana", 14, "bold"), fg="white",
        bg="darkblue").pack()

tk.Label(janela, text="Soluções para seus problemas Tech").pack(pady=15)

janela.mainloop()