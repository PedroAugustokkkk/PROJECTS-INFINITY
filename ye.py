# PROGRAMA QUE MONTA UM CARDÁPIO SEMANAL

# BIBLIOTECAS
import random # Biblioteca para escolher aleatoriamente um item (nesse caso um alimento)
import time # Biblioteca para fazer um delay no programa
import json  # Biblioteca para salvar e carregar os dados em arquivo

# Caminho do arquivo onde os dados serão salvos
ARQUIVO_DADOS = 'cardapio.json' # Variavel que armazena um arquivo de armazenamento (para guardarmos os dados dos alimentos colocados pelo usuário)

# Função para carregar os dados do arquivo JSON, se existir
def carregar_dados(): # Função em si
    try: # Tipo um IF
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f: # Tente abrir um arquivo e ler 'r' - read - ler
            return json.load(f)  # Retorna o dicionário carregado
    except FileNotFoundError: # Se o arquivo nao existe, executa o bloco:
        return {  # Se não existir, retorna dicionário vazio
            "carboidrato": [],
            "proteina": [],
            "salada": [],
            "sobremesa": [],,
            "leguminosa": []
        }

# Função para salvar os dados no arquivo JSON
def salvar_dados(comida): # Função em si com o parametro comida (dicionario)
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f: # Tenta abrir o arquivo em modo de escrever 'w' - write - escrever
        json.dump(comida, f, ensure_ascii=False, indent=4)  # Salva o dicionário formatado

# Função que carrega os dados ao iniciar o programa
comida = carregar_dados() 

# Referências para as listas dentro do dicionário comida
carboidratos = comida["carboidrato"] # comida é o dicionario, que pega o item carboidrato e salva na variavel carboidratos, e assim por diante
proteinas = comida["proteina"]
saladas = comida["salada"]
sobremesas = comida["sobremesa"]
leguminosas = comida["leguminosa"] 

# ESTRUTURA DE REPETIÇÃO PRINCIPAL COM MENU

while True:
    menu = int(input("""
 _________________________________________________________________
|  BEM VINDO AO GERADOR DE CARDÁPIOS! A SUA SOLUÇÃO NUTRICIONAL   | 
|                   O QUE DESEJA FAZER?                           |
|=================================================================|
|[1] - Adicionar Alimentos                                        |
|[2] - Listar Cardápios                                           |
|[3] - Deletar                                                    |
|[4] - Sair                                                       |
|_________________________________________________________________|
            Informe o número da opção desejada: \n""")) # menu basico principa
    if menu == 1:
        while True:
            menu = int(input("""
 _________________________________________________________________
|            Informe qual alimento deseja adicionar:              |
|=================================================================|
|[1] - Carboidrato                                                |
|[2] - Leguminosa                                                 |
|[3] - Proteína                                                   |
|[4] - Salada                                                     |
|[5] - Sobremesa                                                  |
|[6] - Sair                                                       |
|_________________________________________________________________|
            Informe o número da opção desejada: \n""")) # menu secundario para adição dos diferentes tipos de alimentos/nutrientes
            if menu == 1:
                # Pede o nome do carboidrato e adiciona na lista
                alimento = input("Digite o nome do carboidrato: ") # aqui é o input, salvo em alimento
                carboidratos.append(alimento.lower()) # adiciona o alimento (em letra minuscula para verificações futuras) na lista de carboidratos e com append (um em seguida do outro)
                print("Adicionando carboidrato. Por favor, aguarde... ") # printa uma mensagem para a pessoa saber que estamos adicionando o que ela digitou
                time.sleep(1.5) # delay pra gerar uma ansiedade no usuario (leia-se expectativa)
                print(f"Carboidrato '{alimento}' adicionado com sucesso!") # imprime a mensagem de que o alimento x foi adicionado
            elif menu == 2:
                # Pede o nome da proteína e adiciona na lista
                alimento = input("Digite o nome da proteína: ")
                leguminosas.append(alimento.lower())
                print("Leguminosa sendo inserida no cardápio... ")
                time.sleep(1.5)
                print(f"Leguminosa: '{alimento}' adicionada com sucesso!")
            elif menu == 3:
                # Pede o nome da salada e adiciona na lista
                alimento = input("Digite o nome da salada: ")
                proteinas.append(alimento.lower())
                print("Opa! Estamos adicionando a proteína informada... ")
                time.sleep(1.5)
                print(f"Salada: '{alimento}' adicionada com sucesso!")
            elif menu == 4:
                # Pede o nome da sobremesa e adiciona na lista
                alimento = input("Digite o nome da sobremesa: ")
                saladas.append(alimento.lower())
                print("A salada está sendo adicionada ao cardápio, aguarde um momento... ")
                time.sleep(1.5)
                print(f"Salada: '{alimento}' adicionada com sucesso!")
            elif menu == 5:
                # Pede o nome da sobremesa e adiciona na lista
                alimento = input("Digite o nome da sobremesa: ")
                sobremesas.append(alimento.lower())
                print("Estamos adicionando a sobremesa, por favor aguarde... ")
                time.sleep(1.5)
                print(f"Sobremesa '{alimento}' adicionada com sucesso!")
            elif menu == 6:
                break # quebramos o laço/loop do while do menu secundario
            else:
                print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE!") # caso a anta do usuario digite um numero invalido, tipo 87
    
    elif menu == 2:
        # random.choice é uma funcao da bibliote random que justamente escolhe aleatoriamente um item de uma lista indicada (por parenteses)
        # fazemos esse random.choice para cada tipo de alimento, já que essa é a ideia do programa: gerar listar aleatorias de alimentos/dietas para o usuario
        print(f"""
        SEGUNDA-FEIRA: 
        Carboidrato: {random.choice(carboidratos)}
        Leguminosa: {random.choice(leguminosas)} 
        Proteina: {random.choice(proteinas)}
        Salada: {random.choice(saladas)}
        Sobremesas: {random.choice(sobremesas)} 

        TERÇA-FEIRA: 
        Carboidrato: {random.choice(carboidratos)}
        Leguminosa: {random.choice(leguminosas)} 
        Proteina: {random.choice(proteinas)}
        Salada: {random.choice(saladas)}
        Sobremesas: {random.choice(sobremesas)} 

        QUARTA-FEIRA: 
        Carboidrato: {random.choice(carboidratos)}
        Leguminosa: {random.choice(leguminosas)} 
        Proteina: {random.choice(proteinas)}
        Salada: {random.choice(saladas)}
        Sobremesas: {random.choice(sobremesas)} 

        QUINTA-FEIRA: 
        Carboidrato: {random.choice(carboidratos)}
        Leguminosa: {random.choice(leguminosas)}
        Proteina: {random.choice(proteinas)}
        Salada: {random.choice(saladas)}
        Sobremesas: {random.choice(sobremesas)} 

        SEXTA-FEIRA: 
        Carboidrato: {random.choice(carboidratos)}
        Leguminosa: {random.choice(leguminosas)}
        Proteina: {random.choice(proteinas)}
        Salada: {random.choice(saladas)}
        Sobremesas: {random.choice(sobremesas)} 

        SÁBADO: 
        Carboidrato: {random.choice(carboidratos)}
        Leguminosa: {random.choice(leguminosas)}
        Proteina: {random.choice(proteinas)}
        Salada: {random.choice(saladas)}
        Sobremesas: {random.choice(sobremesas)} 

        DOMINGO: 
        Carboidrato: {random.choice(carboidratos)}
        Leguminosa: {random.choice(leguminosas)}
        Proteina: {random.choice(proteinas)}
        Salada: {random.choice(saladas)}
        Sobremesas: {random.choice(sobremesas)} 
        """)  
        
    elif menu == 3:
        # menu terceario para deletar alimento, com uma logica parecida de adicionar, porem com o metodo remove
        menu = int(input("""
 _________________________________________________________________
|            Informe qual alimento deseja deletar:                |
|=================================================================|
|[1] - Carboidrato                                                |
|[2] - Leguminosa                                                 |
|[3] - Proteína                                                   |
|[4] - Salada                                                     |
|[5] - Sobremesa                                                  |
|[6] - Sair                                                       |
|_________________________________________________________________|
            Informe o número da opção desejada: \n"""))
        if menu == 1:
            print(carboidratos)
            alimento = input("Digite o nome do carboidrato que deseja deletar: ") # pede o usuario que alimento deseja deletar
            if alimento.lower() in carboidratos: # verifica se esse alimento (em letras minuscular por conta do metodo .lower()) ESTÁ na lista carboidratos
                carboidratos.remove(alimento)
                print("Removendo carboidrato, aguarde...\n")
                time.sleep(1) # se estiver, ele remove esse alimento digitado
                print(f"Carboidrato '{alimento}' removido!") # e imprime essa mensagem
            else:
                print(f"Carboidrato '{alimento}' não encontrado na lista.")
        elif menu == 2:
            print(leguminosas)
            alimento = input("Digite o nome da proteína que deseja deletar: ")
            if alimento.lower() in leguminosas:
                leguminosas.remove(alimento)
                print("Removendo proteína, aguarde...\n")
                time.sleep(1)
                print(f"Leguminosa '{alimento}' removida!")
            else:
                print(f"Leguminosa '{alimento}' não encontrada na lista.") # caso contrario, quer dizer que o alimento nao foi encontrado na lista
        elif menu == 3:
            print(proteinas)
            alimento = input("Digite o nome da proteína que deseja deletar: ")
            if alimento.lower() in proteinas:
                proteinas.remove(alimento)
                print("Removendo carboidrato, aguarde...\n")
                time.sleep(1)
                print(f"Proteína '{alimento}' removida!")
            else:
                print(f"Proteína '{alimento}' não encontrada na lista.")
        elif menu == 4: 
            print(saladas)
            alimento = input("Digite o nome da salada que deseja deletar: ")
            if alimento.lower() in saladas:
                saladas.remove(alimento)
                print("Removendo salada, aguarde...\n")
                time.sleep(1)
                print(f"Salada '{alimento}' removida!")
            else:
                print(f"Salada '{alimento}' não encontrada na lista.") 
        elif menu == 5:
            print(sobremesas)
            alimento = input("Digite o nome da sobremesa que deseja deletar: ")
            if alimento.lower() in sobremesas:
                sobremesas.remove(alimento)
                print("Removendo sobremesa, aguarde...\n")
                time.sleep(1)
                print(f"Sobremesa '{alimento}' removida!")
            else:
                print(f"Sobremesa '{alimento}' não encontrada na lista.") 
        elif menu == 6:
            break
        else:
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE!")     
    
    elif menu == 4:
        salvar_dados(comida)  # Chama a função criada lá em cima para salvar os dados no arquivo .json
        print("Dados salvos com sucesso! Saindo...")
        break # sair
        
    else: 
        print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE!") # caso a anta do usuario digite um numero invalido, tipo 87

print(carboidratos)
print(leguminosas)
print(proteinas)
print(saladas)
print(sobremesas)

# def adicionarAlimento():
#     carboidrato = input("Informe o nome do carboidrato que deseja adicionar: ")
#     proteina = input("Informe qual proteína deseja adicionar: ")
#     salada = input("Informe qual salada deseja adicionar: ")
#     sobremesa = input("Informe qual sobremesa deseja adicionar: ")
    
# def criarCardapio():
#     name = input("Dê um nome para o novo cardápio: ")
#     novo_cardapio = {}
# cardapios = {
#     "cardapio 1"
#         "carboidratoCard": []
#         "proteinaCard": []
#         "saladaCard": []
#         "sobremesaCard": []    
# }