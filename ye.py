# print("print")
# #aaaaaaaaaaaaaaaaaaaaa
# #yea



# PROGRAMA QUE MONTA UM CARDÁPIO SEMANAL
import random
import time

carboidratos = []
proteinas = []
saladas = []
sobremesas = []

comida = {
    "carboidrato": carboidratos,
    "proteina": proteinas,
    "salada": saladas,
    "sobremesa": sobremesas
}

cardapios = {
    "cardapio 1"
        "carboidratoCard": []
        "proteinaCard": []
        "saladaCard": []
        "sobremesaCard": []    
}



while True:
    menu = int(input('''
Digite qual item você deseja adicionar ou veja o cardápio:

[1] - Carboidratos
[2] - Proteínas
[3] - Salada
[4] - Sobremesa
[5] - Cardápio
[6] - Sair
'''))
    
    if menu == 1:
        adicionarAlimento(carboidrato)
    
    elif menu == 2:
        adicionarAlimento(proteina)
    
    elif menu == 3:
        adicionarAlimento(salada)
    
    elif menu == 4:
        adicionarAlimento(sobremesa)
    
    elif menu == 5:
        print(f"""
SEGUNDA-FEIRA: {comida.random} 
TERÇA-FEIRA: {comida.random}
QUARTA-FEIRA: {comida.random}
QUINTA-FEIRA: {comida.random}
SEXTA-FEIRA: {comida.random}
SÁBADO: {comida.random}
DOMINGO: {comida.random}
""")
        
    elif menu == 6:
        break
    else: 
        print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE!")



def adicionarAlimento():
    carboidrato = input("Informe o nome do carboidrato que deseja adicionar: ")
    proteina = input("Informe qual proteína deseja adicionar: ")
    salada = input("Informe qual salada deseja adicionar: ")
    sobremesa = input("Informe qual sobremesa deseja adicionar: ")
    
def criarCardapio():
    name = input("Dê um nome para o novo cardápio: ")
    novo_cardapio = {}