# Importe o módulo pygame
import pygame

# Importe pygame.locals para fácil acesso as cooordenadas chaves
# Atualizado para atender os padrõess flake8 e black
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Inicialize o pygame
pygame.init()

# Defina constantes para a altura e a largura da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Crie o objeto da tela
# O tamanho é definido pelas constantes 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variável para manter o loop do jogo
running = True

# Loop principal
while running:
    # Veja cada evento na fila de eventos
    for event in pygame.event.get():
        # O jogador pressionou alguma tecla?
        if event.type == KEYDOWN:
            # Foi a tecla Escape? Se sim, pare o loop.
            if event.key == K_ESCAPE:
                running = False

        # O jogador clicou o botão de fechar a janela? Se sim, pare o loop.
        elif event.type == QUIT:
            running = False

# Encha a tela com branco
screen.fill((255, 255, 255))

# Crie uma superfície e passe uma tupla com comprimento e largura
surf = pygame.Surface((50, 50))

# Dê a superfície uma cor para destacar do fundo
surf.fill((0, 0, 0))
rect = surf.get_rect()

# Coloque o centro de surf no centro da tela
surf_center = (
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_height())/2
)

# Desenhe surf com as novas coordenadas
screen.blit(surf, surf_center)
pygame.display.flip()