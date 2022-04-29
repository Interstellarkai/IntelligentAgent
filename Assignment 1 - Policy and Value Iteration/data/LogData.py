from entity.GridType import *
from entity.Config import *
from entity.Coordinate import *
from entity.Maze import *

class LogData:

	def __init__(self, maze : Maze):
		self.data = {}
		for r in range(NUM_ROW):
			for c in range(NUM_COL):
				if (maze.getGrid(Coordinate(r, c)).getGridType() == GridType.WALL):
					key = "Wall: (" + str(r) + ", " + str(c) + ")"
					self.data[key] = []
				else:
					key = "State: (" + str(r) + ", " + str(c) + ")"
					self.data[key] = []

	def add(self, maze : Maze):
		for r in range(NUM_ROW):
			for c in range(NUM_COL):
				# get the key name that was pre-defined by us
				if (maze.getGrid(Coordinate(r, c)).getGridType() == GridType.WALL):
					key = "Wall: (" + str(r) + ", " + str(c) + ")"
				else:
					key = "State: (" + str(r) + ", " + str(c) + ")"
				
				lst = self.data[key]
				lst.append(maze.getGrid(Coordinate(r, c)).getUtility())