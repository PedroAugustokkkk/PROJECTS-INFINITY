convidados = []

while True: 
    convidado = str(input("Digite um convidado: "))

    if convidado.lower() == "sair":
        break

    convidados.append(convidado)

print(f"A lista de convidados é {convidados}")
