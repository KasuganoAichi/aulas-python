import tkinter as tk
from tkinter import messagebox


class BotaoCadastrar(tk.Button):
	def __init__(self, master, command):
		super().__init__


class AppCadastro(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Cadastro de pessoas")
		self.geometry("400x300")
		self.pessoas = []

		self.criar_widgets()

	def criar_widgets(self):
		self.label1 = tk.Label(self, text="Nome:")
		self.label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
		self.entrada_nome = tk.Entry(self)
		self.entrada_nome.grid(row=0, column=1, padx=5, pady=5)

		self.label2 = tk.Label(self, text="Idade:")
		self.label2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
		self.entrada_idade = tk.Entry(self)
		self.entrada_idade.grid(row=1, column=1, padx=5, pady=5)

		self.botao_cadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrar)
		self.botao_cadastrar.grid(row=2, column=0, columnspan=2, pady=5)

		self.lista = tk.Label(self, text="Nenhuma pessoa cadastrada.", justify="left")
		self.lista.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="w")

	def cadastrar(self):
		nome = self.entrada_nome.get().strip()

		if not nome:
			messagebox.showerror("Erro", "Nome é obrigatório.")
			return

		try:
			idade = int(self.entrada_idade.get())
			if idade < 0:
				raise ValueError("Idade não pode ser inferior a 0.")
		except ValueError as erro:
			messagebox.showerror("Erro", str(erro) or "Informe uma idade válida.")
			return

		self.pessoas.append((nome, idade))
		self.atualizar_lista()
		self.entrada_nome.delete(0, tk.END)
		self.entrada_idade.delete(0, tk.END)

	def atualizar_lista(self):
		pessoas = "\n".join(
			f"{indice}. {nome} - {idade} anos"
			for indice, (nome, idade) in enumerate(self.pessoas, start=1)
		)
		self.lista.config(text=f"Pessoas cadastradas:\n{pessoas}")


app = AppCadastro()
app.mainloop()