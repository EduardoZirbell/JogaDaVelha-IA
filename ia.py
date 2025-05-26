# ia.py
# Representa a IA do jogo.


class IA:
    def __init__(self):
        "Inicializa a IA como jogador 1 (círculo)."
        self.jogador = 1

    def simbolo(self):
        "Retorna o símbolo correspondente ao jogador da IA."
        return "O" if self.jogador == 1 else "X"

    def bestAction(self, board):
        "Calcula a melhor ação possível para a IA no estado atual do tabuleiro, utilizando o algoritmo Minimax."
        melhor_valor = float('-inf')
        melhor_acao = None
        for acao in board.acoes_possiveis():
            board.tabuleiro[acao[0]][acao[1]] = self.jogador
            valor = self.minimax(board, False)
            board.desfazer_jogada(acao)
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_acao = acao
        return melhor_acao

    def minimax(self, board, maximizando):
        "Roda o algoritmo Minimax recursivo para avaliar o melhor valor possível para a IA, simulando todas as jogadas futuras."
        vencedor = board.verificar_vencedor()
        if vencedor == self.jogador:
            return 1
        elif vencedor != 0:
            return -1
        elif board.tabuleiro_cheio():
            return 0

        if maximizando:
            melhor_valor = float('-inf')
            for acao in board.acoes_possiveis():
                board.tabuleiro[acao[0]][acao[1]] = self.jogador
                valor = self.minimax(board, False)
                board.desfazer_jogada(acao)
                melhor_valor = max(melhor_valor, valor)
            return melhor_valor
        else:
            pior_valor = float('inf')
            for acao in board.acoes_possiveis():
                board.tabuleiro[acao[0]][acao[1]] = 2  # Jogador humano
                valor = self.minimax(board, True)
                board.desfazer_jogada(acao)
                pior_valor = min(pior_valor, valor)
            return pior_valor
