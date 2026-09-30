import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Meu App")
        self.geometry("400x300")
        
        self.criar_widgets()
    
    def criar_widgets(self):
        self.label1 = tk.Label(self, text="Bem-Vindo", font=("Arial", 14))
        self.label1.pack()
        
        self.label2 = tk.Label(self, text="Informe dois números:", font=("Arial", 14))
        self.label2.pack(pady=5)

        self.entrada1 = tk.Entry(self)
        self.entrada1.pack(pady=5)
        
        self.entrada2 = tk.Entry(self)
        self.entrada2.pack(pady=5)

        self.botao1 = tk.Button(self, text="Somar", command=self.somar)
        self.botao1.pack(pady=5)
        
        self.botao2 = tk.Button(self, text="Subtrair", command=self.subtrair)
        self.botao2.pack(pady=5)
        
        self.botao3 = tk.Button(self, text="Limpar", command=self.limpar)
        self.botao3.pack(pady=5)
        
        self.resultado1 = tk.Label(self, text="", font=("Arial", 12))
        self.resultado1.pack(pady=5)

    def somar(self):
        try:
            soma = int(self.entrada1.get()) + int(self.entrada2.get())
            self.resultado1.config(text=f"{soma}")
        except ValueError:
            self.resultado1.config(text="Entrada inválida, informe apenas números.")
    
    def subtrair(self):
        try:
            subtracao = int(self.entrada1.get()) - int(self.entrada2.get())
            self.resultado1.config(text=f"{subtracao}")
        except ValueError:
            self.resultado1.config(text="Entrada inválida, informe apenas números.")
                
    def limpar(self):
        self.entrada1.delete(0, tk.END)
        self.entrada2.delete(0, tk.END)
        self.resultado1.config(text="")


app = App()
app.mainloop()