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
        
        self.label2 = tk.Label(self, text="Informe um número", font=("Arial", 14))
        self.label2.pack(pady=5)

        self.entrada1 = tk.Entry(self)
        self.entrada1.pack(pady=5)

        self.botao1 = tk.Button(self, text="Dobrar", command=self.calcular)
        self.botao1.pack(pady=5)
        
        self.botao2 = tk.Button(self, text="Limpar", command=self.limpar)
        self.botao2.pack(pady=5)
        
        self.resultado1 = tk.Label(self, text="", font=("Arial", 12))
        self.resultado1.pack(pady=5)

    def calcular(self):
        try:
            dobro = int(self.entrada1.get()) * 2
            self.resultado1.config(text=f"{dobro}")
        except ValueError:
            self.resultado1.config(text="Entrada inválida, informe um número.")
    
    def limpar(self):
        self.entrada1.delete(0, tk.END)
        self.resultado1.config(text="")


app = App()
app.mainloop()