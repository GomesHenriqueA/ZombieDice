# Projeto Jogo Zombie Dice em Desenvolvimento por Henrique Gomes - Curso: Análise e Desenvolvimento de Sistemas
# 27/08/2021


import random

# Dados
dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"

playGame = False

# Adiciona os 13 dados no saco

saco = []


def adicionarDados():
    for i in range(0, 6):
        saco.append(dadoVerde)
    for i in range(0, 4):
        saco.append(dadoAmarelo)
    for i in range(0, 3):
        saco.append(dadoVermelho)


if playGame == True:
    adicionarDados()

# Seleção de Número de Jogadores
listPlayers = []

numJog = int(input("Insira o Número de Jogadores: "))
if numJog < 2:
    print("Número de Jogadores insuficientes!")
else:
    for ind in range(1, numJog + 1):
        nome = input(f"Insira o Nome do jogador N° {ind}: ")
        cerebros = 0
        vidas = 3

        # Adiciona cada jogador à lista e agrega o placar individual
        player = [f"Player N°{ind}, Nome: {nome}, Pontos: {cerebros}, Vidas: {vidas}"]
        listPlayers.append(player)

        playGame = True

    # Começar o Jogo!
    while playGame == True:
        adicionarDados()
        rodada = False
        i = 1

        # Indicação de quem irá jogar os dados
        try:
            jogador = int(input("Insira o Número do jogador que irá jogar os dados:"))
            jogadorVez = jogador - 1

        except:
            print("Insira um Valor Válido!")

        if jogador != 0:
            playGame = True
            rodada = True

        # Inicio da Rodada
        while rodada == True:
            try:
                jogar = int(input("[1] - Rolar os Dados\n[2] - Sair\n"))
            except:
                print("Digite um valor Válido!")
            if jogar == 1:
                dados = []
                for i in range(0, 3):
                    numSorteado = random.randint(1, 12)

                    dadoSorteado = saco[numSorteado]

                    faceDado = random.randint(0, 5)

                    # Verificação das faces sorteadas e agregamento de pontos
                    try:
                        if dadoSorteado[faceDado] == "C":
                            if listPlayers[jogadorVez][cerebros] == 13: # Em desenvolvimento
                                print(f"======= Vitória do Jogador N°{jogadorVez} =======")
                                rodada = False
                                playGame = False
                            else:
                                print(f"Dado {i + 1}: {dadoSorteado[faceDado]}")
                                print("Voce comeu um Cérebro!")
                                cerebros = cerebros + 1

                        elif dadoSorteado[faceDado] == "T":
                            if listPlayers[jogadorVez][vidas] == 0: # Em desenvolvimento
                                print("Você ficou sem vidas! Fim da sua Rodada!")
                                rodada = False
                            else:
                                print(f"Dado {i + 1}: {dadoSorteado[faceDado]}")
                                print("Você levou um tiro!")
                                vidas = vidas - 1
                        else:
                            print(f"Dado {i + 1}: {dadoSorteado[faceDado]}")
                            print("Sua vítma fugiu, corra atrás dela!!!")
                    except:
                        print("Erro")
            # Finalização de Turno
            elif jogar == 2:
                print("Fim do seu Turno!\nPróximo Jogador!")
                rodada = False
            try:
                continuar = int(input("Deseja Continuar Jogando?\n[1] - Sim\n[2] - Não\n"))
                if continuar == 1:
                    continue
                else:
                    print("Fim de Jogo!")
                    playGame = False
                    break
            except:
                print("Valor Inválido!")
        else:
            rodada = False
            playGame = False