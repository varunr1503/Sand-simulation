import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

# Simulation parameters
WIDTH, HEIGHT = 100, 75  # Grid size (smaller for better performance)
PIXEL_SIZE = 8  # Size of each sand particle
WINDOW_WIDTH, WINDOW_HEIGHT = WIDTH * PIXEL_SIZE, HEIGHT * PIXEL_SIZE

# Colors
SAND_COLOR = (0.9, 0.7, 0.2)

# Initialize sand grid (1 = sand, 0 = empty)
sand_grid = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

# Constants for physics
GRAVITY = 1  # Strength of gravity

def update_sand():
    """Updates the sand particles using basic physics."""
    # Process sand from bottom to top to prevent overwrite issues
    for y in range(HEIGHT - 2, -1, -1):  # Start from second-last row up
        for x in range(1, WIDTH - 1):  # Avoid out-of-bounds issues
            if sand_grid[y, x] == 1:  # If this cell contains sand
                
                # Move directly down if empty space is available
                if sand_grid[y + 1, x] == 0:
                    sand_grid[y + 1, x] = 1
                    sand_grid[y, x] = 0
                
                # If blocked, try to move diagonally (random left/right)
                elif sand_grid[y + 1, x] != 0:
                    direction = np.random.choice([-1, 1])  # Randomize left/right movement
                    if sand_grid[y + 1, x + direction] == 0:
                        sand_grid[y + 1, x + direction] = 1
                        sand_grid[y, x] = 0

def render_sand():
    """Render sand particles using OpenGL."""
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if sand_grid[y, x] == 1:
                glColor3f(*SAND_COLOR)
                x_pos = x * PIXEL_SIZE
                y_pos = y * PIXEL_SIZE

                glVertex2f(x_pos, y_pos)
                glVertex2f(x_pos + PIXEL_SIZE, y_pos)
                glVertex2f(x_pos + PIXEL_SIZE, y_pos + PIXEL_SIZE)
                glVertex2f(x_pos, y_pos + PIXEL_SIZE)
    glEnd()

def main():
    """Main simulation loop."""
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
    glOrtho(0, WINDOW_WIDTH, WINDOW_HEIGHT, 0, -1, 1)

    running = True
    while running:
        pygame.time.delay(30)  # Slow down simulation for better visualization
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # Left click to add sand
                    mx, my = pygame.mouse.get_pos()
                    grid_x = mx // PIXEL_SIZE
                    grid_y = my // PIXEL_SIZE
                    if 0 <= grid_x < WIDTH and 0 <= grid_y < HEIGHT:
                        sand_grid[grid_y, grid_x] = 1

        update_sand()  # Apply physics
        render_sand()  # Draw the grid
        pygame.display.flip()  # Refresh screen

    pygame.quit()

if __name__ == "__main__":
    main()
