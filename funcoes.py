def parabens ():
    print("Parabéns pra você")

parabens()


def saudacao():
    print("Seja bem-vindo ao sistema, Cauê")

saudacao()

def preco_coxinha():
    print("Coxinha - R$2,00")

preco_coxinha()

def numero():
    print("12 é número")

numero()

def parabens(nome):
    print(f"Parabéns para você! {nome}")

parabens("Pedrinho")

def perfil(nome, idade:int):
    print(f"Seu nome é {nome} e sua idade é {idade}")

perfil("Pedro", 20)


def tabela_precos(preco1:float, preco2:float):
    print(f"Coxinha - R${preco1}")
    print(f"Empada - R${preco2}")

tabela_precos(2.50, 3.80)

def envelhecer(idade):
    print(f"Você ficou um ano mais velho, agora tem {idade} anos")

envelhecer(90)

def configuracoes(marca, modelo, preco, status):
    print(f"MARCA: {marca}")
    print(f"MODELO: {modelo}")
    print(f"PREÇO: {preco}")
    print(f"STATUS: {status}")
