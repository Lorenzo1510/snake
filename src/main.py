import config
import pygame
from game_logic import Snake, Food

pygame.init()
display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def game_loop():
    running = True
    snake = Snake(10, 10, 1)
    food = Food(5, 5)
    score = 0
    last_milestone = 0

    font = pygame.font.Font(None, 36)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.direction = 'right'
                elif event.key == pygame.K_LEFT:
                    snake.direction = 'left'
                elif event.key == pygame.K_UP:
                    snake.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    snake.direction = 'down'
        snake.move()
        if snake.body[0] == (food.x, food.y):
            score += 1
            snake.grow()
            food.respawn()
        if score % 5 == 0 and score != 0 and score != last_milestone:
            config.FPS += 5
            last_milestone = score
        if snake.check_collision():
            running = False
        display.fill(config.WHITE)
        pygame.draw.rect(display, config.RED, (food.x * config.GRID_SIZE, food.y * config.GRID_SIZE, config.GRID_SIZE, config.GRID_SIZE))
        for x, y in snake.body:
            pygame.draw.rect(display, config.GREEN, (x * config.GRID_SIZE, y * config.GRID_SIZE, config.GRID_SIZE, config.GRID_SIZE))


        score_text = font.render(f"Score: {score}", True, config.BLACK)
        display.blit(score_text, (10, 10))  # Mostra il punteggio in alto a sinistra

        pygame.display.update()
        clock.tick(config.FPS)

game_loop()