from .Config import *

class Coordinate(object):

	def __init__(self, row: int, col : int):
		self.UP = 0
		self.DOWN = 1
		self.LEFT = 2
		self.RIGHT = 3
		
		if (col < 0 or row < 0):
			raise Exception("Col and Row must be a positive integer.") 
		elif (col > NUM_COL - 1):
			raise Exception("Col out of range.");
		elif (row > NUM_ROW - 1):
			raise Exception("Row out of range.");
		else:
			self.row = row;
			self.col = col;
	

	def getCol(self):
		return self.col

	def getRow(self):
		return self.row

	# List of neighboring coordinate accordong to direction
	def getNeighbours(self, direction: int) -> list:
		coordinates = []

		offset = [
				[ [ -1, 0 ], [ 0, -1 ], [ 0, +1 ] ], # Up-Forward, Up-Left, Up-Right
				[ [ +1, 0 ], [ 0, +1 ], [ 0, -1 ] ], # Down-Forward, Down-Left, Down-Right

				[ [ 0, -1 ], [ +1, 0 ], [ -1, 0 ] ], # Left-Forward, Left-Left, Left-Right
				[ [ 0, +1 ], [ -1, 0 ], [ +1, 0 ] ]  # Right-Forward, Right-Left, Right-Right
				]

		# Up
		try:
			coordinate = Coordinate(self.row + offset[direction][0][0], self.col + offset[direction][0][1])
			coordinates.append(coordinate)
		except:
			coordinate = Coordinate(self.row, self.col)
			coordinates.append(coordinate)
		# Left
		try:
			coordinate = Coordinate(self.row + offset[direction][1][0], self.col + offset[direction][1][1])
			coordinates.append(coordinate)
		except:
			coordinate = Coordinate(self.row, self.col)
			coordinates.append(coordinate)
		# Right
		try:
			coordinate = Coordinate(self.row + offset[direction][2][0], self.col + offset[direction][2][1])
			coordinates.append(coordinate)
		except:
			coordinate = Coordinate(self.row, self.col)
			coordinates.append(coordinate)

		return coordinates

