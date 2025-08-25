import random # BIBLIOTECA PARA VALORES ALEATÓRIOS

# O computador escolhe um número entre 1 e 100
numero_secreto = random.randint(1, 100)

tentativas = 0

print("Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

while True:
    chute = int(input("Digite seu palpite: "))
    tentativas += 1

    if chute < numero_secreto:
        print("Muito baixo. Tente novamente.")
    elif chute > numero_secreto:
        print("Muito alto. Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break
