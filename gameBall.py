import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball properties
BALL_RADIUS = 15
BALL_SPEED = 5

# Paddle properties
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
PADDLE_SPEED = 7

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Ball position and velocity
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([-BALL_SPEED, BALL_SPEED])
ball_dy = random.choice([-BALL_SPEED, BALL_SPEED])
# Ensure the ball is moving diagonally
if ball_dx == 0:
    ball_dx = BALL_SPEED
if ball_dy == 0:
    ball_dy = BALL_SPEED
# Ball initial position
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
# Ball initial velocity

# Paddle position
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - 30

# Score
score = 0

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
        paddle_x += PADDLE_SPEED

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
        ball_dx = -ball_dx
    if ball_y - BALL_RADIUS <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if (paddle_y <= ball_y + BALL_RADIUS <= paddle_y + PADDLE_HEIGHT and
            paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH):
        ball_dy = -ball_dy
        score += 1

    # Ball falls below the paddle
    if ball_y > HEIGHT:
        print(f"Game Over! Your score: {score}")
        running = False

    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    # Draw paddle
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
# Quit pygame

pygame.quit()
# Exit the program
import sys
sys.exit()
