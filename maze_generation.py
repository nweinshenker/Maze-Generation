from random import shuffle, random
import numpy as np



def generatorGrid(width, height):
    """
    Generates a grid of n x m to be defined as the board for which we will do the basic
    search of our graph traversals
    """
    board_grid = np.zeros([width, height])

    # Fill a portion of the grid position with 1 respresented as wall
    board_grid[1][:3] = np.fill_diagonal
    return

if __name__ == "__main__":
    print("hello")
    pass