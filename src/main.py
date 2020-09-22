import os, sys, random
import pygame
from pygame.locals import *

# Basic tests for the following imports to see if place within
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Character Objects to be placed within the maze
class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer

WIDTH, HEIGHT = 40, 40
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

pygame.init()
screen = pygame.display.set_mode([405, 405])

def main():
    """ 
    Function call for the game logic to set up the initial maze generation of the 
    following pygame
    """
    pygame.display.set_caption("Maze Generation")
    pygame.mouse.set_visible(True)


    # Set up the objects of the pygame 
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                running= False# Flag that we are done so we exit this loop
                print("Exiting the Program")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                grid[row][column] = 1
                print("Click ", pos, "grid coordinates: ", row, column)
    
        # Set the screen background
        screen.fill(WHITE)
    
        # Draw the grid
        for row in range(10):
            for column in range(10):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                    pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
        # Go ahead and update the screen with what we've drawn.
        # Draw Everything
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
