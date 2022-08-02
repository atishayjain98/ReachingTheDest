# ReachingTheDest

Algorithm which finds the shortest path from a cell A in the grid to a cell B in the grid, while only moving up, down, left or right through cells with passages. Log the route description to the console when done or an error message if no way was found. The grid should be represented as 2D list of booleans.

Program algorithm
* A 2-D grid of lists of boolean values is generated.
* Obstacles or False values can be appended to the grid using the random obstacle generator or predefined generator.
* The path is found using find_a_way() function which searches for the path without obstacles by searching the immediate neighbours of the queue point.
* The path if found is displayed, else the error that path is not found is shown.
