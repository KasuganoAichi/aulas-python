
import tkinter as tk
from tkinter import ttk, messagebox
from modelo import Aluno

class AppCadastro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Cadastro de Alunos")    
        self.geometry("420x450")
        self.alunos = [] # a lista de objetos Aluno (o "banco de dados")
        self.indice_editando = None #indice utilizado para marcar o aluno que está sendo editado
        self.criar_widget()

    def criar_widget(self):
        #Cria a label que contabiliza a quantidade de alunos cadastrados
        self.total_alunos = tk.Label(self, text=f"Total Alunos: {len(self.alunos)}")
        self.total_alunos.grid(row=0,column=1,pady=5, sticky="e")

        #cria a label e entrada para nome do aluno
        tk.Label(self,text="Nome: ").grid(row=1,column=0,padx=10,pady=5,sticky="w")
        self.entrada_nome = tk.Entry(self,width=28)
        self.entrada_nome.grid(row=1,column=1,columnspan=2,padx=10,pady=5)

        #cria a label e entrada para nota do aluno
        tk.Label(self,text="Nota: ").grid(row=2,column=0,padx=10,pady=5,sticky="w")
        self.entrada_nota = tk.Entry(self,width=28)
        self.entrada_nota.grid(row=2,column=1,columnspan=2,padx=10,pady=5)

        #cria a label e combobox com os cursos disponíveis
        tk.Label(self,text="Curso: ").grid(row=3,column=0,padx=10,pady=5,sticky="w")
        opcoes = ["Selecione um Curso", "Administração", "Enfermagem", "Informática"]
        self.entrada_curso = ttk.Combobox(self, values=opcoes, state="readonly")
        self.entrada_curso.grid(row=3,column=1,columnspan=2,padx=10,pady=5)
        self.entrada_curso.current(0) #deixa na primeira opção a combobox

        #cria os botões da parte superior do programa
        tk.Button(self,text="Cadastrar", command=self.cadastrar).grid(row=4,column=1,pady=8, sticky="e")
        tk.Button(self,text="Remover", command=self.remover).grid(row=4,column=2,pady=8, sticky="w")
        tk.Button(self,text="Editar", command=self.editar).grid(row=5,column=1, sticky="e")
        tk.Button(self,text="Limpar Campos", command=self.limpar_campos).grid(row=5,column=2, sticky="w")

        #cria uma caixa de lista que contém a lista de alunos cadastrados
        self.lista_alunos = tk.Listbox(self, width=55, height=12)
        self.lista_alunos.grid(row=6,column=0,columnspan=3,padx=10,pady=5)

        #cria os botões ao final da janela do programa
        tk.Button(self,text="Ordenar por Nome", command=self.ordenar_nome).grid(row=7,column=0,sticky="e")
        tk.Button(self,text="Media Geral", command=self.calcular_media).grid(row=7, column=1,sticky="e")
        tk.Button(self,text="Aprovados/Reprovadas", command=self.calcular_aprovados).grid(row=7, column=2,padx=5,sticky="w")

    #função de cadastro de alunos
    def cadastrar(self):
        nome = self.entrada_nome.get()
        nota_texto = self.entrada_nota.get()
        curso = self.entrada_curso.get()
        #verificações de regras de negócio, garante que as entradas estarão no formato requisitado
        if nome == "" or nota_texto == "" or curso == "Selecione um Curso":
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

        #verifica se algum item está selecionado para edição, se não, segue normalmente
        if self.indice_editando is not None:
            self.alunos[self.indice_editando].nome = nome
            self.alunos[self.indice_editando].nota = nota
            self.alunos[self.indice_editando].curso = curso
            self.indice_editando = None
        else:
            novo_aluno = Aluno(nome, nota, curso)
            self.alunos.append(novo_aluno)

        #limpa os campos de entrada e atualiza a lista de alunos
        self.atualizar_lista()
        self.limpar_campos()

    #função para remover alunos 
    def remover(self):
        selecionado = self.lista_alunos.curselection()

        #verificações de regras de negócios, antes de prosseguir
        if len(self.alunos) == 0:
            messagebox.showerror("Erro", "Não há alunos cadastrados")
            return
        elif not selecionado:
            messagebox.showwarning("Atenção","Selecione um aluno para remover.")
            return
        indice = selecionado[0]
        aluno = self.alunos[indice]

        #exclui aluno da lista de alunos
        if messagebox.askyesno("Confirmar", f"Remover {aluno.nome} ?"):
            self.alunos.pop(indice)
            self.atualizar_lista()

    #função para editar alunos já cadastrados
    def editar(self):
        selecionado = self.lista_alunos.curselection()

        #verificação de regras de negócio, antes de realizar a edição
        if len(self.alunos) == 0:
            messagebox.showerror("Erro", "Não há alunos cadastrados")
            return
        elif not selecionado:
            messagebox.showwarning("Atenção","Selecione um aluno para editar.")
            return

        #armazena indice do aluno escolhido para edição a uma variável global
        indice = selecionado[0]
        aluno = self.alunos[indice]
        self.indice_editando = indice

        #limpa os campos de entrada e altera seus valores para os do aluno selecionado para edição
        self.entrada_nome.delete(0, tk.END)
        self.entrada_nome.insert(0, aluno.nome)

        self.entrada_nota.delete(0, tk.END)
        self.entrada_nota.insert(0, str(aluno.nota))

        self.entrada_curso.set(aluno.curso)

        #mantém o aluno selecionado para melhor identificação
        self.entrada_nome.focus()

    #função que calcula a media geral de todos os alunos cadastrados.
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
            #se não houver alunos cadastrados, apenas envia mensagem de erro
            messagebox.showerror("Erro", "Não há alunos cadastrados.")
            return

    #função que mostra a quantia de alunos aprovados/reprovados  
    def calcular_aprovados(self):
        aprovados = 0
        reprovados = 0
        total_alunos = len(self.alunos)
        if total_alunos > 0:
            for aluno in self.alunos:
                if float(aluno.nota) >= 6:
                    aprovados += 1
                else:
                    reprovados += 1
            messagebox.showinfo("Aprovados/Reprovados", f"Total de Alunos: {total_alunos}\nAprovados: {aprovados}\nReprovados: {reprovados}")
            return
        else:
            #caso não hajam alunos cadastrados, avisa
            messagebox.showerror("Erro", "Não há alunos cadastrados.")
            return

    #função que ordena a lista de alunos por ordem alfabética
    # utiliza-se de funções nativas de Python   
    def ordenar_nome(self):
        self.alunos.sort(key=lambda x: x.nome.lower())
        self.atualizar_lista()

            
    #função que atualiza de alunos, sempre limpando a tela e escrevendo novamente para evitar erros e duplicidade
    def atualizar_lista(self):
        self.lista_alunos.delete(0,tk.END) # limpando a lista visual
        i = 0
        for aluno in self.alunos:
            self.lista_alunos.insert(tk.END,str(aluno))
            if float(aluno.nota) >= 6:
                self.lista_alunos.itemconfig(i, fg="green")
            else:
                self.lista_alunos.itemconfig(i, fg="red")
            i += 1
        self.total_alunos.config(text=f"Total Alunos: {len(self.alunos)}") #atualiza também a quantia de alunos cadastrados
        self.entrada_curso.current(0)

    #função que limpa os campos de entrada e os reseta aos valores padrão
    def limpar_campos(self):
        self.entrada_nome.delete(0,tk.END)
        self.entrada_nota.delete(0,tk.END)
        self.entrada_curso.current(0)
        self.indice_editando = None
        self.entrada_nome.focus()
        self.lista_alunos.select_clear(0)
                        

        
if __name__ == "__main__":
    app = AppCadastro()
    app.mainloop()