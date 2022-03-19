import enum
from .Config import *

class GridType(enum.Enum):
	WHITE = enum.auto()
	GREEN = enum.auto()
	BROWN = enum.auto()
	WALL = enum.auto()

def getReward(GridType : GridType):
	if (GridType == GridType.WHITE):
		return REWARD_WHITE
	elif (GridType == GridType.GREEN):
		return REWARD_GREEN
	elif (GridType == GridType.BROWN):
		return REWARD_BROWN
	elif (GridType == GridType.WALL):
		return REWARD_WALL
	else:
		print("getReward: unknown grid type")
		return float(0)

def getSymbol(GridType : GridType):
	if (GridType == GridType.WHITE):
		return "W"
	elif (GridType == GridType.GREEN):
		return "G"
	elif (GridType == GridType.BROWN):
		return "B"
	elif (GridType == GridType.WALL):
		return "X"
	else:
		print("getSymbol: unknown grid type")
		return ""
