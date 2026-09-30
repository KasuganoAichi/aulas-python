import tkinter as tk
from tkinter import ttk, messagebox

def tipo_plano():
    p = plano.get().capitalize()
    messagebox.showinfo("Plano", p)
    

janela = tk.Tk()
janela.title("Checkbutton")
janela.geometry("420x520")

tk.Label(janela,text="Plano:").grid(row=0,column=0, padx=10, pady=5, sticky="w")
plano = tk.StringVar(value="basico")
frame_radio = tk.Frame(janela)
frame_radio.grid(row=0, column=1, sticky="w",padx=10)
tk.Radiobutton(frame_radio, text="Básico", variable=plano, value="basico").pack(side="left")
tk.Radiobutton(frame_radio, text="Padrão", variable=plano, value="padrao").pack(side="left", padx=10)
tk.Radiobutton(frame_radio, text="Premium", variable=plano, value="premium").pack(side="left", padx=10)
tk.Button(janela, text="Contiuar", command=tipo_plano).grid(row=1,column=0,columnspan=2, padx=10, pady=5)

janela.mainloop()