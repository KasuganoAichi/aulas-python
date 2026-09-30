import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Meu App")
        self.geometry("400x300")
        
        self.criar_widgets()
    
    def criar_widgets(self):
        self.label1 = tk.Label(self, text="Contador", font=("Arial", 14))
        self.label1.pack()
        
        self.botao1 = tk.Button(self, text="Clique Aqui", command=self.aumentar)
        self.botao1.pack(pady=5)
        
        self.resultado1 = tk.Label(self, text="0", font=("Arial", 12))
        self.resultado1.pack(pady=5)

    def aumentar(self):
        x = int(self.resultado1.cget("text")) + 1
        self.resultado1.config(text=x)


app = App()
app.mainloop()