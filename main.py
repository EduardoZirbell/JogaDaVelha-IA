import pygame
import sys

pygame.init()

# constantes
largura, altura = 300, 300  # Dimensões da janela do jogo
largura_linha = 5  # Espessura das linhas do tabuleiro
linhas, colunas = 3, 3  # Número de linhas e colunas do tabuleiro
tamanho_quadrado = largura // colunas  # Tamanho de cada célula do tabuleiro
raio_circulo = tamanho_quadrado // 3  # Raio do círculo (O)
largura_circulo = 15  # Espessura do círculo (O)
largura_x = 25  # Espessura do X
espaco = tamanho_quadrado // 4  # Espaço interno para o desenho do X

# cores
cor_fundo = (28, 170, 156)  # Cor de fundo da tela
cor_linha = (23, 145, 135)  # Cor das linhas do tabuleiro
cor_circulo = (239, 231, 200)  # Cor do círculo (jogador O)
cor_x = (84, 84, 84)  # Cor do X (jogador X)
cor_texto = (255, 255, 255)  # Cor dos textos na tela
cor_botao = (50, 50, 50)  # Cor do botão padrão
cor_botao_hover = (70, 70, 70)  # Cor do botão com mouse por cima
cor_vencedor = (255, 0, 0)  # Cor do texto de vencedor (vermelho)

# inicialização
tela = pygame.display.set_mode((largura, altura))  
pygame.display.set_caption('Jogo da Velha')  
fonte = pygame.font.SysFont(None, 36)  

# inicia o tabuleiro
tabuleiro = [[0 for _ in range(colunas)] for _ in range(linhas)]

# estados
estado = 'menu' 
jogador = 2  
fim_de_jogo = False  
texto_vencedor = ""  

# desenha as linhas horizontais e verticais do tabuleiro.
def desenhar_linhas():   
    for linha in range(1, linhas):
        pygame.draw.line(tela, cor_linha, (0, linha * tamanho_quadrado), (largura, linha * tamanho_quadrado), largura_linha)
    for coluna in range(1, colunas):
        pygame.draw.line(tela, cor_linha, (coluna * tamanho_quadrado, 0), (coluna * tamanho_quadrado, altura), largura_linha)
        
# desenha os símbolos x e o no tabuleiro.
def desenhar_figuras():
    for linha in range(linhas):
        for coluna in range(colunas):
            if tabuleiro[linha][coluna] == 1:  # o
                pygame.draw.circle(
                    tela, cor_circulo,
                    (coluna * tamanho_quadrado + tamanho_quadrado // 2, linha * tamanho_quadrado + tamanho_quadrado // 2),
                    raio_circulo, largura_circulo)
            elif tabuleiro[linha][coluna] == 2:  # x
                pygame.draw.line(tela, cor_x,
                                 (coluna * tamanho_quadrado + espaco, linha * tamanho_quadrado + espaco),
                                 (coluna * tamanho_quadrado + tamanho_quadrado - espaco,
                                  linha * tamanho_quadrado + tamanho_quadrado - espaco), largura_x)
                pygame.draw.line(tela, cor_x,
                                 (coluna * tamanho_quadrado + espaco, linha * tamanho_quadrado + tamanho_quadrado - espaco),
                                 (coluna * tamanho_quadrado + tamanho_quadrado - espaco, linha * tamanho_quadrado + espaco), largura_x)

# verifica se algum jogador venceu.
def verificar_vencedor():
    for linha in range(linhas):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != 0:
            return tabuleiro[linha][0]
    for coluna in range(colunas):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != 0:
            return tabuleiro[0][coluna]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != 0:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 0:
        return tabuleiro[0][2]
    return 0  # nenhum vencedor

def tabuleiro_cheio():
    return all(celula != 0 for linha in tabuleiro for celula in linha)

def reiniciar_jogo():
    global tabuleiro, fim_de_jogo, jogador, texto_vencedor
    tabuleiro = [[0 for _ in range(colunas)] for _ in range(linhas)]
    tela.fill(cor_fundo)
    desenhar_linhas()
    fim_de_jogo = False
    jogador = 2
    texto_vencedor = ""

def desenhar_botao(retangulo, texto):
    mouse = pygame.mouse.get_pos()
    cor = cor_botao_hover if retangulo.collidepoint(mouse) else cor_botao
    pygame.draw.rect(tela, cor, retangulo)
    rotulo = fonte.render(texto, True, cor_texto)
    tela.blit(rotulo, (retangulo.x + (retangulo.width - rotulo.get_width()) // 2,
                       retangulo.y + (retangulo.height - rotulo.get_height()) // 2))

def exibir_vencedor(texto):
    rotulo = fonte.render(texto, True, cor_vencedor)
    tela.blit(rotulo, (largura // 2 - rotulo.get_width() // 2, altura // 2 - rotulo.get_height() // 2))

executando = True
while executando:
    tela.fill(cor_fundo)

    if estado == 'menu':
        # cria os botões do menu inicial
        botao_jogar = pygame.Rect(100, 80, 100, 40)
        botao_sair = pygame.Rect(100, 150, 100, 40)
        desenhar_botao(botao_jogar, 'Jogar')
        desenhar_botao(botao_sair, 'Sair')
    elif estado == 'jogo':
        # desenha o tabuleiro e figuras
        desenhar_linhas()
        desenhar_figuras()
        if fim_de_jogo:
            exibir_vencedor(texto_vencedor)
            botao_menu = pygame.Rect(100, altura - 50, 100, 35)
            desenhar_botao(botao_menu, 'Menu')

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if estado == 'menu':
                if botao_jogar.collidepoint(evento.pos):
                    reiniciar_jogo()
                    estado = 'jogo'
                elif botao_sair.collidepoint(evento.pos):
                    executando = False
            elif estado == 'jogo':
                if fim_de_jogo:
                    if botao_menu.collidepoint(evento.pos):
                        estado = 'menu'
                else:
                    mouse_x, mouse_y = evento.pos
                    linha_clicada = mouse_y // tamanho_quadrado
                    coluna_clicada = mouse_x // tamanho_quadrado
                    if tabuleiro[linha_clicada][coluna_clicada] == 0:
                        tabuleiro[linha_clicada][coluna_clicada] = jogador
                        vencedor = verificar_vencedor()
                        if vencedor != 0:
                            fim_de_jogo = True
                            texto_vencedor = "X venceu!" if vencedor == 2 else "O venceu!"
                        elif tabuleiro_cheio():
                            fim_de_jogo = True
                            texto_vencedor = "Empate!"
                        jogador = 2 if jogador == 1 else 1

        if evento.type == pygame.KEYDOWN and estado == 'jogo':
            if evento.key == pygame.K_r:  # tecla r para reiniciar
                reiniciar_jogo()

    pygame.display.update()

pygame.quit()
