compras = []
produto = ""
option = ""

while True:
    print("\n1 - Adicionar produto a lista.")
    print("2 - Remover produto da lista.")
    print("3 - Mostrar lista completa.")
    print("4 - Sair.")
    option = input("\nInforme número da opção desejada: ")
    if option == "1":
        produto = input("\nInforme nome do produto que deseja incluir: ")
        compras.append(produto)
    elif option == "2":
        if len(compras) == 0:
            print("\nLista vazia, não é possível remover produtos.")
        else:
            produto = input("\nInforme nome do produto que deseja remover: ")
            if produto in compras:
                compras.remove(produto)
                print(f"\n{produto} removido com sucesso.")
            else:
                print(f"\n{produto} não está na lista")
    elif option == "3":
        print(f"\nLista de compras: {compras}")
    elif option == "4":
        print("\nEncerrando programa...")
        break
    else:
        print("\nComando desconhecido, tente novamente.")