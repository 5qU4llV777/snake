import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Define as constantes
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

# Define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Cria a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Cria a cobrinha
snake = [(200, 200), (220, 200), (240, 200)]

# Cria a comida
food = (400, 300)

# Define a direção da cobrinha
direction = 'RIGHT'

# Loop principal
while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Move a cobrinha
    head = snake[-1]
    if direction == 'UP':
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == 'DOWN':
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == 'LEFT':
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == 'RIGHT':
        new_head = (head[0] + BLOCK_SIZE, head[1])
    snake.append(new_head)

    # Verifica se a cobrinha comeu a comida
    if snake[-1] == food:
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop(0)

    # Verifica se a cobrinha colidiu com a parede ou com ela mesma
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
            snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
            snake[-1] in snake[:-1]):
        pygame.quit()
        sys.exit()

    # Desenha a tela
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, WHITE, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()

    # Espera um pouco
    pygame.time.delay(1000 // SPEED)