import pygame
import math
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pool Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball properties
BALL_RADIUS = 10
FRICTION = 0.98

# Clock for controlling frame rate
clock = pygame.time.Clock()

class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Apply friction
        self.vx *= FRICTION
        self.vy *= FRICTION

        # Collision with walls
        if self.x - BALL_RADIUS < 0 or self.x + BALL_RADIUS > WIDTH:
            self.vx = -self.vx
        if self.y - BALL_RADIUS < 0 or self.y + BALL_RADIUS > HEIGHT:
            self.vy = -self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), BALL_RADIUS)

# Create balls
balls = [Ball(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), RED) for _ in range(5)]
cue_ball = Ball(WIDTH // 2, HEIGHT // 2, WHITE)

# Game loop
running = True
while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position and handle cue ball movement
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:  # Left mouse button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - cue_ball.x
        dy = mouse_y - cue_ball.y
        distance = math.hypot(dx, dy)
        if distance > 0:
            cue_ball.vx += dx / distance * 2
            cue_ball.vy += dy / distance * 2

    # Update and draw balls
    cue_ball.move()
    cue_ball.draw(screen)

    for ball in balls:
        ball.move()
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()