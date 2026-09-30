def ler_nota_valida():
    while True:
        nota = input("Informe uma nota de 0 a 10: ")
        try:
            nota = int(nota)
            if nota < 0 or nota > 10:
                raise ValueError("A nota deve estar entre 0 e 10.")
            print(f"Nota: {nota}")
            break
        except ValueError as erro:
            print(f"\n{erro}")

ler_nota_valida()