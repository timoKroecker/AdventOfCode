import os
import time

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
    obstacles = set()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                obstacles.add((i, j))
    return obstacles

def turn(direction):
    return {
        UP: RIGHT,
        RIGHT: DOWN,
        DOWN:LEFT,
        LEFT: UP
    }[direction]

def is_in_map(guard, map_shape):
    return (guard[0] in range(map_shape[0]) and
            guard[1] in range(map_shape[1]))

def get_guard_path(map_shape, guard, obstacles):
    direction = UP
    visited = set()
    while is_in_map(guard, map_shape):
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

def get_loop_score(map_shape, guard, obstacles):
    direction = UP
    visited = set()
    while is_in_map(guard, map_shape):
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
    map_shape = (len(map), len(map[0]))
    guard = get_guard(map)
    obstacles = get_obstacles(map)
    visited = get_guard_path(map_shape, guard, obstacles)
    visited.remove(guard)
    num_loops = 0
    for pos in visited:
        obstacles.add(pos)
        num_loops += get_loop_score(map_shape, guard, obstacles)
        obstacles.remove(pos)
    return num_loops

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    lines = init_data()

    start_time = time.time()
    print("6.1:")
    print(len(get_guard_path(map_shape=(len(lines), len(lines[0])),
                             guard=get_guard(lines),
                             obstacles=get_obstacles(lines))))
    print("")

    print("6.2:")
    print(get_num_loops(lines))
    print("")
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
