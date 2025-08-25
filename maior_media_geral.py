numeros = []

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)

for numero in numeros: 
    if numero > media: 
        print(numero)
