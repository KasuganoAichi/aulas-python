import csv

pecas = [["Peça", "Preço"], ["Monitor Ultrawide", 2500], ["Teclado Mecânico", 350]]

with open("hardware.csv", "w", newline="")as file:
    writer = csv.writer(file)
    for line in pecas:
        writer.writerow(line)