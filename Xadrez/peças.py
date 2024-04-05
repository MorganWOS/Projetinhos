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
