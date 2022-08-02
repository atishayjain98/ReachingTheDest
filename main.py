import collections, random


# for random set of obstacles
def random_generate_obstacles():
    obstacle = [(random.randrange(0, 10), random.randrange(0, 10)) for i in range(6)]
    for i in obstacle:
        x, y = i
        array_grid[x][y] = False
    return obstacle


# for given obstacles 
def generate_obstacles():
    array_grid[0][5] = array_grid[2][3] = array_grid[3][5] = array_grid[3][4] = array_grid[6][7] = array_grid[8][
        9] = False
    obstacless = [(0, 5), (2, 3), (3, 5), (3, 4), (6, 7), (8, 9)]
    return obstacless


def find_a_way():
    queue = collections.deque([[start_point]])
    already_checked = set(start_point)

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if y == end_point[1] and x == end_point[0]:
            print("Hurray ! You made it by taking the path - ", path)
            return path
        # checking top,bottom, right and left of node if there is obstacle
        for x1, y1 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x1 < len(array_grid) and 0 <= y1 < len(array_grid) and array_grid[x1][y1] != False and (
                    x1, y1) not in already_checked:
                queue.append(path + [(x1, y1)])
                already_checked.add((x1, y1))
    print("Ah! You are stuck !!!")


rows = []
columns = []

rows, cols = (10, 10)
# method 2b
array_grid = [[True for i in range(cols)] for j in range(rows)]

start_point = (input("Enter start point as x,y (range is from 0-9) : "))
start_point = tuple(map(int, start_point.split(",")))
end_point = (input("Enter end point as x,y (range is from 0-9) : "))
end_point = tuple(map(int, end_point.split(",")))

generate_obstacles()                # if we want to take it from pre-defined obstacle
# random_generate_obstacles()       # if we want to take it from random obstacle
if end_point in generate_obstacles():       # for random change generate_obstacles() to random_generate_obstacles() 
    print("Uh ho, The end point is an obstacle, cant reach there !")
else:
    find_a_way()
