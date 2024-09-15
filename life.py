# pip install pygame
# pip install numpy
# pip install pygame numpy


import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Define screen size and colors
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set grid size
ROWS, COLS = 50, 50
CELL_SIZE = WIDTH // COLS

# Initialize the grid
grid = np.zeros((ROWS, COLS))

# Function to draw the grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if grid[row][col] == 1 else BLACK
            pygame.draw.rect(SCREEN, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

# Function to get the next generation
def next_generation(grid):
    new_grid = np.copy(grid)
    for row in range(ROWS):
        for col in range(COLS):
            # Get number of live neighbors
            live_neighbors = np.sum(grid[max(0, row - 1):min(ROWS, row + 2), max(0, col - 1):min(COLS, col + 2)]) - grid[row][col]
            
            # Apply Game of Life rules
            if grid[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[row][col] = 0
            elif grid[row][col] == 0 and live_neighbors == 3:
                new_grid[row][col] = 1
    return new_grid

# Main loop
def main():
    global grid
    running = True
    paused = True

    while running:
        SCREEN.fill(BLACK)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused  # Pause/unpause the game
                if event.key == pygame.K_r:
                    grid = np.zeros((ROWS, COLS))  # Reset the grid

            # Mouse input for toggling cells
            if pygame.mouse.get_pressed()[0]:
                mouseX, mouseY = pygame.mouse.get_pos()
                grid[mouseY // CELL_SIZE, mouseX // CELL_SIZE] = 1
            elif pygame.mouse.get_pressed()[2]:
                mouseX, mouseY = pygame.mouse.get_pos()
                grid[mouseY // CELL_SIZE, mouseX // CELL_SIZE] = 0

        if not paused:
            grid = next_generation(grid)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
