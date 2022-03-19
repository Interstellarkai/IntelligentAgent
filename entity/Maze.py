from .Config import *
from .Grid import *
from .Coordinate import *
from .GridType import *
from .Config import *

class Maze(object):
    def __init__(self):
        self.numRow = NUM_ROW
        self.numCol = NUM_COL
        self.grids = [[0 for i in range(self.numCol)]
                      for j in range(self.numRow)]

        for r in range(self.numRow):
            for c in range(self.numCol):
                coord = Coordinate(r, c)
                self.grids[r][c] = Grid(coord)
        
        self.importMap()

    def getGrid(self, coordinate: Coordinate) -> Grid:
        r = coordinate.getRow()
        c = coordinate.getCol()
        grids = self.grids[r][c]
        return grids

    def getNeighboursOfGrid(self, currGrid: Grid) -> list:
        currPolicy = currGrid.getPolicy()
        neighbourCoords = currGrid.getNeighbours(getValue(currPolicy))

        # Make sure neighbour GridType is not a wall
        neighbourGrids = []
        for n in range(len(neighbourCoords)):
            neighbourGrid = self.getGrid(neighbourCoords[n])

            # If it's a wall, use current coordinate
            if (neighbourGrid.getGridType() == GridType.WALL):
                neighbourCoords[n] = currGrid

            neighbourGrids.append(self.getGrid(neighbourCoords[n]))

        return neighbourGrids

    def getNeighboursOfGridwDirection(self, currGrid: Grid, direction: int) -> list:
        neighbourCoords = currGrid.getNeighbours(direction)
        # print(neighbourCoords[0].getRow(), neighbourCoords[0].getCol() )
        # print(neighbourCoords[1].getRow(), neighbourCoords[1].getCol() )
        # print(neighbourCoords[2].getRow(), neighbourCoords[2].getCol() )
        # Make sure neighbour GridType is not a wall
        neighbourGrids = []
        for n in range(len(neighbourCoords)):
            neighbourGrid = self.getGrid(neighbourCoords[n])

            # If it's a wall, use current coordinate
            if (neighbourGrid.getGridType() == GridType.WALL):
                neighbourCoords[n] = currGrid

            neighbourGrids.append(self.getGrid(neighbourCoords[n]))
        return neighbourGrids

    # Prints Maze in the console
    def printer(self):
        for r in range(self.numRow):
            for c in range(self.numCol):
                currGrid = self.grids[r][c]

                if (currGrid.getGridType() != GridType.WALL):
                    # 1. Get utility (value)
                    utility = currGrid.getUtility()
                    # 2. Get grid type (letter)
                    gridType = currGrid.getGridType()
                    symbol = getSymbol(gridType)
                    # Get policy (arrow)
                    policy = currGrid.getPolicy()
                    policy = direction(policy)

                    print("| {} {:7.3f} {}".format(symbol, utility, policy), end = '')

                else:
                    print("|            ", end = '')
            print("|")
            print("-" * 13 * self.numCol)
        print("")


    def importMap(self):
        # Toggle for default map or random map
        for r in range(self.numRow):
            for c in range(self.numCol):
                type = map[r][c]
                self.grids[r][c].setGridType(type)