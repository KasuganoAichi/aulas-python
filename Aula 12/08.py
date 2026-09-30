while True:
    try:
        idade = int(input("Informe sua idade: "))
        break
    except ValueError:
        print("\n Valor deve ser um número.")
print(f"\nSua idade é: {idade}")