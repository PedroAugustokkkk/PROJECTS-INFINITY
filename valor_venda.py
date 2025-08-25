valores = []
while True: 
    valor = float(input("Digite o valor de venda: "))
    
    if valor == 0.0:
        break

    valores.append(valor)

    if valores:

        maior = max(valores)
        menor = min(valores)
        media = sum(valores) / len(valores)

        print(f"Valores digitados: {valores}")
        print(f"Maior valor: {maior}")
        print(f"Menor valor: {menor}")
        print(f"Média: {media}")

    else:
        print(f"Nenhum valor foi digitado.")

    
