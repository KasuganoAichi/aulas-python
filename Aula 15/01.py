import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Meu App")
        self.geometry("400x300")


app = App()
app.mainloop()