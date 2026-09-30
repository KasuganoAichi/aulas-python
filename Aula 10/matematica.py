def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if x == 0 or y == 0:
        return "Não é possível realizar a divisão por 0."
    else:
        return x / y

if __name__ == "__main__":
    print(somar(2, 3))