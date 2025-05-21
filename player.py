# player.py
# Representa o jogador atual do jogo.

class Player:
    def __init__(self):
        # Jogador começa com o valor 2 (representa "X")
        self.jogador = 2

    def simbolo(self):
        # Retorna o símbolo correspondente ao jogador atual
        return 'X' if self.jogador == 2 else 'O'

    def alternar(self):
        # Alterna entre os jogadores (1 e 2)
        self.jogador = 1 if self.jogador == 2 else 2
