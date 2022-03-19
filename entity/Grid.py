from .Coordinate import *
from .Policy import *
from .GridType import *
from .Config import *

class Grid(Coordinate):

	def __init__(self, coordinate: Coordinate):
		super().__init__(coordinate.getRow(), coordinate.getCol())
		self.utility = 0
		self.policy = Policy.UP
		self.gridType = GridType.WHITE

	def getUtility(self):
		return self.utility

	def setUtility(self, utility):
		self.utility = utility;

	def getPolicy(self):
		return self.policy

	def setPolicy(self, val : int):
		if (val == 0): #UP
			self.policy = Policy.UP
		elif (val == 1): #DOWN
			self.policy = Policy.DOWN
		elif (val == 2): #LEFT
			self.policy = Policy.LEFT
		elif (val == 3): #RIGHT
			self.policy = Policy.RIGHT
		else:
			self.policy = None
			print("unknown policy")

	def getGridType(self):
		return self.gridType

	def setGridType(self, type : str):
		if (type == 'W'):
			self.gridType = GridType.WHITE;
			self.setUtility(REWARD_WHITE);
		if (type == 'G'):
			self.gridType = GridType.GREEN;
			self.setUtility(REWARD_GREEN);
		if (type == 'B'):
			self.gridType = GridType.BROWN;
			self.setUtility(REWARD_BROWN);
		if (type == '#'):
			self.gridType = GridType.WALL;
			self.setUtility(REWARD_WALL);
