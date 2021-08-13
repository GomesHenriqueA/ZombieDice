import random


# Faces dos dados -C = Cérebro -P = Pegadas -T = Tiro
verde = ["C", "P", "C", "T", "P", "C"]  # 6 Dados
amarelo = ["T", "P", "C", "T", "P", "C"]  # 4 Dados
vermelho = ["T", "P", "T", "C", "P", "T"]  # 3 Dados

dados = ["Verde", "Verde", "Verde", "Verde", "Verde", "Verde", "Amarelo", "Amarelo", "Amarelo", "Amarelo",
         "Vermelho", "Vermelho", "Vermelho"]


# Função para jogar os dados
def RolarDados():

    #Escolha dos 3 dados
    choose1 = random.choice(dados)
    choose2 = random.choice(dados)
    choose3 = random.choice(dados)
    print(choose1)
    print(choose2)
    print(choose3)
    print()

    if choose1 == "Verde":
        greenDice = random.choice(verde)
        print("Dado Verde: ", greenDice)
        if greenDice == "C":
            print("Ponto")
            print()
        elif greenDice == "P":
            print("Dado Verde = Pegadas!")
            print()
        else:
            print("Você perdeu 1 vida!")
            print()
    elif choose1 == "Amarelo":
        yellowDice = random.choice(amarelo)
        print("Dado Amarelo: ", yellowDice)
        if yellowDice == "C":
            print("Ponto")
            print()
        elif yellowDice == "P":
            print("Dado Amarelo = Pegadas!")
            print()
        else:
            print("Você perdeu 1 vida!")
            print()
    else:
        redDice = random.choice(vermelho)
        print("Dado Vermelho : ", redDice)
        if redDice == "C":
            print("Ponto")
            print()
        elif redDice == "P":
            print("Dado Vermelho = Pegadas!")
            print()
        else:
            print("Você perdeu 1 vida!")
            print()

    if choose2 == "Verde":
        greenDice = random.choice(verde)
        print("Dado Verde: ", greenDice)
        if greenDice == "C":
            print("Ponto")
            print()
        elif greenDice == "P":
            print("Dado Verde = Pegadas!")
            print()
        else:
            print("Você perdeu 1 vida!")
            print()
    elif choose2 == "Amarelo":
        yellowDice = random.choice(amarelo)
        print("Dado Amarelo: ", yellowDice)
        if yellowDice == "C":
            print("Ponto")
            print()
        elif yellowDice == "P":
            print("Dado Amarelo = Pegadas!")
            print()
        else:
            print("Você perdeu 1 vida!")
            print()
    else:
        redDice = random.choice(vermelho)
        print("Dado Vermelho : ", redDice)
        if redDice == "C":
            print("Ponto")
            print()
        elif redDice == "P":
            print("Dado Vermelho = Pegadas!")
            print()
        else:
            print("Você perdeu 1 vida!")
            print()

    if choose3 == "Verde":
        greenDice = random.choice(verde)
        print("Dado Verde: ", greenDice)
        if greenDice == "C":
            print("Ponto")
            print()
        elif greenDice == "P":
            print("Dado Verde = Pegadas!")
            print()
        else:
            print("Você perdeu 1 vida!")
            print()
    elif choose3 == "Amarelo":
        yellowDice = random.choice(amarelo)
        print("Dado Amarelo: ", yellowDice)
        if yellowDice == "C":
            print("Ponto")
            print()
        elif yellowDice == "P":
            print("Dado Amarelo = Pegadas!")
            print()
        else:
            print("Você perdeu 1 vida!")
            print()
    else:
        redDice = random.choice(vermelho)
        print("Dado Vermelho : ", redDice)
        if redDice == "C":
            print("Ponto")
            print()
        elif redDice == "P":
            print("Dado Vermelho = Pegadas!")
            print()
        else:
            print("Você perdeu 1 vida!")
            print()