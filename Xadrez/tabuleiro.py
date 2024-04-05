class Tabuleiro:
    """Defini todas as carecterísticas de um tabuleiro"""
    

    def __init__(self):
        self.num_casas = 64
        self.colum_num = tuple(range(1, 9))
        self.colum_letra = (chr(i) for i in range(65, 73))
        self.color = ('Brancas', 'Pretas')
        self.posições = {}


    def cria_posições(self):
        """Cria todas as posições possíveis no tabuleiro
        usando a forma de coluna-fileira(letra-número)"""
        for num in self.colum_letra:
            for i in self.colum_num:
                self.posições[f'{num}{i}'] = ''