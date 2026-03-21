try:
    import pygame
except ImportError:
    print("Pygame is not installed. Please install it using 'pip install pygame' and try again.")
    print("If Pygame is already installed, make sure you are using the correct Python version. Python 3.12 works best for Pygame.")
    input("Press Enter to exit...")
    exit(1)
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

# Game variables
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
last_move_time = 0
move_delay = 150
food = (random.randrange(0, 600, 20), random.randrange(0, 600, 20))
can_change_direction = True

running = True
while running:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update game logic
    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()
    
    if keys[pygame.K_RIGHT] and direction != "LEFT" and can_change_direction:
        direction = "RIGHT"
        can_change_direction = False
    if keys[pygame.K_LEFT] and direction != "RIGHT" and can_change_direction:
        direction = "LEFT"
        can_change_direction = False
    if keys[pygame.K_DOWN] and direction != "UP" and can_change_direction:
        direction = "DOWN"
        can_change_direction = False
    if keys[pygame.K_UP] and direction != "DOWN" and can_change_direction:
        direction = "UP"
        can_change_direction = False

    if current_time - last_move_time > move_delay and direction != "EMPTY":
        last_move_time = current_time
        can_change_direction = True
        if direction == "RIGHT":
            snake = [(snake[0][0] + 20, snake[0][1])] + snake[:-1]
        if direction == "LEFT":
            snake = [(snake[0][0] - 20, snake[0][1])] + snake[:-1]
        if direction == "DOWN":
            snake = [(snake[0][0], snake[0][1] + 20)] + snake[:-1]
        if direction == "UP":
            snake = [(snake[0][0], snake[0][1] - 20)] + snake[:-1]
    
    if snake[0] == food:
        snake.append(snake[-1])
        food = (random.randrange(0, 600, 20), random.randrange(0, 600, 20))

    if snake[0][0] < 0 or snake[0][1] < 0 or snake[0][0] >= 600 or snake[0][1] >= 600 or snake[0] in snake[1:]:
        running = False

    # 3. Draw everything
    screen.fill((0, 0, 0))  # Black background
    for (sx, sy) in snake:
        pygame.draw.rect(screen, (0, 255, 0), (sx, sy, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 20, 20))
    pygame.display.flip()

    clock.tick(60)  # 60 FPS cap

pygame.quit()