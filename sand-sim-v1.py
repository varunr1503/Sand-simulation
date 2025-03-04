#just a basic simulation - sand particle moves down if there's an empty space or if blocked, moves left/right
import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

# Simulation parameters
WIDTH, HEIGHT = 200, 150  # Simulation grid size
PIXEL_SIZE = 5  # Pixel size for rendering
WINDOW_WIDTH, WINDOW_HEIGHT = WIDTH * PIXEL_SIZE, HEIGHT * PIXEL_SIZE

# Colors
SAND_COLOR = (0.9, 0.7, 0.2)

# Initialize the sand grid
sand_grid = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

def update_sand():
    """Updates the sand particles using a simple cellular automaton."""
    for y in range(HEIGHT - 2, -1, -1):  # Iterate from bottom to top
        for x in range(1, WIDTH - 1):
            if sand_grid[y, x] == 1:  # If this cell is sand
                # Try to move downward
                if sand_grid[y + 1, x] == 0:
                    sand_grid[y + 1, x] = 1
                    sand_grid[y, x] = 0
                # Try to move diagonally left
                elif sand_grid[y + 1, x - 1] == 0:
                    sand_grid[y + 1, x - 1] = 1
                    sand_grid[y, x] = 0
                # Try to move diagonally right
                elif sand_grid[y + 1, x + 1] == 0:
                    sand_grid[y + 1, x + 1] = 1
                    sand_grid[y, x] = 0

def render_sand():
    """Render the sand particles using OpenGL."""
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
    """Main loop to run the simulation."""
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
    
    glOrtho(0, WINDOW_WIDTH, WINDOW_HEIGHT, 0, -1, 1)  # Set up 2D projection
    
    running = True
    while running:
        pygame.time.delay(10)  # Slow down the simulation slightly
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # Left mouse button
                    mx, my = pygame.mouse.get_pos()
                    grid_x = mx // PIXEL_SIZE
                    grid_y = my // PIXEL_SIZE
                    if 0 <= grid_x < WIDTH and 0 <= grid_y < HEIGHT:
                        sand_grid[grid_y, grid_x] = 1  # Place sand at the clicked position
        
        update_sand()  # Update sand particles
        render_sand()  # Render updated sand grid
        pygame.display.flip()  # Swap buffers
    
    pygame.quit()

if __name__ == "__main__":
    main()
