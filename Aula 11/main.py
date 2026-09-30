# import moedas

# print("Convertento valor de R$100,00 para Doláres: \n")
# print(f"${moedas.real_para_dolar(100):.2f}")

# from moedas import real_para_dolar, real_para_euro, dolar_para_real

# print("Convertento valor de R$100,00 para Doláres: \n")
# print(f"${real_para_dolar(100):.2f}")
# print("Convertento valor de R$100,00 para Euros: \n")
# print(f"${real_para_euro(100):.2f}")
# print("Convertento valor de $100,00 para Reais: \n")
# print(f"${dolar_para_real(100):.2f}")

# from senha_utils import tem_numero

# print(f"A senha 12345 tem números?")
# print(tem_numero("12345"))
# print(f"A senha abcde tem números?")
# print(tem_numero("abcde"))
# print(f"A senha 123ab tem números?")
# print(tem_numero("123ab"))

# import senha_utils as su 

# print(f"A senha 12345 tem números?")
# print(su.tem_numero("12345"))
# print(f"A senha abcde tem números?")
# print(su.tem_numero("abcde"))
# print(f"A senha 123ab tem números?")
# print(su.tem_numero("123ab"))

# ATV 5: Porque ao utilizar o caracter "*", a linguagem entende que você deseja Importar
# todas as funções do modúlo selecionado, lotado a memória RAM desnecessariamente, chamando
# funções para o seu programa que não serão utilizados pelo trecho de código atual e 
# tornando mais difícil sua leitura, por não especificar quais funções estão sendo chamadas.

# import random

# print("Hora da roleta da sorte!")
# print(random.choice(["Nada", "5 pontos", "10 pontos", "Bõnus"]))
# print("Seu número da sorte é: ")
# print(random.randint(1, 100))

# from datetime import date

# print(f"Data de hoje: {date.today()}")
# print(f"Mês atual: {date.today().month}")

# from filme import Filme

# f1 = Filme("Senhor dos Aneis", 240)
# f2 = Filme("Star Wars", 140)
# f3 = Filme("Encanto", 90)

# catalogo = [f1, f2, f3]

# for filme in catalogo:
#     print(f"Título: {filme.titulo}\n Duração: {filme.duracao_min}min\n")

# from funcionario import Funcionario
# from folha_pagamento import Pagamento

# f = Funcionario("Leonardo", "TI")
# p = Pagamento(f, 2500)

# print(f"Funcionario: {p.funcionario.nome}")
# print(f"Cargo: {p.funcionario.cargo}")
# print(f"Salario Bruto: {p.salario}")

# import moedas as m

# print(f"{m.dolar_para_real(200):.2f}")

# from cinema.filme import Filme

# f1 = Filme("Senhor dos Aneis", 240)
# f2 = Filme("Star Wars", 140)
# f3 = Filme("Encanto", 90)

# catalogo = [f1, f2, f3]

# for filme in catalogo:
#     print(f"Título: {filme.titulo}\n Duração: {filme.duracao_min}min\n")

# from cinema.filme import Filme
# from cinema.sessao import Sessao

# f = Filme("Senhor dos Aneis", 240)
# s = Sessao(f, "14:50")

# print("Próxima Sessão: ")
# print(f"Título: {s.filme.titulo}")
# print(f"Duração: {s.filme.duracao_min}min")
# print(f"Horário: {s.horario}")

# from moedas import dolar_para_real #importa somente a função dolar_para_real de moeda.py
# import senha_utils as su #importa o módulo senha_utils.py com o apelido su
# import random #importa a biblioteca nativa de Python Random
# import cinema.filme #importa a classe Filme do pacote cinema

##DESAFIOS

# from conversor.temperatura import fahrenheit_para_celsius, celsius_para_fahrenheit
# from conversor.medidas import pes_para_metros, metros_para_pes

# while (True):
#     print("1 - Converter Celsius para Fahrenheit.")
#     print("2 - Converter Fahrenheit para Celsius.")
#     print("3 - Converter Metros para Pés.")
#     print("4 - Converter Pés para Metros.")
#     print("5 - Sair")
#     option = input("Informe o número da opção desejada: ")
#     if option == "1":
#         valor = input("Informe temperatura em Celsius: ")
#         if valor.isdigit():
#             valor = float(valor)
#             print(f"Convertendo {valor:.1f}°C para Fahrenheit: {celsius_para_fahrenheit(valor):.1f}°F")
#         else:
#             print("Valor informado é inválido, retornando ao menu principal. \n\n")
#     elif option == "2":
#         valor = input("Informe temperatura em Fahrenheit: ")
#         if valor.isdigit():
#             valor = float(valor)
#             print(f"Convertendo {valor:.1f}°F para Celsius: {fahrenheit_para_celsius(valor):.1f}°F")
#         else:
#             print("Valor informado é inválido, retornando ao menu principal. \n\n")
#     elif option == "3":
#         valor = input("Informe a distância em Metros: ")
#         if valor.isdigit():
#             valor = float(valor)
#             print(f"Convertendo {valor:.2f}m para Pés: {metros_para_pes(valor):.2f}ft")
#         else:
#             print("Valor informado é inválido, retornando ao menu principal. \n\n")
#     elif option == "4":
#         valor = input("Informe a distância em Pés: ")
#         if valor.isdigit():
#             valor = float(valor)
#             print(f"Convertendo {valor:.2f}ft para Metros: {pes_para_metros(valor):.2f}m")
#         else:
#             print("Valor informado é inválido, retornando ao menu principal. \n\n")
#     elif option == "5":
#         print("Programa encerrado...")
#         break
#     else:
#         print("Opção desconhecida, informe novamente.")
#         print("\n\n\n")

# import random
# from acervo.livro import Livro
# from acervo.relatorois import mais_antigo, recentes

# acervo = []
# ano = random.randint(0,2026)
# acervo.append(Livro("Senhor dos Aneis: Sociedade do Anel", ano))
# ano = random.randint(0,2026)
# acervo.append(Livro("Senhor dos Aneis: As Duas Torres", ano))
# ano = random.randint(0,2026)
# acervo.append(Livro("Senhor dos Aneis: O Retorno do Rei", ano))
# ano = random.randint(0,2026)
# acervo.append(Livro("Silmarillon ", ano))
# ano = random.randint(0,2026)
# acervo.append(Livro("O Hobbit", ano))

# for item in acervo:
#     print(f"Título: {item.titulo} / Ano: {item.ano}")

# print("O livro mais antigo do acervo é:")
# antigo = mais_antigo(acervo)
# print(f"{antigo.titulo} / Ano: {antigo.ano}")

# lista_recentes = recentes(acervo)

# print("Lista dos livros mais Recentes: ")
# if not lista_recentes:
#     print("Não há livros lançados após 2015 no acervo.")
# else:
#     for item in lista_recentes:
#         print(f"Título: {item.titulo} / Ano: {item.ano}")

import random
from datetime import date
from cassino.historico import Historico
from cassino.roleta import Roleta

h = Historico()
r = Roleta()

for i in range (1, 11):
    h.registrar(r.girar())
    print(f"Rodada {i} Resultado: {h.resultados[i-1]}")

print(f"Maior resultado: {h.maior()}")
print(f"Media dos resultados: {h.media()}")
print(f"Data: {date.today()}")