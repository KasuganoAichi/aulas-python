media = float(input("Digite a média do aluno: "))

if media >= 9:
    print(f"Media: {media}, Excelenete")
elif 7 <= media < 9:
    print(f"Media: {media}, Bom")
elif 6 <= media < 7:
    print(f"Media: {media}, Aprovado")
else:
    print(f"Media: {media}, Reprovado")