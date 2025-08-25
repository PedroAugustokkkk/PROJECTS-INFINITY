idades = []

for i in range (1, 6):
    idade = int(input("Digite uma idade: "))
    idades.append(idade)


maior = max(idades)
menor = min(idades)
media = sum(idades) / len(idades)

print(f"A maior idade é: {maior}")
print(f"A menor idade é: {menor}")
print(f"A média de idades é: {media}")