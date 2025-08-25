numero1 = int(input("Digite o número inicial: "))
numero2 = int(input("Digite o número final: "))

for i in range(numero1 , numero2 + 1):  # +1 porque o range não inclui o último valor
    print(i)