from copy import deepcopy
def game_of_life(grid):
    """
        Test one state of the game of life for this following cellular automata
        See if the following implementation of this will result in a correct state
    """
    copy = deepcopy(grid)
    neighborhood = {0, -1, 1}

    for row in grid:
        for col in grid[row]:
            if grid[row][col] == 1:

                # Access the alive count in the neighborhood
                alive_count = 0
                for i in range(3):
                    for j in range(3):
                        if not(neighborhood[i] == 0 and neighborhood[i] == 0):
                            ni_row = [i + row]
                            ni_col = [i + col]

                            if (row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row])
                                and grid[ni_row][ni_col]):
                                alive_count += 1

                # Perform the following rules accordingly to number alive
                if (grid[row][col] == 1 and alive_count < 2):
                    copy[row][col] = 0
                elif (grid[row][col] == 1 and (alive_count == 2 or alive_count == 3)):
                    copy[row][col] = 1
                elif (grid[row][col] == 1 and alive_count > 3):
                    copy[row][col] = 0
                elif (grid[row][col] == 0 and alive_count == 3):
                    copy[row][col] = 1
    