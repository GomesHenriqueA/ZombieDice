# Projeto Jogo Zombie Dice em Desenvolvimento por Henrique Gomes - Curso: Análise e Desenvolvimento de Sistemas
# 27/08/2021

import os
import random

# Dados
dadoVerde = "CPCTPC"
dadoAmarelo = "TPCTPC"
dadoVermelho = "TPTCPT"

playGame = False

# Adiciona os 13 dados no saco

saco = []
listPlayers = []


def adicionarDados():
    for i in range(0, 6):
        saco.append(dadoVerde)
    for i in range(0, 4):
        saco.append(dadoAmarelo)
    for i in range(0, 3):
        saco.append(dadoVermelho)


opção = 0

# Abertura do Menu Principal
while opção != 4:
    print("======Zombie Dice======")
    print()
    print("Menu Principal")
    print("----------------------")
    print("""    [1] - Iniciar Novo Jogo
    [2] - Exibir Placar
    [3] - Excluir Jogador
    [4] - Sair""")
    print()
    opção = int(input("Escolha uma Opção!\n"))
    if opção == 1:
        print()
        print("Novo Jogo")
        print("----------------------")
        print('''    [1] - Adicionar Jogadores
    [2] - Voltar para o Menu''')
        opcaoInicio = int(input("Escolha uma Opção!\n"))
        if opcaoInicio == 1:

            # Seleção de Número de Jogadores
            numJog = int(input("Insira o Número de Jogadores: \n"))
            if numJog < 2:
                print("Número de Jogadores insuficientes!\nRetornando ao Menu Inicial")
            else:
                for ind in range(1, numJog + 1):
                    nome = input(f"Insira o Nome do jogador N° {ind}: ")
                    cerebrosTotal = 0
                    vidas = 3

                    # Adiciona cada jogador à lista e agrega o placar individual
                    player = ["N°" + str(ind), "Nome: " + str(nome), "Pontos: " + str(cerebrosTotal), "Vidas:" + str(vidas)]

                    listPlayers.append(player)  # Adiciona Lista 1 na lista com todos os jogadores.

                playGame = True

                # Começar o Jogo!
                while playGame == True:
                    adicionarDados()
                    rodada = False
                    i = 1
                    os.system("cls")

                    # Indicação de quem irá jogar os dados
                    try:
                        jogador = int(input("Insira o Número do jogador que irá jogar os dados:"))
                        jogadorVez = jogador - 1

                    except:
                            print("Insira um Valor Válido!")

                    if jogador != 0:
                        playGame = True
                        rodada = True
                        cerebrosTurno = 0
                        tirosTurno = 0

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
                                        if listPlayers[jogadorVez][2] == 13:  # Em desenvolvimento
                                            print(f"======= Vitória do Jogador N°{jogadorVez} =======")
                                            rodada = False
                                            playGame = False
                                        else:
                                            print(f"Dado {i + 1}: {dadoSorteado[faceDado]}")
                                            print("Voce comeu um Cérebro!\n")
                                            cerebrosTurno = cerebrosTurno + 1

                                    elif dadoSorteado[faceDado] == "T":
                                        if listPlayers[jogadorVez][3] == 0:  # Em desenvolvimento
                                            print("Você ficou sem vidas! Fim da sua Rodada!")
                                            rodada = False
                                        elif tirosTurno == 3:
                                            print("Você levou muitos tiros! Fim da sua Rodada!")
                                            rodada = False
                                        else:
                                            print(f"Dado {i + 1}: {dadoSorteado[faceDado]}")
                                            print("Você levou um tiro!\n")
                                            tirosTurno = tirosTurno + 1
                                    else:
                                        print(f"Dado {i + 1}: {dadoSorteado[faceDado]}")
                                        print("Sua vítma fugiu, corra atrás dela!!!\n")
                                except:
                                    print("Erro")
                        # Finalização de Turno
                        elif jogar == 2:
                            print("Fim do seu Turno!\nPróximo Jogador!")
                            rodada = False
                            listPlayers[jogadorVez][2] = "Pontos: " + str(cerebrosTotal + cerebrosTurno)
                            cerebrosTurno = 0
                            listPlayers[jogadorVez][3] = "Vidas: " + str(vidas - tirosTurno)
                            tirosTurno = 0
                        try:
                            continuar = int(input("Deseja Continuar Jogando?\n[1] - Sim\n[2] - Não\n"))
                            if continuar == 1:
                                if tirosTurno == 3:
                                    print("Impossível continuar jogando nesta Rodada.")
                                    print("Você levou muitos tiros! Fim do seu Turno!\n")
                                    rodada = False
                                    os.system("cls")
                                else:
                                    continue
                            elif continuar == 2:
                                listPlayers[jogadorVez][2] = "Pontos: " + str(cerebrosTotal + cerebrosTurno)
                                cerebrosTurno = 0
                                listPlayers[jogadorVez][3] = "Vidas: " + str(vidas - tirosTurno)
                                tirosTurno = 0
                                os.system("cls")
                                print("Fim do seu Turno!")
                                rodada = False
                            else:
                                print("Digite um Valor Válido!")
                        except:
                            print("Valor Inválido!")
                    else:
                        rodada = False
        elif opcaoInicio == 2:
            break
        else:
            print("Insira um Valor Válido!")

    # Opção 2 = Mostrar o Placar
    elif opção == 2:
        if len(listPlayers) == 0:
            print("A lista de Jogadores esta Vazia!\n")
        else:
            os.system("cls")
            print(listPlayers)

    # Opção 3 = Excluir um Jogador da lista
    elif opção == 3:
        if len(listPlayers) == 0:
            print("A lista de Jogadores esta Vazia!\n")
        elif len(listPlayers) == 2:
            print("Operação Ilegal!")
            print("Se um Jogador for Excluido o número de jogadores restantes será insuficiente para jogar!")
        else:
            delJogador = int(input("Digite o Número do Jogador que Deseja Excluir:"))
            delJogador = delJogador - 1
            listPlayers.pop(delJogador)

    # Opção 4 = Fechar o Jogo
    elif opção == 4:
        print("Jogo Encerrado!\nObrigado Por jogar!")
        break
    else:
        print("Valor Inválido!")
print("Fim do Programa!")