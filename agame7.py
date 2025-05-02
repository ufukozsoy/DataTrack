import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tennis Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 10

# Paddle positions
player1_x, player1_y = 50, HEIGHT // 2 - PADDLE_HEIGHT // 2
player2_x, player2_y = WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2

# Ball position and velocity
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 4, 4

# Speeds
paddle_speed = 6

# Scores
player1_score, player2_score = 0, 0
font = pygame.font.Font(None, 74)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom walls
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if (player1_x < ball_x - BALL_RADIUS < player1_x + PADDLE_WIDTH and
            player1_y < ball_y < player1_y + PADDLE_HEIGHT):
        ball_dx = -ball_dx
    if (player2_x < ball_x + BALL_RADIUS < player2_x + PADDLE_WIDTH and
            player2_y < ball_y < player2_y + PADDLE_HEIGHT):
        ball_dx = -ball_dx

    # Ball out of bounds
    if ball_x < 0:
        player2_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = -ball_dx
    if ball_x > WIDTH:
        player1_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = -ball_dx

    # Draw paddles, ball, and scores
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

    score_text = font.render(f"{player1_score} - {player2_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()