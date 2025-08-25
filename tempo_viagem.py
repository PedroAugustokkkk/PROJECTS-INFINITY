distancia = float(input("Qual é a distância da viagem? (em km): "))
velocidade = float(input("Digite a qual velocidade você irá viajar: "))

tempo = distancia / velocidade

if tempo < 1: 
    print(f"O tempo de viagem é {tempo} e é CURTO")
elif 1 < tempo < 6:
    print(f"Seu tempo de viagem é {tempo} e é MÉDIO")
else: 
    print(f"Seu tempo de viagem é {tempo} e LONGO")

