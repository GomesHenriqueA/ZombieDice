from Dados import *

# Seleção de Número de Jogadores
numJog = int(input("Insira o Número de Jogadores: "))
listaJog = list()

if numJog < 2:
    print("Número de Jogadores insuficientes!")
else:
    for i in range(numJog):
        listaJog.append(input(f"Jogador N°{i + 1}:"))


def ListaJog():
    print()
    print("=======Jogadores=======")
    print(listaJog)


RolarDados()
