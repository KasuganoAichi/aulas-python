import csv

with open("produtos.csv", "w", newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["nome","preço"])
    writer.writerow(["esponja", "3.50"])
    writer.writerow(["bombril", "10.50"])
    writer.writerow(["detergente", "2.50"])

with open("produtos.csv", "r")as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)