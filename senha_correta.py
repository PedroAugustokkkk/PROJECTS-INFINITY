senha = 1234
cont = 0

while True: 
    digitar = int(input("Digite a senha: "))
    if digitar != senha: 
        print("SENHA INCORRETA, TENTE NOVAMENTE")
        cont += 1
    else:
        break

print(f"Você tentou por {cont} vezes")