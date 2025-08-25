notas = []

while True:
    nota = float(input("Digite uma nota: "))

    if nota == -1:
        break

    notas.append(nota)

    media = sum(notas) / len(notas)


    
if media >= 6.0: 
        print("TURMA APROVADA")
else: 
        print("TURMA REPROVADA") 