codigo = input("Informe um código de produto: ").upper().strip()

if codigo.startswith("BR-"):
    if codigo[3:].isalnum():
        print(f"O código {codigo} é válido.")
    else:
        print("Código inválido")
else:
    print("Código inválido")