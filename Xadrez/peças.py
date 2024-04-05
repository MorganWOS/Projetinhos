class Peças():
    """Classe para definir as peças do jogo"""


    def __init__(self):
        self.rei = 'Rei'
        self.rainha = 'Rainha'
        self.peão = 'Peão'
        self.torre = 'Torre'
        self.cavalo = 'Cavalo'
        self.bispo = 'Bispo'
        self.ordem_pretas = ['Torre', 'Cavalo', 'Bispo', 'Rei', 'Rainha', 'Bispo', 'Cavalo', 'Torre']
        self.ordem_brancas = ['Torre', 'Cavalo', 'Bispo', 'Rainha', 'Rei', 'Bispo', 'Cavalo', 'Torre']

    def mostra_jogadas_disponiveis(self, peça, posições, posição):
        #Mostra ao usuario quais são as jogadas disponiveis para a peça escolhida
        if peça == 'Peão':
            jogadas_disponiveis = [i for i in posições.keys() if i[0] == posição[0] and int(i[1]) == (int(posição[1]) + 1)]
        if peça == 'Rei':
            pass
        if peça == 'Rainha':
            pass
        if peça == 'Cavalo':
            pass
        if peça == 'Bispo':
            pass
        if peça == 'Torre':
            pass
        return jogadas_disponiveis