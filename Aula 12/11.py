temp = input("Informe temperatura em celsius: ")
try:
    temp = float(temp)
    print(f"Temperatura em Fahrenheit: {(temp * 9/5) +32}")
except ValueError:
    print("Valor informado deve ser númerico.")