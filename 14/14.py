import os
import numpy as np
import matplotlib.pyplot as plt
import copy

AIR = 0
ROCK = 1
SAND = 2
SOURCE = 2

def add_rock_line_positions(string_1, string_2, rocks):
    position_1 = tuple([int(x) for x in string_1.split(",")])
    position_2 = tuple([int(x) for x in string_2.split(",")])
    for i in range(min(position_1[0], position_2[0]), max(position_1[0], position_2[0]) + 1):
        for j in range(min(position_1[1], position_2[1]), max(position_1[1], position_2[1]) + 1):
            rocks.add((j, i))
    return rocks

def init_map():
    #read text file
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    rocks = set()
    for line in lines:
        row = line.replace("\n", "").split(" -> ")
        for i in range(len(row) - 1):
            rocks = add_rock_line_positions(row[i], row[i + 1], rocks)
    return (0, 500), rocks

def get_down(position):
    return (position[0] + 1, position[1])

def get_down_left(position):
    return (position[0] + 1, position[1] - 1)

def get_down_right(position):
    return (position[0] + 1, position[1] + 1)

def get_dropped_position(position, rocks_and_sand, max_value, is_first_task):
    if(not is_first_task):
        max_value += 2
    if(position == None):
        return None
    if(position[0] + 1 > max_value and is_first_task):
        return None
    if(position[0] + 1 == max_value and not is_first_task):
        return position
    if(get_down(position) in rocks_and_sand):
        if(get_down_left(position) in rocks_and_sand):
            if(get_down_right(position) in rocks_and_sand):
                return position
            return get_down_right(position)
        return get_down_left(position)
    return get_down(position)

def drop_single_sand_batch(source, rocks_and_sand, max_value, is_first_task):
    destination = get_dropped_position(source, rocks_and_sand, max_value, is_first_task)
    while(source != destination):
        old_destination = destination
        destination = get_dropped_position(destination, rocks_and_sand, max_value, is_first_task)
        source = old_destination
    return destination

def drop_lots_of_sand(source, rocks, max_value, is_first_task):
    sand = []
    rocks_and_sand = copy.deepcopy(rocks)
    while(True):
        destination = drop_single_sand_batch(source, rocks_and_sand, max_value, is_first_task)
        if(destination == None):
            return sand
        sand.append(destination)
        rocks_and_sand.add(destination)
        if(destination == source):
            return set(sand)

def show_map(rocks, sand, source):
    mini_x = 0
    maxi_x = max(max([pos[0] for pos in rocks]), max([pos[0] for pos in sand]))
    mini_y = min(min([pos[1] for pos in rocks]), min([pos[1] for pos in sand]))
    maxi_y = max(max([pos[1] for pos in rocks]), max([pos[1] for pos in sand]))
    map = np.zeros((maxi_x - mini_x + 1, maxi_y - mini_y + 1))
    for position in rocks:
        map[position[0] - mini_x, position[1] - mini_y] = ROCK
    for position in sand:
        map[position[0] - mini_x, position[1] - mini_y] = SAND
    map[source[0] - mini_x, source[1] - mini_y] = SAND
    plt.imshow(map)
    plt.show()

if __name__ == "__main__":
    source, rocks = init_map()

    mini_x = 0
    maxi_x = max([position[0] for position in rocks])
    mini_y = min([position[1] for position in rocks])
    maxi_y = max([position[1] for position in rocks])

    sand_1 = drop_lots_of_sand(source, rocks, maxi_x, True)
    sand_2 = drop_lots_of_sand(source, rocks, maxi_x, False)

    print("14.1:")
    print(len(sand_1))
    print("")
    show_map(rocks, sand_1, source)

    print("14.2:")
    print(len(sand_2))
    show_map(rocks, sand_2, source)