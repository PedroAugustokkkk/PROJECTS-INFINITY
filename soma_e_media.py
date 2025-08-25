# TESTE
numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

print(f"Números digitados: {numeros}")
print(f"Soma = {soma}")
print(f"Média = {media}")
