def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

def menu():
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

while True:
    menu()
    op = int(input("Informe número da operação desejada: "))
    if op == 1:
        a = int(input("Informe primeiro número: "))
        b = int(input("Informe primeiro número: "))
        print(somar(a,b))
    elif op == 2:
        a = int(input("Informe primeiro número: "))
        b = int(input("Informe primeiro número: "))
        print(subtrair(a,b))
    elif op == 3:
        a = int(input("Informe primeiro número: "))
        b = int(input("Informe primeiro número: "))
        print(multiplicar(a,b))
    elif op == 4:
        a = int(input("Informe primeiro número: "))
        b = int(input("Informe primeiro número: "))
        if a == 0 or b == 0:
            print("Não é possível dividir por 0.")
        else:
            print(dividir(a,b))
    elif op == 5:
        print("Encerrando programa.")
        break
    else:
        print("Comando desconhecido, tente novamente.")