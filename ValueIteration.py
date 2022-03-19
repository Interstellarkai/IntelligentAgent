from entity.Grid import *
from entity.GridType import *
from entity.Config import *
from entity.Coordinate import *
from entity.Maze import *
from data.LogData import *
from data.Plot import *
from pprint import pprint


# Maximum Error allowed: (default 0.1)
# Lower Max Error => Higher Total Iteration Count
Rmax = +1  # Max Reward
c = 0.0001  # Constant
Epsilon = c * Rmax  # Max Error
gamma = DISCOUNT_FACTOR

file_name = "Value Iteration (Max_Error=" + str(Epsilon) + ")"


# Calculate the utility of the given Grid.
# return The difference prevUtility and newUtility

def calculateUtility(currGrid: Grid, maze: Maze) -> float:
    subUtilities = ['Temp', 'Temp', 'Temp', 'Temp']

    # 1. Find all possible utilities based on intended direction (i.e. UP, DOWN, LEFT, RIGHT)
    for dir in range(4):
        # Sum up the 3 possible utility of each intended direction (i.e. UP, LEFT, RIGHT)
		# 0.8 chance forward, 0.1 chance left, and 0.1 chance right 
        neighbours = maze.getNeighboursOfGridwDirection(currGrid, dir)
        up = PROBABILITY_UP * neighbours[0].getUtility()
        left = PROBABILITY_LEFT * neighbours[1].getUtility()
        right = PROBABILITY_RIGHT * neighbours[2].getUtility()

        subUtilities[dir] = up + left + right

    # 2. Find the maximum possible utility
    maxUtilityIndex = 0
    for u in range(len(subUtilities)): # 4 because of the directions above
        if (subUtilities[u] > subUtilities[maxUtilityIndex]):
            maxUtilityIndex = u

	# 3. Get the current grid reward value
    gridType = currGrid.getGridType()
    currReward = getReward(gridType)
    currUtility = currGrid.getUtility() # for pointer 5

    # 4. Update the utility & policy of current grid to the Max Utility
    newUtility = currReward + DISCOUNT_FACTOR * subUtilities[maxUtilityIndex]
    currGrid.setUtility(newUtility)
    currGrid.setPolicy(maxUtilityIndex)

    # 5. Return the difference of currUtility & newUtility
    return (abs(currUtility - newUtility))


def ValueIteration(maze: Maze):
    threshold = Epsilon * ((1 - gamma) / gamma)  # Convergence threshold
    maxChangeInUtility = 0 # To see improvement (Should get lesser with each iteration)
    iteration = 1 # To count the number of iterations
    logger = LogData(maze) # To log data for graph plotting

    print("Default:")
    maze.printer()
    logger.add(maze)

    while True:
        print("Iteration: {}".format(iteration))
        maxChange = 0

        # Explore the entire maze
        for r in range(NUM_ROW):
            for c in range(NUM_COL):
                currGrid = maze.getGrid(Coordinate(r, c))

                # 1. Skip if currGrid is a wall
                if (currGrid.getGridType() == GridType.WALL):
                    continue

                # 2a. Calculate and update utility on current grid
				# 2b. Get the change in current utility
                currChange = calculateUtility(currGrid, maze)

				# 3. Update the maxChange in utility
                if (currChange > maxChange):
                    maxChangeInUtility = currChange

        iteration += 1
		# Change in utility should get lesser with each iteration
        print("Maximum change in utility: {:.3f}".format(maxChangeInUtility))
        maze.printer() # Print the current maze progress
        logger.add(maze) # Log the data for plotting

        if maxChangeInUtility <= threshold:
            break

    # pprint(logger.data)
    plot(logger.data, file_name)

if __name__ == '__main__':
    maze = Maze()
    ValueIteration(maze)
