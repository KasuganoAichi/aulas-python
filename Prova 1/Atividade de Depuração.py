#Faltava os ":" para determinar o começo da função
# def saudacao(nome):         
#     print(f"Olá, {nome}!")


#Utilizado "=" que denota valor de variável ao invés de "==" que verifica se os valores são iguais
# idade = 20
# if idade == 18:            
#     print("Tem 18 anos")

    
# #Faltou o termo "self" para que a classe salve o valor corretamente em seu inicializador
# class Gato:
#     def __init__(self, nome):
#         self.nome = nome
#     def miar(self):
#         print(f"{self.nome}: miau")

#Erro de identação, print estava com identação errada e fora do loop
# for i in range(3):
#     print(i)

#Input retorna uma string, é preciso por o mesmo dentro de int() para transformar o valor em int
#somente desta forma o sistema irá realizar o cálculo
# n1 = int(input("Primeiro número: "))
# n2 = int(input("Segundo número: "))
# print(n1 + n2) # deveria mostrar a SOMA dos dois números

# TERMOSTATO (4 erros para corrigir)
# class Termostato:
#     def __init__(self, temperatura=20): #Faltava os ":"
#         self.__temperatura = temperatura
        
#     @property
#     def temperatura(self):          #Faltou o argumento "self" e "__" para permitir o acesso a variável privada da classe
#         return self.__temperatura   
    
#     @temperatura.setter
#     def temperatura(self, valor):
#         if valor >= 10 and valor <= 30:    #Erro de lógica, operadores de comparação invertidos, adicionado "=" as comparações para que
#             self.__temperatura = valor     #10 e 30 tornem-se valores válidos e operador Bool Or utilizado ao invés de and
#         else:
#             print("Temperatura fora do limite (10 a 30)!")
            
#     def aumentar(self):
#         self.temperatura = self.temperatura + 1 #utilizado função aritmética "-" ao invés de "+" para realizar soma
    
#     def modo_economia(self):
#         self.temperatura = 22
#         print("Modo economia ativado")

# t = Termostato()
# print(t.temperatura) # esperado: 20
# t.temperatura = 25 # deve aceitar
# print(t.temperatura) # esperado: 25
# t.temperatura = 50 # deve recusar
# print(t.temperatura) # esperado: 25
# t.modo_economia() #altera temperatura para 22 e ativa modo economia de energia
# print(t.temperatura) #esperado: 22

# RPG (4 erros para corrigir)
# class Personagem:
#     def __init__(self, nome, vida):
#         self.nome = nome
#         self.vida = vida
        
#     def atacar(self):
#         print(f"{self.nome} ataca!")
        
#     def status(self):
#         print(f"{self.nome} - Vida: {self.vida}")  #Faltou o argumento "self" no começo da variável vida
        
# class Guerreiro(Personagem):    #Faltou o caracter ":" no fim da linha para denotar o início da função
#     def __init__(self, nome, vida, forca):
#         super().__init__(nome, vida)  #Faltou passar a variável vida ao super construtor
#         self.forca = forca
        
#     def atacar(self):           #Erro de digitação, foi escrito "atcar" ao invés de "atacar"
#         print(f"{self.nome} ataca com espada! Força: {self.forca}")
    
#     #Adicionado "força" a apresentação de status do personagem
#     def status(self):
#             print(f"{self.nome} - Vida: {self.vida} - Força: {self.forca}")
    
# class Mago(Personagem):
#     def __init__(self, nome, vida, mana):
#         super().__init__(nome, vida)
#         self.mana = mana
    
#     def atacar(self):
#         print(f"{self.nome} lança uma bola de fogo!")
    
#     #Adicionado "mana" a apresentação de status do personagem
#     def status(self):
#         print(f"{self.nome} - Vida: {self.vida} - Mana: {self.mana}")
    
        
# heroi = Guerreiro("Thor", 100, 50)
# heroi.atacar() # esperado: ataque especial com a força
# heroi.status() # esperado: Thor - Vida: 100
# heroi2 = Mago("Loki", 25, 100)
# heroi2.atacar() # esperado: ataque com bola de fogo
# heroi2.status() # esperado Loki - Vida: 25 - Mana: 100

# EXPORTADORES (4 erros para corrigir)
class ExportadorPDF:
    def exportar(self, dados):
        print(f"Exportando '{dados}' para PDF") #exportador de PDF estava com frase referenciando arquivo CSV
    
class ExportadorCSV:
    def exportar(self, dados):      #Nome da função estava diferente das demais, sendo tratada como algo completamente diferente
        print(f"Exportando '{dados}' para CSV") #e sem uso de polimorfismo

class ExportadorTXT:
    def exportar(self, dados):     #Inicialmente não foi passado "self" para a função
        print(f"Exportando '{dados}' para TXT")
        
class ExportadorJSON:
    def exportar(self, dados):     
        print(f"Exportando '{dados}' para JSON")
        
def exportar_tudo(exportadores, dados):  #ausência do carácter ":" ao final da linha
    for exp in exportadores:
        exp.exportar(dados)

lista = [ExportadorPDF(), ExportadorCSV(), ExportadorTXT(), ExportadorJSON()]
exportar_tudo(lista, "Relatório de vendas")
