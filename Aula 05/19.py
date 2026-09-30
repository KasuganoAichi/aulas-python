import csv

media = float(0)
divisor = float(0)

with open("notas_turma.csv", "r")as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        media += float(line[1])
        divisor += 1

print(f"Média da Turma: {media / divisor}")