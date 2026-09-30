qtd = int(input("Informe quantas notas irá digitar: "))
media = float(0)

for i in range(1, qtd + 1):
    nota = float(input(f"Digite a {i}ª nota: "))
    media += nota
media = media / qtd

if media >= 6:
    print(f"\nMedia: {media:.2f} - Turma Aprovada.")
else:
    print(f"\nMedia: {media:.2f} - Turma Reprovada.")