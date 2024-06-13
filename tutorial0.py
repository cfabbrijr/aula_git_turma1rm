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