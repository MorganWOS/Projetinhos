import tabuleiro
import peças
import player
import maquina

#Declara as variaveis principais e as instancias que o jogo ira utilizar
tab = tabuleiro.Tabuleiro()
pe = peças.Peças()
pla = player.Player()
maq = maquina.Maquina()

termino = False
xeque_mate = False
turno = True

casas_vazias = []


#Cria o jogo
cor = input("Escolha a cor de suas peças(b/p): ")
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

def conta_casa_vazias(lista):
    for casa, valor in tab.posições.items():
        if valor == '':
            lista.append(casa)
conta_casa_vazias(casas_vazias)
print(casas_vazias)

"""""
while termino == False:
    if xeque_mate:
        print('Game Over')
        termino == True
    if turno:
        pergunta_jogada = input("Faça sua jogada: ")
        pla.jogada(pergunta_jogada)
        turno == False

    if turno == False:
        print("A maquina esta pensando...")
        maq.jogada()
        turno == True"""