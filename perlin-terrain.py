import pygame
import noise
import numpy as np

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Real-Time Terrain Generation')
clock = pygame.time.Clock()

def generate_terrain(width, height, scale):
    terrain = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            terrain[x][y] = noise.pnoise2(x / scale, 
                                           y / scale, 
                                           octaves=6, 
                                           persistence=0.5, 
                                           lacunarity=2.0, 
                                           repeatx=1024, 
                                           repeaty=1024, 
                                           base=0)
    max_height = np.max(terrain)
    min_height = np.min(terrain)
    terrain = (terrain - min_height) / (max_height - min_height)  # Normalize
    return terrain

def draw_terrain(screen, terrain, width, height):
    for x in range(width):
        for y in range(height):
            color_value = terrain[x][y]
            color = (color_value * 255, color_value * 255, 255)
            pygame.draw.rect(screen, color, (x, y, 1, 1))

scale = 100.0
terrain = generate_terrain(SCREEN_WIDTH, SCREEN_HEIGHT, scale)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing the terrain
    draw_terrain(screen, terrain, SCREEN_WIDTH, SCREEN_HEIGHT)

    pygame.display.flip()
    clock.tick(60)  # Maintain 60 FPS

pygame.quit()

# import pygame
# import noise
# import numpy as np

# # Screen dimensions
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# # Pygame initialization
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),vsync=True)
# pygame.display.set_caption('Infinite Scrolling Terrain')
# clock = pygame.time.Clock()

# # Terrain parameters
# scale = 100.0
# scroll_speed = 2  # Speed of scrolling
# x_offset = 0  # Tracks horizontal scrolling position

# def generate_terrain_column(x_offset, height, scale):
#     """Generates a single column of terrain at a given x-offset"""
#     column = np.zeros(height)
#     for y in range(height):
#         column[y] = noise.pnoise2((x_offset) / scale, 
#                                   y / scale, 
#                                   octaves=6, 
#                                   persistence=0.5, 
#                                   lacunarity=2.0, 
#                                   repeatx=1024, 
#                                   repeaty=1024, 
#                                   base=0)
#     return column

# def normalize_terrain(terrain):
#     """Normalize terrain to range [0, 255] for coloring"""
#     min_val, max_val = np.min(terrain), np.max(terrain)
#     return ((terrain - min_val) / (max_val - min_val) * 255).astype(np.uint8)

# # Initialize terrain with first SCREEN_WIDTH columns
# terrain = np.array([generate_terrain_column(x, SCREEN_HEIGHT, scale) for x in range(SCREEN_WIDTH)]).T
# terrain = normalize_terrain(terrain)

# def draw_terrain(screen, terrain):
#     """Draws the terrain on the screen"""
#     surface = pygame.surfarray.make_surface(np.dstack([terrain] * 3))  # Convert grayscale to RGB
#     screen.blit(surface, (0, 0))  # Draw terrain as an image

# # Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Shift terrain left and generate new column
#     x_offset += scroll_speed  # Update scrolling position

#     # Remove leftmost column and add a new rightmost column
#     terrain = np.roll(terrain, -scroll_speed, axis=1)
#     for i in range(scroll_speed):
#         new_col = normalize_terrain(generate_terrain_column(x_offset + SCREEN_WIDTH + i, SCREEN_HEIGHT, scale))
#         terrain[:, -1 - i] = new_col  # Add new column at the right edge

#     # Draw updated terrain
#     draw_terrain(screen, terrain)
#     pygame.display.flip()
#     clock.tick(120)  # Maintain 60 FPS

# pygame.quit()
