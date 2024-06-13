# Encha a tela com branco
screen.fill((255, 255, 255))

# Crie uma superfície e passe uma tupla com comprimento e largura
surf = pygame.Surface((50, 50))

# Dê a superfície uma cor para destacar do fundo
surf.fill((0, 0, 0))
rect = surf.get_rect()

# Esta linha diz "Desenhe surf sobre o centro da tela"
screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
pygame.display.flip()

# Coloque o centro de surf no centro da tela
surf_center = (
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_height())/2
)

# Desenhe surf com as novas coordenadas
screen.blit(surf, surf_center)
pygame.display.flip()

# Defina o objeto Jogador extendendo pygame.sprite.Sprite
# A superfície desenhada na tela é agora um atributo do 'jogador'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()