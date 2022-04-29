from entity.Grid import *
from entity.GridType import *
from entity.Config import *
from entity.Coordinate import *
from entity.Maze import *
from data.LogData import *
from data.Plot import *
from pprint import pprint

# K Value
# k ( number of times simplified Bellman update is executed to produce the next utility estimate, default 20),
# set high values = [guarantee optimality similar to value iteration]
# If we set K = 1, it will not iteratively call on Bellman update, and there will be no values converge. This will then be value iteration
k = 10000
file_name = "Policy Iteration (K=" + str(k) + ")"

#  Calculates utilities for a given Policy.


def policyEvaluation(maze: Maze, k: int):
    for i in range(k):
        for r in range(NUM_ROW):
            for c in range(NUM_COL):
                # 1. Get current reward & policy
                currGrid = maze.getGrid(Coordinate(r, c))

                # Skip if currGrid is a wall
                if (currGrid.getGridType() == GridType.WALL):
                    continue

                # 2. Sum up the 3 neighbours (i.e. UP, LEFT, RIGHT) based on the current policy
                neighbours = maze.getNeighboursOfGrid(currGrid)
                up = PROBABILITY_UP * neighbours[0].getUtility()
                left = PROBABILITY_LEFT * neighbours[1].getUtility()
                right = PROBABILITY_RIGHT * neighbours[2].getUtility()

                # 3. Update Utility
                gridType = currGrid.getGridType()
                reward = getReward(gridType)
                currGrid.setUtility(
                    reward + DISCOUNT_FACTOR * (up + left + right))

# return "True : bool" if policy is changed


def policyImprovement(currGrid: Grid, maze: Maze) -> bool:
    # 1. Find the maximum possible sub-utility
    maxSubUtility = ['Temp', 'Temp', 'Temp', 'Temp']
    for dir in range(4):
        neighbours = maze.getNeighboursOfGridwDirection(currGrid, dir)
        up = PROBABILITY_UP * neighbours[0].getUtility()  # front grid utility
        left = PROBABILITY_LEFT * neighbours[1].getUtility()  # left grid utility
        right = PROBABILITY_RIGHT * neighbours[2].getUtility()  # right grid utlity

        maxSubUtility[dir] = up + left + right

    maxSU = 0
    # 2. Get the highest utility "direction"
    for dir in range(1, len(maxSubUtility)):
        if (maxSubUtility[dir] > maxSubUtility[maxSU]):
            maxSU = dir

    # 3. Current sub-utility (based on current policy)
    neighbours = maze.getNeighboursOfGrid(currGrid)
    up = PROBABILITY_UP * neighbours[0].getUtility() # Forward
    left = PROBABILITY_LEFT * neighbours[1].getUtility() # Noise
    right = PROBABILITY_RIGHT * neighbours[2].getUtility() # Noise

    currSubUtility = up + left + right

    # 4. Update policy
		# It will be true if there's a need to change the direction as there's a better utility.
		# After each iteration, this statement should be run lesser and lesser
    if (maxSubUtility[maxSU] > currSubUtility):
        currGrid.setPolicy(maxSU)
        return True
    else:
        return False


def PolicyIteration(maze: Maze):
    flag = True
    iteration = 1
    logger = LogData(maze)

    print("Default:")
    maze.printer()
    logger.add(maze)

    # Repeat 1 and 2 until policy is stable
    while flag:
        print("Iteration {}:\n".format(iteration))

        # 1. Policy Evaluation
        policyEvaluation(maze, k)

        # 2. Policy Improvement
        policyStable = True
        # for each s ε S
        for r in range(NUM_ROW):
            for c in range(NUM_COL):
                currGrid = maze.getGrid(Coordinate(r, c))

                # Skip if currGrid is a wall
                if (currGrid.getGridType() == GridType.WALL):
                    continue

                # Run policy improvement algorithm
                changed = policyImprovement(currGrid, maze)

                # current policy != new improved policy
                if (changed):
                    policyStable = False

                # Terminate once policy is stable
                if policyStable:
                    flag = False
                    break

        iteration += 1  # count the number of iterations
        maze.printer()  # Print out the progress
        logger.add(maze)  # Log data for plotting

    # pprint(logger.data)
    plot(logger.data, file_name)


if __name__ == '__main__':
    maze = Maze()
    PolicyIteration(maze)
