# config.py
# Este arquivo contém as constantes usadas no jogo.

# Tamanho da tela
LARGURA, ALTURA = 300, 300

# Número de linhas e colunas do tabuleiro
LINHAS, COLUNAS = 3, 3

# Tamanho de cada célula/quadrado
TAMANHO_QUADRADO = LARGURA // COLUNAS

# Propriedades gráficas das formas (círculo e X)
RAIO_CIRCULO = TAMANHO_QUADRADO // 3
LARGURA_CIRCULO = 15
LARGURA_X = 25
ESPACO = TAMANHO_QUADRADO // 4

# Cores (RGB)
COR_FUNDO = (28, 170, 156)
COR_LINHA = (23, 145, 135)
COR_CIRCULO = (239, 231, 200)
COR_X = (84, 84, 84)
COR_TEXTO = (255, 255, 255)
COR_BOTAO = (50, 50, 50)
COR_BOTAO_HOVER = (70, 70, 70)
COR_VENCEDOR = (255, 0, 0)
