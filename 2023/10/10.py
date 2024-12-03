import os
import numpy as np
import operator
import matplotlib.pyplot as plt

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

#DRY and PIPE must be fixed to -1 and 1 respectively
DRY = -1
FLOODED = 0
PIPE = 1

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    return lines

#---------------------------------------------------------------------
#10.1

def add_tuples(a, b):
    return tuple(map(operator.add, a, b))

def subtract_tuples(a, b):
    return tuple(map(operator.sub, a, b))

def get_start(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if(data[i][j] == "S"):
                return (i, j)
    return None

def get_next_direction(previous_direction, pipe_type):
    directions =    {
                        "-": [LEFT, RIGHT],
                        "|": [UP, DOWN],
                        "F": [DOWN, RIGHT],
                        "L": [UP, RIGHT],
                        "J": [UP, LEFT],
                        "7": [DOWN, LEFT]
                    }
    possible_directions = directions[pipe_type]
    for direction in possible_directions:
        if(add_tuples(direction, previous_direction) != (0, 0)):
            return direction
    return None

def init_queue(start, map):
    queue = []
    directions = [UP, DOWN, LEFT, RIGHT]
    possible_pipe_types =   {
                                DOWN: ["|", "J", "L"],
                                UP: ["|", "7", "F"],
                                RIGHT: ["-", "J", "7"],
                                LEFT: ["-", "L", "F"]
                            }
    for direction in directions:
        new_position = add_tuples(start, direction)
        pipe_type = map[new_position[0]][new_position[1]]
        if(pipe_type in possible_pipe_types[direction]):
            queue.append([start, direction])
    return queue

def calculate_distances(map, start):
    distances = np.zeros((len(map), len(map[0]))).astype(int) - 1000
    distances[start[0], start[1]] = 0
    queue = init_queue(start, map)
    current_distance = 1
    while(len(queue) > 0):
        new_queue = []
        for element in queue:
            old_position = element[0]
            direction = element[1]
            new_position = add_tuples(old_position, direction)
            if(distances[new_position[0], new_position[1]] < 0):
                distances[new_position[0],
                          new_position[1]] = current_distance
                pipe_type = map[new_position[0]][new_position[1]]
                new_queue.append([new_position,
                                  get_next_direction(direction,
                                                     pipe_type)])
        queue = new_queue
        current_distance += 1
    return distances

#---------------------------------------------------------------------
#10.2

def get_circle(distances, map):
    start = get_start(map)
    circle = np.sign((distances - 0.5)).astype(int)
    circle[start[0], start[1]] = 1

    return circle            

def get_unvisited_neighbors(position, map):
    neighbors = []
    for direction in DIRECTIONS:
        new_position = add_tuples(position, direction)
        if (new_position[0] >= 0 and
            new_position[1] >= 0 and
            new_position[0] < len(map) and
            new_position[1] < len(map[0]) and
            map[new_position[0], new_position[1]] == DRY):
            neighbors.append(new_position)
    return neighbors

def flood_map(map):
    map = np.copy(map)
    if map[0, 0] == PIPE:
        print("Map cannot be flooded from start " +
              "(0, 0),\nbecause there is a pipe.")
        return map
    start = (0, 0)
    map[start[0], start[1]] = FLOODED
    queue = [start]
    while(len(queue) > 0):
        new_queue = []
        for position in queue:
            new_queue += get_unvisited_neighbors(position, map)
        for position in new_queue:
            map[position[0], position[1]] = FLOODED
        queue = list(set(new_queue))
    return map

def upscale_s(map):
    start = get_start(map)
    queue = init_queue(start, map)
    big_s = [
        [".", "|", "."],
        ["-", "S", "-"],
        [".", "|", "."],
    ]
    for elem in DIRECTIONS:
        if elem not in [x[1] for x in queue]:
            i = 1 + elem[0]
            j = 1 + elem[1]
            big_s[i][j] = "."
    return big_s

def upscale_map(map):
    big_by_symbol = {
        "-":[
            [".", ".", "."],
            ["-", "-", "-"],
            [".", ".", "."],
        ],
        "|":[
            [".", "|", "."],
            [".", "|", "."],
            [".", "|", "."],
        ],
        "F":[
            [".", ".", "."],
            [".", "F", "-"],
            [".", "|", "."],
        ],
        "L":[
            [".", "|", "."],
            [".", "L", "-"],
            [".", ".", "."],
        ],
        "J":[
            [".", "|", "."],
            ["-", "J", "."],
            [".", ".", "."],
        ],
        "7":[
            [".", ".", "."],
            ["-", "7", "."],
            [".", "|", "."],
        ],
        ".":[
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."],
        ],
    }
    big_by_symbol["S"] = upscale_s(map)
    new_map = []
    for i in range(3 * len(map)):
        new_map.append([])
    for i, row in enumerate(map):
        for symbol in row:
            big_symbol = big_by_symbol[symbol]
            big_row_index = i * 3
            for k in range(3):
                new_map[big_row_index + k] += big_symbol[k]
    return new_map

def downscale_map(map):
    new_shape = tuple(x//3 for x in map.shape)
    new_map = np.zeros(new_shape)
    for i in range(len(new_map)):
        for j in range(len(new_map[0])):
            new_map[i, j] = map[3 * i + 1, 3 * j + 1]
    return new_map

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    data = init_data()

    big_map = upscale_map(data)
    big_distances = calculate_distances(big_map, get_start(big_map))
    
    print("")
    print("10.1")
    print(np.max(big_distances) // 3)

    circle = get_circle(big_distances, big_map)
    flooded_circle = flood_map(circle)
    small_map = downscale_map(flooded_circle)
    enclosed_tiles = (np.sign(-1 * small_map - 0.5) / 2 + 0.5).astype(int)
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    plt.imshow(small_map, cmap='hot', interpolation='nearest')
    plt.savefig(dir_path + '/flooded_map.png')
    plt.imshow(enclosed_tiles, cmap='hot', interpolation='nearest')
    plt.savefig(dir_path + '/enclosed_tiles.png')

    print("")
    print("10.2")
    print(np.sum(enclosed_tiles))