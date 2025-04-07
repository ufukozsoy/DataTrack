import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Load assets
plane_img = pygame.image.load("plane.png")  # Replace with your plane image
plane_img = pygame.transform.scale(plane_img, (50, 50))
enemy_img = pygame.image.load("enemy.png")  # Replace with your enemy image
enemy_img = pygame.transform.scale(enemy_img, (50, 50))

# Plane class
class Plane:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 50:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < HEIGHT - 50:
            self.y += self.speed

    def draw(self):
        screen.blit(plane_img, (self.x, self.y))

# Enemy class
class Enemy:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 50)
        self.y = random.randint(-100, -50)
        self.speed = random.randint(3, 6)

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-100, -50)
            self.x = random.randint(0, WIDTH - 50)

    def draw(self):
        screen.blit(enemy_img, (self.x, self.y))

# Main game loop
def main():
    plane = Plane()
    enemies = [Enemy() for _ in range(5)]
    running = True
    score = 0

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        plane.move(keys)

        for enemy in enemies:
            enemy.move()
            if pygame.Rect(plane.x, plane.y, 50, 50).colliderect(pygame.Rect(enemy.x, enemy.y, 50, 50)):
                print(f"Game Over! Final Score: {score}")
                pygame.quit()
                sys.exit()
            enemy.draw()

        plane.draw()

        # Update score
        score += 1
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()