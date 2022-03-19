# Default Map
# map = [
#     ['G', '#', 'G', 'W', 'W', 'G'],
#     ['W', 'B', 'W', 'G', '#', 'B'],
#     ['W', 'W', 'B', 'W', 'G', 'W'],
#     ['W', 'W', 'W', 'B', 'W', 'G'],
#     ['W', '#', '#', '#', 'B', 'W'],
#     ['W', 'W', 'W', 'W', 'W', 'W']
# ]

# Random Map from running entity.randomMap
map = [
    ['#', '#', 'G', 'W', 'W', 'W', 'W', 'G', 'W', 'G', 'G', 'W'],
    ['B', 'G', '#', 'B', 'G', 'W', 'G', 'W', 'G', 'G', 'W', '#'],
    ['W', 'B', '#', 'W', '#', 'W', 'W', 'W', 'B', 'G', 'W', 'G'],
    ['B', 'W', 'G', 'W', 'W', 'G', '#', 'B', '#', 'W', '#', 'B'],
    ['G', 'B', 'B', 'W', 'W', 'W', '#', 'G', '#', 'G', '#', 'B'],
    ['#', 'B', 'W', 'G', 'B', 'G', 'G', '#', '#', 'W', '#', 'B'],
    ['W', '#', 'B', 'W', 'B', 'B', '#', '#', 'G', 'B', 'G', 'G'],
    ['B', 'G', 'G', 'G', '#', '#', 'B', '#', 'W', 'W', 'G', 'G'],

    ['#', '#', 'G', 'G', 'W', 'W', 'W', 'W', 'G', '#', 'B', '#'],
    ['#', 'B', 'G', 'B', 'B', 'W', 'W', '#', 'W', 'B', 'G', '#'],
    ['#', 'B', 'W', 'G', '#', 'G', 'G', 'G', 'B', '#', 'G', 'B'],
    ['W', 'W', '#', '#', '#', 'B', 'B', '#', 'B', 'B', '#', 'W']
]

# Grid World
NUM_ROW = len(map)
NUM_COL = len(map[0])

# Reward
REWARD_WHITE = float(-0.04)
REWARD_GREEN = float(1)
REWARD_BROWN = float(-1)
REWARD_WALL = float(0)

# Probabilities
PROBABILITY_UP = float(0.8)
PROBABILITY_LEFT = float(0.1)
PROBABILITY_RIGHT = float(0.1)

# Discount Factor
DISCOUNT_FACTOR = float(0.99)

