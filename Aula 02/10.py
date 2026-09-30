while True:
    email = input("Informe e-mail para cadastro: ").strip().lower()
    if "@" in email and email.endswith(".com"):
        print("E-mail cadastrado com sucesso!")
        break
    else:
        print("\nE-mail inválido. Tente novamente.")