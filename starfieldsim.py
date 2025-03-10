import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starfield Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Number of stars
NUM_STARS = 500

# Star class
class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.z = random.randint(1, WIDTH)  # Depth factor
        self.speed = random.uniform(2, 60)  # Speed based on depth
        self.pz = self.z

    def update(self):
        self.z -= self.speed  # Move forward
        if self.z <= 0:  # Reset if out of bounds
            self.x = random.randint(0, WIDTH)
            self.y = random.randint(0, HEIGHT)
            self.z = WIDTH
            self.pz = self.z
            self.speed = random.uniform(2, 6)

    def draw(self, surface):
        size = max(1, int((WIDTH - self.z) / WIDTH * 5))  # Size depends on depth
        screen_x = int((self.x - WIDTH / 2) * (WIDTH / self.z) + WIDTH / 2)
        screen_y = int((self.y - HEIGHT / 2) * (WIDTH / self.z) + HEIGHT / 2)

        px = int((self.x - WIDTH / 2) * (WIDTH / self.pz) + WIDTH / 2)
        py = int((self.y - HEIGHT / 2) * (WIDTH / self.pz) + HEIGHT / 2)
    
        # pygame.draw.circle(surface, WHITE, (screen_x, screen_y), size)
        pygame.draw.line(surface, WHITE, (px, py), (screen_x, screen_y))

        # pygame.draw.circle(surface, WHITE, (screen_x, screen_y), size)

        self.pz = self.z

# Create stars
stars = [Star() for _ in range(NUM_STARS)]

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for star in stars:
        star.update()
        star.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
