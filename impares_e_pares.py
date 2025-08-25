numeros = []
pares = []
impares = []

while True: 

    numero = int(input("Digite um número: "))

    if numero == 0:
        break

    numeros.append(numero)


for i in numeros: 
    if i % 2 == 0: 
        pares.append(i)
    else:
        impares.append(i)

print(f"Esses são os números pares: {pares}")
print()
print(f"Esses são os números ímpares: {impares}")