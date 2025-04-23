import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hentball Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball properties
ball_radius = 13
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 4 * random.choice([-1, 1])
ball_dy = 4 * random.choice([-1, 1])

# Paddle properties
paddle_width = 20
paddle_height = 100
left_paddle_x = 50
left_paddle_y = HEIGHT // 2 - paddle_height // 2
right_paddle_x = WIDTH - 50 - paddle_width
right_paddle_y = HEIGHT // 2 - paddle_height // 2
paddle_speed = 6

# Scores
left_score = 0
right_score = 0
font = pygame.font.Font(None, 74)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - paddle_height:
        right_paddle_y += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom walls
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_dy *= -1

    # Ball collision with paddles
    if (left_paddle_x < ball_x - ball_radius < left_paddle_x + paddle_width and
            left_paddle_y < ball_y < left_paddle_y + paddle_height):
        ball_dx *= -1
    if (right_paddle_x < ball_x + ball_radius < right_paddle_x + paddle_width and
            right_paddle_y < ball_y < right_paddle_y + paddle_height):
        ball_dx *= -1

    # Ball out of bounds
    if ball_x < 0:
        right_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx *= -1
    if ball_x > WIDTH:
        left_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx *= -1

    # Draw paddles, ball, and scores
    pygame.draw.rect(screen, RED, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, BLUE, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (3 * WIDTH // 4, 20))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()