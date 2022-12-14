import os
import numpy as np
import matplotlib.pyplot as plt

def get_start(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if(map[i][j] == -13):
                map[i][j] = 1
                return (i, j)
    return None

def get_end(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if(map[i][j] == -27):
                map[i][j] = 26
                return (i, j)
    return None

def init_map():
    #read text file
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    map = []

    for line in lines:
        row = [*line.replace("\n", "")]
        map.append([ord(i) - 96 for i in row])
    start_pos = get_start(map)
    end_pos = get_end(map)
    return np.array(map), start_pos, end_pos

def reachable_neighbours(height_map, position):
    num_rows , num_cols = height_map.shape
    neighbours = []
    up = position[0] - 1
    down = position[0] + 1
    left = position[1] - 1
    right = position[1] + 1
    if(up >= 0 and (height_map[position] - height_map[up, position[1]] <= 1)):
        neighbours.append((up, position[1]))
    if(down < num_rows and (height_map[position] - height_map[down, position[1]] <= 1)):
        neighbours.append((down, position[1]))
    if(left >= 0 and (height_map[position] - height_map[position[0], left] <= 1)):
        neighbours.append((position[0], left))
    if(right < num_cols and (height_map[position] - height_map[position[0], right] <= 1)):
        neighbours.append((position[0], right))
    return neighbours

def update_distances(height_map, distance_map, positions):
    next_positions = []
    for position in positions:
        neighbours = reachable_neighbours(height_map, position)
        for neighbour in neighbours:
            if(distance_map[neighbour] < 0 or distance_map[neighbour] > distance_map[position] + 1):
                distance_map[neighbour] = distance_map[position] + 1
                next_positions.append(neighbour)
    return distance_map, next_positions

def find_shortest_distances(height_map, distance_map):
    positions = [end_pos]
    while(len(positions) > 0):
        distance_map, positions = update_distances(height_map, distance_map, positions)
    return distance_map

def find_shortest_trail(height_map, distance_map, current_min):
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            if(height_map[i, j] == 1 and distance_map[i, j] >= 0):
                current_min = min(current_min, distance_map[i, j])
    return current_min

if __name__ == "__main__":
    height_map, start_pos, end_pos = init_map()
    distance_map = np.zeros((len(height_map), len(height_map[0])), int) - 50
    distance_map[end_pos] = 0
    distance_map = find_shortest_distances(height_map, distance_map)

    print("12.1:")
    print(distance_map[start_pos])
    print("")

    print("12.2:")
    print(find_shortest_trail(height_map, distance_map, distance_map[start_pos]))

    plt.imshow(distance_map)
    plt.show()