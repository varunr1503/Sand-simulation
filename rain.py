import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Purple Rain Simulation")

# Colors
BLACK = (0, 0, 0)
PURPLE = (138, 43, 226)
LIGHT_PURPLE = (186, 85, 211)
DARK_PURPLE = (48, 25, 52)  # Darker purple for gradient background

# Number of raindrops
NUM_DROPS = 200

# Raindrop class
class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.length = random.randint(10, 20)
        self.speed = random.uniform(4, 10)

    def update(self):
        self.y += self.speed  # Move downward
        if self.y > HEIGHT:  # Reset if out of bounds
            self.y = random.randint(-20, -5)
            self.x = random.randint(0, WIDTH)
            self.speed = random.uniform(4, 10)

    def draw(self, surface):
        #glow effect
        # pygame.draw.line(surface, LIGHT_PURPLE, (self.x, self.y), (self.x, self.y + self.length),4)
        #draw rain
        pygame.draw.line(surface, PURPLE, (self.x, self.y), (self.x, self.y + self.length), 2)

# Function to draw gradient background
def draw_gradient_background(surface):
    for y in range(HEIGHT):
        color = (
            int(DARK_PURPLE[0] + (PURPLE[0] - DARK_PURPLE[0]) * (y / HEIGHT)),
            int(DARK_PURPLE[1] + (PURPLE[1] - DARK_PURPLE[1]) * (y / HEIGHT)),
            int(DARK_PURPLE[2] + (PURPLE[2] - DARK_PURPLE[2]) * (y / HEIGHT))
        )
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))



# Create raindrops
raindrops = [Raindrop() for _ in range(NUM_DROPS)]

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    # screen.fill(BLACK)
    draw_gradient_background(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for drop in raindrops:
        drop.update()
        drop.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

