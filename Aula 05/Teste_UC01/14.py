n1 = int(0)
n2 = int(0)
res = int(0)
option = ""

while True:
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Sair")
    option = input("\nDigite o número da operação que deseja realizar: ")

    if option == "1":
        n1 = int(input("\nInforme o primeiro número: "))
        n2 = int(input("\nInforme o segundo número: "))
        res = n1 + n2
        print(f"\n{n1} + {n2} = {res}")
    elif option == "2":
        n1 = int(input("\nInforme o primeiro número: "))
        n2 = int(input("\nInforme o segundo número: "))
        res = n1 - n2
        print(f"\n{n1} - {n2} = {res}")
    elif option == "3":
        n1 = int(input("\nInforme o primeiro número: "))
        n2 = int(input("\nInforme o segundo número: "))
        res = n1 * n2
        print(f"\n{n1} * {n2} = {res}")
    elif option == "4":
        print("\nEncerrando o programa")
        break
    else:
        print("\nComando desconhecido, informe novamente.")
    print("\n")
