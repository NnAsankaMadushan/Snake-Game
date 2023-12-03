import pygame
import time
import random

pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Snake initial position and size
snake_block = 10
snake_speed = 15

# Font
font_style = pygame.font.SysFont(None, 50)

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, GREEN, [x[0], x[1], snake_block, snake_block])

# Function to display the score
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, WHITE)
    win.blit(value, [0, 0])

# Function to run the game
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    # Initial length of the snake
    snake_list = []
    length_of_snake = 1

    # Initial position of the food
    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            win.fill(BLACK)
            Your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Check if the snake hits the boundaries
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # Update snake length and position of the food
        win.fill(BLACK)
        pygame.draw.rect(win, RED, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake collides with itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake
        our_snake(snake_block, snake_list)

        # Update display
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Set the speed of the snake
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
gameLoop()
