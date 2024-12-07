import os
import copy

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    return [x.replace("\n", "") for x in lines]

#---------------------------------------------------------------------
#6.1

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def get_guard(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "^":
                return (i, j)
    return None

def get_obstacles(lines):
    obstacles = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                obstacles.append((i, j))
    return obstacles

def turn(direction):
    return {
        UP: RIGHT,
        RIGHT: DOWN,
        DOWN:LEFT,
        LEFT: UP
    }[direction]

def is_in_map(guard, map):
    return (guard[0] in range(len(map)) and
            guard[1] in range(len(map[0])))

def get_guard_path(map):
    guard = get_guard(map)
    direction = UP
    obstacles = get_obstacles(map)
    visited = set()
    while(is_in_map(guard, map)):
        visited.add(guard)
        new_pos = (guard[0] + direction[0],
                   guard[1] + direction[1])
        if new_pos in obstacles:
            direction = turn(direction)
        else:
            guard = new_pos
    return visited

#---------------------------------------------------------------------
#6.2

def get_loop_score(map):
    guard = get_guard(map)
    direction = UP
    obstacles = get_obstacles(map)
    visited = set()
    while(is_in_map(guard, map)):
        visited.add(guard + (direction,))
        new_pos = (guard[0] + direction[0],
                   guard[1] + direction[1])
        if new_pos + (direction,) in visited:
            return 1
        if new_pos in obstacles:
            direction = turn(direction)
        else:
            guard = new_pos
    return 0

def get_num_loops(map):
    visited = get_guard_path(map)
    visited.remove(get_guard(map))
    num_loops = 0
    for pos in visited:
        new_map = copy.deepcopy(map)
        new_map[pos[0]] = (new_map[pos[0]][:pos[1]] +
                           "#" +
                           new_map[pos[0]][pos[1] + 1:])
        num_loops += get_loop_score(new_map)
    return num_loops

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    lines = init_data()

    print("6.1:")
    print(len(get_guard_path(lines)))
    print("")

    print("6.2:")
    print("Hold on for about ten minutes...")
    print(get_num_loops(lines))
    print("")