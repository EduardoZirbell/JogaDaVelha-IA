import pygame
from config import *

class Board:
    def __init__(self, tela):
        # Inicializa o objeto Board com uma tela Pygame e um tabuleiro vazio
        # 0 representa uma célula vazia, 1 e 2 representam os jogadores
        self.tela = tela
        self.tabuleiro = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
        self.fim_de_jogo = False
        self.texto_vencedor = ""

    def desenhar_linhas(self):
        # Desenha as linhas do tabuleiro (divisões horizontais e verticais)
        for linha in range(1, LINHAS):
            pygame.draw.line(self.tela, COR_LINHA, (0, linha * TAMANHO_QUADRADO), (LARGURA, linha * TAMANHO_QUADRADO), 5)
        for coluna in range(1, COLUNAS):
            pygame.draw.line(self.tela, COR_LINHA, (coluna * TAMANHO_QUADRADO, 0), (coluna * TAMANHO_QUADRADO, ALTURA), 5)

    def desenhar_figuras(self):
        # Desenha os símbolos dos jogadores (círculo para jogador 1 e X para jogador 2)
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                if self.tabuleiro[linha][coluna] == 1:
                    # Desenha círculo para jogador 1
                    pygame.draw.circle(self.tela, COR_CIRCULO,
                                       (coluna * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
                                        linha * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2),
                                       RAIO_CIRCULO, LARGURA_CIRCULO)
                elif self.tabuleiro[linha][coluna] == 2:
                    # Desenha X para jogador 2
                    pygame.draw.line(self.tela, COR_X,
                                     (coluna * TAMANHO_QUADRADO + ESPACO, linha * TAMANHO_QUADRADO + ESPACO),
                                     (coluna * TAMANHO_QUADRADO + TAMANHO_QUADRADO - ESPACO,
                                      linha * TAMANHO_QUADRADO + TAMANHO_QUADRADO - ESPACO), LARGURA_X)
                    pygame.draw.line(self.tela, COR_X,
                                     (coluna * TAMANHO_QUADRADO + ESPACO, linha * TAMANHO_QUADRADO + TAMANHO_QUADRADO - ESPACO),
                                     (coluna * TAMANHO_QUADRADO + TAMANHO_QUADRADO - ESPACO, linha * TAMANHO_QUADRADO + ESPACO), LARGURA_X)

    def verificar_vencedor(self):
        # Verifica se existe um vencedor nas linhas, colunas ou diagonais
        for linha in range(LINHAS):
            if self.tabuleiro[linha][0] == self.tabuleiro[linha][1] == self.tabuleiro[linha][2] != 0:
                return self.tabuleiro[linha][0]
        for coluna in range(COLUNAS):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != 0:
                return self.tabuleiro[0][coluna]
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != 0:
            return self.tabuleiro[0][0]
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != 0:
            return self.tabuleiro[0][2]
        return 0  # Retorna 0 caso não haja vencedor

    def tabuleiro_cheio(self):
        # Retorna True se todas as células do tabuleiro estiverem preenchidas
        return all(celula != 0 for linha in self.tabuleiro for celula in linha)

    def reiniciar(self):
        # Reinicia o tabuleiro e as variáveis de estado do jogo
        self.tabuleiro = [[0 for _ in range(COLUNAS)] for _ in range(LINHAS)]
        self.fim_de_jogo = False
        self.texto_vencedor = ""

    def jogar(self, linha, coluna, jogador):
        # Realiza a jogada do jogador na célula indicada, se for válida
        if self.tabuleiro[linha][coluna] == 0 and not self.fim_de_jogo:
            self.tabuleiro[linha][coluna] = jogador.jogador  # Marca a célula com o símbolo do jogador
            vencedor = self.verificar_vencedor()
            if vencedor != 0:
                # Define o vencedor e encerra o jogo
                self.fim_de_jogo = True
                self.texto_vencedor = f"{jogador.simbolo()} venceu!"
            elif self.tabuleiro_cheio():
                # Se não houver vencedor e o tabuleiro estiver cheio, é empate
                self.fim_de_jogo = True
                self.texto_vencedor = "Empate!"
            else:
                # Alterna o jogador se o jogo ainda não terminou
                jogador.alternar()

    def acoes_possiveis(self):
        # Retorna uma lista com todas as posições livres do tabuleiro
        return [(linha, coluna)
                for linha in range(LINHAS)
                for coluna in range(COLUNAS)
                if self.tabuleiro[linha][coluna] == 0]
    
    def desfazer_jogada(self, acao):
        # Desfaz a jogada realizada na posição fornecida (usado na IA)
        linha, coluna = acao
        self.tabuleiro[linha][coluna] = 0
