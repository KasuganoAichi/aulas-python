import tkinter as tk
from tkinter import ttk, messagebox

def welcome():
    if aceito.get():
        messagebox.showinfo("Bem-vindo!", "Bem-Vindo!")

janela = tk.Tk()
janela.title("Checkbutton")
janela.geometry("420x520")

aceito = tk.BooleanVar(value=False)
termos = tk.Checkbutton(janela, text="Aceito os termos", variable=aceito)
termos.grid(row=0,column=0, columnspan=2, padx=10, pady=5, sticky="w")
tk.Button(janela, text="Contiuar", command=welcome).grid(row=1,column=0,columnspan=2, padx=10, pady=5, sticky="w")

janela.mainloop()