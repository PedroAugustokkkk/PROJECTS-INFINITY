# MENU DE CADASTRO

users = {}

def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def formatar_telefone(telefone):
    return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"



while True: 
    menu = int(input(
    """====================
MENU DE CADASTRO
===================
[1] CADASTRAR CLIENTE
[2] REMOVER CLIENTE
[3] LISTAR CLIENTES
[4] SAIR
    """
))
    
    

    if menu == 1:
        
        while True: 
            cpf = input("Digite o CPF do cliente a ser cadastrado: ")
            if cpf.isdigit() and len(cpf) == 11: 
                cpf = formatar_cpf(cpf)
                break
            else: 
                print("CPF inválido! Precisa conter 11 números (ex: 10000012345)")
        if cpf in users:
            print("Usuário já cadastrado! Tente novamente")
        else:
            nome = input("Digite o nome do usuário: ")
            
            while True:
                email = input("Digite o e-mail do usuário: ") 
                if "@" and "." in email:
                    break
                else:
                    print("E-mail inválido! Precisa conter '@' e '.' ")
            
            while True:        
                telefone = input("Digite o número de telefone do usuário: ")
                if telefone.isdigit() and len(telefone) == 11:
                    telefone = formatar_telefone(telefone)
                    break
                else: 
                    print("Telefone inválido! Digite 11 números (ex: 71999990000)")
                    
                    
            users[cpf] = {
                "nome": nome,
                "email": email,
                "telefone": telefone
            }
            print("Cliente cadastrado com sucesso!")
    
    
    
    elif menu == 2: 
        cpf = input("Digite o CPF do usuário a ser removido: ")
        if cpf in users: 
            confirmacao = input("Tem certeza que deseja remover o cliente digitado? [s/n]")
            if confirmacao.lower() == "s":
                del users[cpf]
                print("Usuário removido com sucesso!")
            else: 
                print("Remoção cancelada") 
        else: 
            print("Usuário não encontrado.")
    
    
    
    elif menu == 3: 
        if not users: 
            print("Nenhum cliente cadastrado.")
        else:
            print("LISTA DE CLIENTES: ")
            for cpf, dados in users.items():
                print(f"CPF: {cpf} | NOME: {dados['nome']} | E-MAIL: {dados['email']} | TELEFONE: {dados['telefone']}")
    
    
    
    elif menu == 4: 
        break
    
    
    
    else:  
        print("Opção inválida, tente novamente!")         


print(users)