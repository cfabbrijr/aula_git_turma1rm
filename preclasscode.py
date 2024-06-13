# Importe o módulo pygame
import pygame

# Import random para números aleatórios
import random

# Importe pygame.locals para fácil acesso as coordenadas chaves
# Atualizado para atender os padrões flake8 e black
from pygame.locals import (
    RLEACCEL,
    K_UP,               # Tecla para cima
    K_DOWN,             # Tecla para baixo
    K_LEFT,             # Tecla para esquerda
    K_RIGHT,            # Tecla para direita
    K_ESCAPE,           # Tecla de escape
    KEYDOWN,            # Qualquer tecla pressionada
    QUIT,               # Tecla de fechar janela
)

# Defina constantes para largura e a altura da tel
SCREEN_WIDTH = 800          # Esta define a largura
SCREEN_HEIGHT = 600         # Esta define a altura

# Defina o objeto jogador extendendo a classe pygame.sprite.Sprite
# A surface desenhada na tela agora vai ser um atributo de 'jogador'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert() # define a área do objeto jogador como superfície surf
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)  # define a cor do fundo dessa área
        self.rect = self.surf.get_rect()                   # salva essa informação na variável rect
        
    # Mova o sprite com base nas teclas pressionadas pelo usuário
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)     #move_ip = move in place
    
        # Mantenha o jogador dentro da tela do jogo
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Defina o objeto inimigo extendendo a classe pygame.sprite.Sprite
# A superfície que você desenha na tela agora é um atributo do inimigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()    # carrega a imagem do inmigo
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Mova o sprite baseado na velocidade
    # REmova o sprite quando ele passa a borda esquerda da tela
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Defina o objeto cloud extendendo a classe pygame
# Use uma imagem para um sprite mais legal
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # A posição de partida é aleatória
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Mova a nuvem com velocidade constante
    # Remova a nuvem quando ela passa a borda esquerda da tela
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

# Ajuste para sons, os padrões são bons
pygame.mixer.init()

# Inicialize o pygame
pygame.init()


# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Crie o objeto da tela
# O tamanho da tela é definido pelas constantes SCREEN_WIDTH e SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Crie um evento personalizado para adicionar um novo inimigo
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Variável para manter o loop do jogo
running = True

# Instanciar o jogador. Até aqui, isso é apenas um retângulo.
player = Player()

# Crie grupos para conter os sprites dos inimigos
# - inimigos são usados para detectar colisões e atualizar posição
# - clouds são usadas para atulaização da posição
# - all_sprites é usado para desenhar na tela
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)

# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")

# Loop principal
while running:
    # Veja cada evento na fila de eventos
    for event in pygame.event.get():
        # O jogador pressionou alguma tecla?
        if event.type == KEYDOWN:
            # Foi a tecla ESCAPE? Se sim, para o loop.
            if event.type == K_ESCAPE:
                running = False
        # O jogador clicou o botão de fechar a janela? Se sim, pare o loop.
        elif event.type == QUIT:
            running = False

        # Adicione um novo inimigo?
        elif event.type == ADDENEMY:
            # Crie o novo inimigo e adicione ao grupo de sprites
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Adicione uma nova nuvem?
        elif event.type == ADDCLOUD:
            # Crie a nova nuvem e adicione ao grupo de sprites
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
        
    # Use o conjunto de teclas pressionadas e verifique a entrada do usuário
    pressed_keys = pygame.key.get_pressed()
    
            # Encha a tela com a cor branca   alterado em 07 junho
            # screen.fill((0, 0, 0))

            # Desenhe o jogador na tela
            # screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

            # Atualize o display
            # pygame.display.flip()

    # Atualize o sprite do jogador com base nas teclas pressionadas
    player.update(pressed_keys)

            # Fill the screen with black
            #screen.fill((0, 0, 0))

            # Draw the player on the screen
            #screen.blit(player.surf, player.rect)

            # Update the display
            #pygame.display.flip()

    # Atualize a posição de inimigo
    enemies.update()
    clouds.update()

    # Fill the screen with black
    screen.fill((135, 206, 250))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Verifique se qualquer inimigo colidiu com o jogador
    if pygame.sprite.spritecollideany(player, enemies):
        # Se sim, remova o jogador e pare o jogo
        player.kill()

        # Stop any moving sounds and play the collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()

        # Pare o loop
        running = False

    # Flip everything to the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# Nesse ponto, acabou, podemos parar e sair do mixer
pygame.mixer.music.stop()
pygame.mixer.quit()




