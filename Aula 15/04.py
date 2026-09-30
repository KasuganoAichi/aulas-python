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
        
        self.label2 = tk.Label(self, text="Informe seu nome.", font=("Arial", 14))
        self.label2.pack(pady=5)

        self.entrada1 = tk.Entry(self)
        self.entrada1.pack(pady=5)

        self.botao1 = tk.Button(self, text="Clique Aqui", command=self.saudar)
        self.botao1.pack(pady=5)
        
        self.resultado1 = tk.Label(self, text="", font=("Arial", 12))
        self.resultado1.pack(pady=5)

    def saudar(self):
        self.resultado1.config(text=f"Olá, {self.entrada1.get()}")


app = App()
app.mainloop()