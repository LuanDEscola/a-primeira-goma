import pygame

# Inicializando o pygame
pygame.init()

# Definido o tamanho da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ez")

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # Atualização a tela
            pygame.display.flip()