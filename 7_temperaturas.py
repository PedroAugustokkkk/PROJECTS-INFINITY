temperaturas = []
cont = 2

while cont < 7:
    temperatura = float(input(f"Digite a temperatura da {cont}a -Feira: "))
    temperaturas.append(temperatura)
    cont += 1

while cont < 8:
    temperatura = float(input(f"Digite a temperatura do sábado: "))
    temperaturas.append(temperatura)
    cont += 1

while cont < 9:
    temperatura = float(input(f"Digite a temperatura da domingo: "))
    temperaturas.append(temperatura)
    cont += 1

temperatura_max = max(temperaturas)
temperatura_min = min(temperaturas)
temperatura_media = sum(temperaturas) / len(temperaturas)


print(f"A maior temperatura dos dias é {temperatura_max}")
print(f"A menor temperatura dos dias é {temperatura_min}")
print(f"A média das temperaturas é {temperatura_media}")
    
