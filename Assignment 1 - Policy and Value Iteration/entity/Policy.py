import enum
from .Config import *

class Policy(enum.Enum):
	# to get value: use "Policy.UP.value"
	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3

def direction(Policy : Policy):
	if (Policy == Policy.UP):
		return "\u2191"
	elif (Policy == Policy.DOWN):
		return "\u2193"
	elif (Policy == Policy.LEFT):
		return "\u2190"
	elif (Policy == Policy.RIGHT):
		return "\u2192"
	else:
		print("Policy: Unknown direction")
		return None

def getValue(Policy) -> int:
	return Policy.value
