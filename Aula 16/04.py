
import tkinter as tk
from tkinter import ttk, messagebox

class Aluno:
    def __init__ (self,nome,nota):
        self.nome = nome
        self.nota = nota

    def situacao(self):
        return "Aprovado" if self.nota >= 6 else "Reprovado"

    def __str__(self): #m etodo especial
        #como o aluno aparece como texto na Listbox
        return f"{self.nome} - Nota: {self.nota} ({self.situacao()})"






class AppCadastro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Cadastro de Alunos")    
        self.geometry("420x400")
        self.alunos = [] # a lista de objetos Aluno (o "banco de dados")  
        self.criar_widget()

    def criar_widget(self):
        self.total_alunos = tk.Label(self, text=f"Total Alunos: {len(self.alunos)}")
        self.total_alunos.grid(row=0,column=1,pady=5, sticky="e")
        tk.Label(self,text="Nome: ").grid(row=1,column=0,padx=10,pady=5,sticky="w")
        self.entrada_nome = tk.Entry(self,width=28)
        self.entrada_nome.grid(row=1,column=1,columnspan=2,padx=10,pady=5)

        tk.Label(self,text="Nota: ").grid(row=2,column=0,padx=10,pady=5,sticky="w")
        self.entrada_nota = tk.Entry(self,width=28)
        self.entrada_nota.grid(row=2,column=1,columnspan=2,padx=10,pady=5)

        tk.Button(self,text="Cadastrar", command=self.cadastrar).grid(row=3,column=1,pady=8, sticky="e")
        tk.Button(self,text="Remover", command=self.remover).grid(row=3,column=2,pady=8, sticky="w")
        tk.Button(self,text="Limpar Campos", command=self.limpar_campos).grid(row=4,column=1,columnspan=2)

        self.lista_alunos = tk.Listbox(self, width=55, height=12)
        self.lista_alunos.grid(row=5,column=0,columnspan=3,padx=10,pady=5)
        
        tk.Button(self,text="Media Geral", command=self.calcular_media).grid(row=6, column=1)

    def cadastrar(self):
        nome = self.entrada_nome.get()
        nota_texto = self.entrada_nota.get()

        if nome == "" or nota_texto == "":
            messagebox.showwarning("Erro","Todos os campos devem preenchidos.")
            return
        try:
            nota = float(nota_texto)
        except ValueError:
            messagebox.showerror("Erro","A nota deve ser um número.")
            return
        if nota < 0 or nota > 10:
            messagebox.showerror("Erro","A nota deve estar entre 0 e 10.")
            return

        novo_aluno = Aluno(nome,nota)
        self.alunos.append(novo_aluno)
        self.total_alunos.config(text=f"Total Alunos: {len(self.alunos)}")
        self.atualizar_lista()
        self.limpar_campos()
        
    def remover(self):
        selecionado = self.lista_alunos.curselection()
        if len(self.alunos) == 0:
            messagebox.showerror("Erro", "Não há alunos cadastrados")
            return
        elif not selecionado:
            messagebox.showwarning("Atenção","Selecione um aluno para remover.")
            return
        indice = selecionado[0]
        aluno = self.alunos[indice]
        if messagebox.askyesno("Confirmar", f"Remover {aluno.nome} ?"):
            self.alunos.pop(indice)
            self.total_alunos.config(text=f"Total Alunos: {len(self.alunos)}")
            self.atualizar_lista()

    def calcular_media(self):
        media = 0
        total_alunos = len(self.alunos)
        if total_alunos > 0:
            for aluno in self.alunos:
                media += float(aluno.nota)
            media = media / total_alunos
            messagebox.showinfo("Media", f"Media Geral: {media:.2f}")
            return
        else:
            messagebox.showerror("Erro", "Não há alunos cadastrados.")
            

    def atualizar_lista(self):
        self.lista_alunos.delete(0,tk.END) # limpando a lista visual
        for aluno in self.alunos:
            self.lista_alunos.insert(tk.END,str(aluno))

    def limpar_campos(self):
        self.entrada_nome.delete(0,tk.END)
        self.entrada_nota.delete(0,tk.END)   
        self.entrada_nome.focus()
        self.lista_alunos.select_clear(0)
                        

        
app = AppCadastro()
app.mainloop() 