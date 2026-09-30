while True:
    dados = input("Informe email, nome e idade separados por vírgula: ").strip()
    email, nome, idade = dados.split(",")
    email.lower().strip()
    nome.title().strip()
    idade.strip()

    if "@" in email and email.endswith(".com"):
        print(f"{nome} de {idade} anos, seu cadastro foi concluído!")
        break
    else:
        print("Email inválido")