def cadastrar_aluno(nome, idade):
    if not nome.strip():
        raise ValueError("O nome não pode ficar em branco.")

    if idade <= 0 or idade >= 120:
        raise ValueError("Idade inválida para cadastro.")

    return {"nome": nome, "idade": idade}


nome = input("Informe o nome do aluno: ")
idade = int(input("Informe a idade do aluno: "))

try:
    aluno = cadastrar_aluno(nome, idade)
    print(f"Aluno cadastrado: {aluno['nome']}, {aluno['idade']} anos.")
except ValueError as erro:
    print(erro)