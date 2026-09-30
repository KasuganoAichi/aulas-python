lista = ['Turtwig', 'Chimchar', 'Piplup']

index = int(input("Informe índice que deseja acessar: "))

try:
    print(lista[index])
except IndexError:
    print(f"{index} fora do alcance da lista.")
except ValueError:
    print("Você deve informar um número inteiro.")