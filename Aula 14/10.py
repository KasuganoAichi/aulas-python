import tkinter as tk
from tkinter import ttk, messagebox


def inscrever():
    nome = entrada_nome.get().strip()
    idade_texto = entrada_idade.get().strip()
    curso_selecionado = curso.get()
    turno_selecionado = turno.get()

    if not nome or not idade_texto:
        messagebox.showwarning("Atenção", "Preencha o nome e a idade.")
        return

    try:
        idade = int(idade_texto)
    except ValueError:
        messagebox.showwarning("Atenção", "A idade deve ser numérica.")
        return

    if not termo.get():
        messagebox.showwarning(
            "Atenção",
            "Confirme os dados antes de se inscrever."
        )
        return

    resumo = (
        f"Nome: {nome}\n"
        f"Idade: {idade}\n"
        f"Curso: {curso_selecionado}\n"
        f"Turno: {turno_selecionado}\n"
        "Dados confirmados: Sim"
    )

    messagebox.showinfo("Inscrição realizada", resumo)


janela = tk.Tk()
janela.title("Formulário de inscrição")
janela.geometry("400x300")

tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=8, sticky="w")
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.grid(row=0, column=1, padx=10, pady=8)

tk.Label(janela, text="Idade:").grid(row=1, column=0, padx=10, pady=8, sticky="w")
entrada_idade = tk.Entry(janela, width=30)
entrada_idade.grid(row=1, column=1, padx=10, pady=8)

tk.Label(janela, text="Curso:").grid(row=2, column=0, padx=10, pady=8, sticky="w")

curso = tk.StringVar(value="Python")
cursos = ["Python", "Java", "JavaScript"]

combo_cursos = ttk.Combobox(
    janela,
    textvariable=curso,
    values=cursos,
    state="readonly",
    width=27
)
combo_cursos.grid(row=2, column=1, padx=10, pady=8)

tk.Label(janela, text="Turno:").grid(row=3, column=0, padx=10, pady=8, sticky="w")

turno = tk.StringVar(value="Manhã")
frame_turnos = tk.Frame(janela)
frame_turnos.grid(row=3, column=1, padx=10, pady=8, sticky="w")

for opcao in ["Manhã", "Tarde", "Noite"]:
    tk.Radiobutton(
        frame_turnos,
        text=opcao,
        variable=turno,
        value=opcao
    ).pack(side="left")

termo = tk.BooleanVar()
tk.Checkbutton(janela,text="Confirmo os dados",variable=termo).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(janela,text="Inscrever",command=inscrever).grid(row=5, column=0, columnspan=2, pady=10)

janela.mainloop()