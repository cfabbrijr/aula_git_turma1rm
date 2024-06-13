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

