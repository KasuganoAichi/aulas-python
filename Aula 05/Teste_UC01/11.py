tries = int(0)

while True:
    senha = input("Digite sua senha: ")
    tries += 1
    if senha == "senac123":
        print("\nLogin Realizado com sucesso!")
        print(f"\nForam realizadas {tries} tentativas de login.")
        break