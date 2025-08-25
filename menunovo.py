alunos = {}

while True:
    menu = input ("""
    1 - cadastrar alunos
    2 - remover alunos 
    3 - lista de alunos 
    4 - sair da lista 
""")

    if menu == "1":
        nome = input ("Digite seu nome: ")

        if nome in alunos: 
            print ("Digite outro nome: ")
        else: 
            nota = input ("Digite sua nota: ")

            alunos [nome] = {
                "nota": nota

            }
        print("USUARIO CADASTRADO COM SUCESSO")
            
    elif menu == "2":
        nome = input ("Digite o nome do usuario que voce deseja remover: ")
        if nome in alunos: 
            confirmacao = input (f"Digite sim para confirmar a remocao de {nome}: ")
            if confirmacao.lower () == "sim":
                pass 
                del alunos [nome]

                print("USUARIO REMOVIDO COM SUCESSO")
            else: 
                print("Remoção cancelada")
        else:
            print("Usuário não encontrado")


    elif menu == "3": 
        if not alunos: 
            print("Nenhum aluno cadastrado.")
        else:
            print("LISTA DE ALUNOS: ")
            for nome, dados in alunos.items():
                print(f"NOME: {dados["nome"]} | NOTA: {dados['nota']}")
    

    elif menu == "4":
        break
    else:
        print("OPÇÃO INVÁLIDA!")

