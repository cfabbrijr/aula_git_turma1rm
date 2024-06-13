# Importe e inicialize a biblioteca pygame
import pygame
pygame.init()

# Ajuste o tamanho da tela
screen = pygame.display.set_mode([500, 500])

# Rode até que o usuário peça pra sair
running = True
while running:

    # Teste se o usuário clicou no botão de fechar?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencha o fundo da tela com a cor branca
    screen.fill((255, 255, 255))

    # Desenhe um círculo sólido de cor azul no centro da tela
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Atualize o display
    pygame.display.flip()

# pronto! Hora de sair
pygame.quit()
