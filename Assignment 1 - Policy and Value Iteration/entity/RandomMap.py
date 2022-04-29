import random
from pprint import pprint

length  = 12

random.seed() # Initialize random number generator
maze = []

for r in range(length):
    maze.append([])

    for c in range(length):
        colour_number = random.randint(0,3) # random number between 0 and 3 (4 types)
        if colour_number == 0:
            maze[r].append('#')  # wall
        elif colour_number == 1:
            maze[r].append('B')  # brown
        elif colour_number == 2:
            maze[r].append('G')  # green
        else:
            maze[r].append('W')  # white

pprint(maze)