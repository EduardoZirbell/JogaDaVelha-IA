# game_core.py
# Controla o loop principal do jogo e a transição entre o menu e o jogo.

import pygame
from board import Board
from player import Player
from ia import IA
from config import *

class Game:
    # Inicializa o jogo, configurando a janela, o tabuleiro, os jogadores (humano e IA),
    # Define a configuração de fonte dos textos e o estado inicial (menu). Também define o loop principal como ativo.

    def __init__(self):
        # Inicializa o objeto Game_Core
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('Jogo da Velha')
        self.fonte = pygame.font.SysFont(None, 36)
        self.estado = 'menu'  # 'menu' ou 'jogo'
        self.board = Board(self.tela)
        self.jogador = Player()
        self.ia = IA()
        self.executando = True

    def desenhar_botao(self, ret, texto):
        # Desenha um botão interativo
        mouse = pygame.mouse.get_pos()
        cor = COR_BOTAO_HOVER if ret.collidepoint(mouse) else COR_BOTAO
        pygame.draw.rect(self.tela, cor, ret)
        rotulo = self.fonte.render(texto, True, COR_TEXTO)
        self.tela.blit(rotulo, (ret.x + (ret.width - rotulo.get_width()) // 2,
                                ret.y + (ret.height - rotulo.get_height()) // 2))

    def exibir_texto_central(self, texto, cor):
        # Exibe texto centralizado na tela
        rotulo = self.fonte.render(texto, True, cor)
        self.tela.blit(rotulo, (LARGURA // 2 - rotulo.get_width() // 2, ALTURA // 2 - rotulo.get_height() // 2))

    def loop(self):
        # Loop principal do jogo
        while self.executando:
            self.tela.fill(COR_FUNDO)

            if self.estado == 'menu':
                # Tela do menu
                botao_jogar = pygame.Rect(100, 80, 100, 40)
                botao_sair = pygame.Rect(100, 150, 100, 40)
                self.desenhar_botao(botao_jogar, 'Jogar')
                self.desenhar_botao(botao_sair, 'Sair')
            elif self.estado == 'jogo':
                # Tela do jogo
                self.board.desenhar_linhas()
                self.board.desenhar_figuras()
                if not self.board.fim_de_jogo:
                    rotulo = self.fonte.render(f"Vez de: {self.jogador.simbolo()}", True, COR_TEXTO)
                    self.tela.blit(rotulo, (10, 10))
                    if self.jogador.jogador == 1:
                        acao = self.ia.bestAction(self.board)
                        if acao:
                            self.board.jogar(acao[0], acao[1], self.jogador)
                else:
                    self.exibir_texto_central(self.board.texto_vencedor, COR_VENCEDOR)
                    botao_menu = pygame.Rect(100, ALTURA - 50, 100, 35)
                    self.desenhar_botao(botao_menu, 'Menu')

            # Trata os eventos do jogo, como fechar a janela, cliques do mouse e teclas pressionadas.
            # No menu, permite iniciar ou sair do jogo. Durante a partida, registra jogadas e permite reiniciar com a tecla "R".
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.executando = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.estado == 'menu':
                        if botao_jogar.collidepoint(evento.pos):
                            self.board.reiniciar()
                            self.jogador = Player()
                            self.estado = 'jogo'
                        elif botao_sair.collidepoint(evento.pos):
                            self.executando = False
                    elif self.estado == 'jogo':
                        if self.board.fim_de_jogo:
                            botao_menu = pygame.Rect(100, ALTURA - 50, 100, 35)
                            if botao_menu.collidepoint(evento.pos):
                                self.estado = 'menu'
                        else:
                            x, y = evento.pos
                            linha = y // TAMANHO_QUADRADO
                            coluna = x // TAMANHO_QUADRADO
                            self.board.jogar(linha, coluna, self.jogador)
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r and self.estado == 'jogo':
                        self.board.reiniciar()
                        self.jogador = Player()

            pygame.display.update()

        pygame.quit()
