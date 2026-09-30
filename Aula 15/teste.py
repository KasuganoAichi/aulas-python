try:
    numero = int(input('Digite um número: '))
    resultado = 10 / numero
except ValueError:
    print('Isso não é um número válido!')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')