# File Structure
    Value and Policy Iteration of Maze
## Main Package:
|  | File name  | Description  |
| :-: | :-: | :-: |
| 1 | ValueIteration.py | The executable file for the value iteration. (Variable C value) |
| 2 | PolicyIteration.py | The executable file for the value iteration. (Variable K value) |
     
## Entity Package:
|  | File name  | Description  |
| :-: | :-: | :-: |
| 1 | Config.py | For initialization of Maze.py (Constants, Default and Random Maze) |
| 2 | Coordinate.py | To move about the maze, using coordinates increment/decrement |
| 3 | Grid.py | Has Policy, Utility, GridType. These are then broken into subcomponents |
| 4 | GridType.py | An enumeration of grid type and its reward |
| 5 | Maze.py | Aggregation of grids; To get specified and neighboring grids |
| 6 | Policy.py | An enumeration of directions that agent can take |
| 7 | RandomMap.py | Generate Random Maze for Part 2 |

## Data Package:
|  | File name  | Description  |
| :-: | :-: | :-: |
| 1 | LogData.py | Dictionary to store the state's corresponding utility value after each iteration |
| 2 | Plot.py | Using pyplot to generate graph using the data logged from the main algorithm |
