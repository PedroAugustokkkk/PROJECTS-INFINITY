gastos = []

while True:

    gasto = float(input("Digite o seu gasto: "))

    if gasto == 0.0:
        break

    gastos.append(gasto)


if sum(gastos) <= 50:
    print(f"ECONÔMICO")
elif 50 < sum(gastos) <= 100:
    print(f"MODERADO")
elif sum(gastos) > 100:
    print(f"GASTADOR")
else:
    print(f"Esse gasto não é possível")