import tabuleiro
import peças
import player
import maquina
import numpy as np

#Declara as variaveis principais e as instancias que o jogo ira utilizar
tab = tabuleiro.Tabuleiro()
pe = peças.Peças()
pla = player.Player()
maq = maquina.Maquina()

termino = False
xeque_mate = False
turno = True

casas_vazias = []
peças_brancas = []
peças_pretas = []

def faz_jogada(posições, antiga_posição, escolha, peça):
    posições[escolha] = peça
    posições[antiga_posição] = ''


#Cria o jogo 
tab.cria_posições()
for key in tab.posições.keys():
    if key[1] == '2' or key[1] == '7':
        tab.posições[key] = 'Peão'
    if key[1] == '1':
        for peça in pe.ordem_pretas:
            tab.posições[key] = peça
            pe.ordem_pretas.remove(peça)
            break
    if key[1] == '8':
        for peça in pe.ordem_brancas:
            tab.posições[key] = peça
            pe.ordem_brancas.remove(peça)
            break
    if key[1] == '7' or key[1] == '8':
        peças_brancas.append(key)
    if key[1] == '2' or key[1] == '1':
        peças_pretas.append(key)

def conta_casa_vazias(lista):
    for casa, valor in tab.posições.items():
        if casa in lista:
            continue
        if valor == '':
            lista.append(casa)
representação = np.array([[i for i in tab.posições.keys() if i[1] == '1'], [i for i in tab.posições.keys() if i[1] == '2'],
                          [i for i in tab.posições.keys() if i[1] == '3'], [i for i in tab.posições.keys() if i[1] == '4'],
                          [i for i in tab.posições.keys() if i[1] == '5'], [i for i in tab.posições.keys() if i[1] == '6'],
                          [i for i in tab.posições.keys() if i[1] == '7'], [i for i in tab.posições.keys() if i[1] == '8']])
print(representação)
cor = input("Escolha a cor de suas peças(b/p): ") 
if cor == 'p':
    print("Suas peças estão nas fileiras 1 e 2")
    print("D1 = Rei")
if cor =='b':
    print("Suas peaçs estão nas fileiras 8 e 7 ")
    print("E8 = Rei")

while termino == False:
    conta_casa_vazias(casas_vazias)
    if xeque_mate:
        print('Game Over')
        termino == True
    if turno:
        print("1 - Ver tabuleiro\n2 - Ver casas vazias ou comiveis\n3 - Ver suas posições\n4 - fazer jogada")
        pergunta_jogador = str(input("Escolha uma das opções: "))
        if pergunta_jogador == '1':
            print(representação)
        if pergunta_jogador == '2':
            print(casas_vazias)
        if pergunta_jogador == '3':
            if cor == 'p':
                print(peças_pretas)
            else:
                print(peças_brancas)
        if pergunta_jogador == '4':
            escolhe_peça = input("Escolha a peça ou casa: ")
            print(tab.posições[escolhe_peça])
            if tab.posições[escolhe_peça] == 'Peão':
                print(pe.mostra_jogadas_disponiveis(tab.posições[escolhe_peça], tab.posições, escolhe_peça))
            escolhe_jogada = input("Escolha a casa para qual quer se movimentar: ")
            faz_jogada(tab.posições, escolhe_peça, escolhe_jogada, tab.posições[escolhe_peça])
            casas_vazias.remove(escolhe_jogada)
            turno = False
        


    if turno == False:
        print("A maquina esta pensando...")
        print("A maquina fez a jogada!")
        turno = True