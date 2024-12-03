import os
import numpy as np

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    return lines

#---------------------------------------------------------------------
#11.1 / 11.2

def has_galaxies(string):
    for char in string:
        if char == "#":
            return True
    return False

def get_empty_rows(data):
    indices = []
    for i, row in enumerate(data):
        if not has_galaxies(row):
            indices.append(i)
    return indices

def get_empty_columns(data):
    indices = []
    for j in range(len(data[0])):
        column = [data[i][j] for i in range(len(data))]
        column = ''.join(x for x in column)
        if not has_galaxies(column):
            indices.append(j)
    return indices

def get_galaxy_positions(data):
    positions = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                positions.append((i, j))
    return positions

def get_galaxy_distances(data, expansion_rate):
    positions = get_galaxy_positions(data)
    empty_rows = get_empty_rows(data)
    empty_columns = get_empty_columns(data)
    distances = []
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i >= j:
                continue
            distance = (abs(positions[i][0] -
                            positions[j][0]) +
                        abs(positions[i][1] -
                            positions[j][1]))
            for index in empty_rows:
                if (index < max(positions[i][0],
                                positions[j][0]) and
                    index > min(positions[i][0],
                                positions[j][0])):
                    distance += expansion_rate - 1
            for index in empty_columns:
                if (index < max(positions[i][1],
                                positions[j][1]) and
                    index > min(positions[i][1],
                                positions[j][1])):
                    distance += expansion_rate - 1
            distances.append(distance)
    return np.array(distances)

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    universe = init_data()
    
    print("")
    print("11.1")
    print(np.sum(get_galaxy_distances(universe, 2)))

    print("")
    print("11.2")
    print(np.sum(get_galaxy_distances(universe, 1000000)))