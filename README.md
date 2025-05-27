# JogaDaVelha-IA

Um jogo da velha com interface gráfica feita em Pygame e um jogador controlado por Inteligência Artificial.

##  Funcionalidades

- Modo jogador vs IA
- Interface gráfica amigável com Pygame
- IA básica para tomada de decisões (Minimax)
## 📁 Estrutura do Projeto

```
JogaDaVelha-IA/
├── board.py          # Representação e lógica do tabuleiro
├── config.py         # Configurações visuais e gerais do jogo
├── game_core.py      # Loop principal do jogo e manipulação de eventos
├── ia.py             # Algoritmo da Inteligência Artificial
├── main.py           # Ponto de entrada do jogo
└── player.py         # Representação dos jogadores
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8+
- Pygame

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/JogaDaVelha-IA.git
cd JogaDaVelha-IA
```

2. Instale as dependências:

```bash
pip install pygame
```

3. Execute o jogo:

```bash
python main.py
```

## 🎯 Como Jogar

- O jogo inicia automaticamente.
- Clique com o mouse para marcar sua jogada.
- A IA responderá em seguida.
- O primeiro a alinhar três símbolos vence.

