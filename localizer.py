#import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    #
    # TODO - implement this in part 2
    #

    s = 0
    new_beliefs = beliefs
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == color:
                new_beliefs[i][j] = beliefs[i][j] * float(p_hit)
            else:
                new_beliefs[i][j] = beliefs[i][j] * float(p_miss)
            s = s + new_beliefs[i][j]

    new_beliefs_normalized = new_beliefs
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_beliefs_normalized[i][j] = new_beliefs[i][j] / float(s)

    return new_beliefs_normalized

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            # pdb.set_trace()            
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
