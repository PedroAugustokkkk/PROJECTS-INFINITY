# # import math 
# # print(math.sqrt(25))
# # print("escolha escolhas")
# # x = int(input("Digite um número: "))
# # y = int(input("Digite outro número: "))



# # while (x != y):
# #     conta = (x * y)
# #     print(f'Sua multiplicação deu: {conta}')
# #     x = int(input("Digite um número: "))
# #     y = int(input("Digite outro número: "))

# # print("Multiplicação finalizada")   

# # mensagem = "Olá mundo"
# # print(mensagem)

# # nome = "Pedro"
# # idade = 20
# # altura = 1.77
# # cep = "40000-000"
# # casado = False

# # print(f'O seu nome é {nome}, tem {idade} anos, possui altura {altura} metros e mora no CEP {cep}')

# # print(5%2)
# # print(5//2)

# # nome = "Pedrinho"
# # print(nome)
# # nome = input("Digite outro nome: ")
# # print(nome)
# # nome = input("E digite outro nome: ")
# # print(nome)

# # idade1 = int(input("Digite uma idade: "))
# # idade2 = int(input("Digite outra idade: "))

# # if (idade1 == idade2):
# #     print("As idades são iguais")
# # elif (idade1 > idade2):
# #     print("A primeira idade é maior que a segunda")
# # else:
# #     print("A segunda idade é maior que a primeria") 

# # nome1 = input("Digite um nome: ")
# # nome2 = input("Digite outro nome: ")

# # if (nome1 == nome2):
# #     print("Os nomes são iguais")
# # else:
# #     print("Os nomes são diferentes")    










# # print("----------------------------")

# # num1 = int(input("Digite um número: "))


# # if (num1 % 2 == 0):
# #     print("SEU NÚMERO É PAR!")
# # else:
# #     print("SEU NÚMERO É ÍMPAR")

# # print("----------------------------")

# # nota = float(input("Digite a sua nota: "))

# # if (nota >= 6):
# #     print("O ALUNO ESTÁ APROVADO!")
# # else:
# #     print("O ALUNO ESTÁ REPROVADO")

# # print("----------------------------")


# # impares = [1, 3, 5, 7, 9]
# # print(len(impares))


# # def cobrar():
# #     valor = int(input("Que valor você está devendo? "))
# #     return valor


# # cobrar()


# # class Dinheiro:
# #     def extrato():
# #         pass
        
# #     def saidas():
# #         pass
# #     def entradas():
# #         pass
# #     def dividas():
# #         pass
# import time       # Importa o módulo time para usar sleep (pausas)
# import sys        # Importa o módulo sys para manipular a saída no terminal

# # # Lista de números a serem processados
# # lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # # Lista de símbolos usados para simular o "spinner" (carregamento girando)
# # spinner = ['|', '/', '-', '\\']

# # # Para cada número na lista
# # for i in lista:
    
# #     # Loop para mostrar a animação de carregamento (gira o spinner)
# #     for s in spinner:
# #         # Escreve "Calculando" seguido do símbolo atual do spinner na mesma linha
# #         sys.stdout.write(f'\rCalculando {s}')
# #         sys.stdout.flush()  # Força a exibição imediata do texto no terminal
# #         time.sleep(0.1)     # Espera 0.1 segundo entre os frames da animação

# #     # Calcula o resultado multiplicando o número por 1.75
# #     x = i * 1.75

# #     # Escreve o resultado formatado com 2 casas decimais, substituindo a linha anterior
# #     sys.stdout.write('\rResultado: {:.2f}\n'.format(x))

# #     # Espera 1 segundo antes de continuar com o próximo número
# #     time.sleep(1)
# # spinner = ['|', '/', '-', '\\']

# lista = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

# for i in lista:
    
#     if i < 0:
#         print(i)

# lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print("========================================")

# for i in lista1:
#     if i % 2 == 0:
#         print(i)

# C R U D 
# CREATE
# READ
# UPTADE
# DELETE

aluno = {
    "nome": "",
    "idade": int(),
    "nota": int()
}

aluno["nome"] = str(input("Digite o seu nome: "))
aluno["idade"] = int(input("Digite a sua idade: "))
aluno["nota"] = int(input("Digite a sua nota: "))

print(f"Seus dados são {aluno}")
# ye




















