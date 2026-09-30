meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

mes = input("Informe número do mês desejado: ")

try:
    mes = int(mes) - 1
    print(f"{meses[mes]}")
except ValueError:
    print("Valor informado deve ser um número inteiro.")
except IndexError:
    print("Valor informado deve estar entre 1 e 12.")