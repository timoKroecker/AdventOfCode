import os

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    return [x.replace("\n", "") for x in lines]

#---------------------------------------------------------------------
#8.1

def get_frequencies(map) -> dict:
    freqs = {}
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if char == ".":
                continue
            if char in freqs.keys():
                freqs[char] = freqs[char] + [(i, j)]
            else:
                freqs[char] = [(i, j)]
    return freqs

def is_in_map(pos, map):
    return (pos[0] in range(len(map)) and
            pos[1] in range(len(map[0])))

def get_nodes_1(map, antennas):
    nodes = set()
    for antenna_1 in antennas:
        for antenna_2 in antennas:
            if antenna_1 == antenna_2:
                continue
            diff_x = antenna_1[0] - antenna_2[0]
            diff_y = antenna_1[1] - antenna_2[1]
            antinode = (antenna_1[0] + diff_x,
                        antenna_1[1] + diff_y)
            if is_in_map(antinode, map):
                nodes.add(antinode)
            antinode = (antenna_2[0] - diff_x,
                        antenna_2[1] - diff_y)
            if is_in_map(antinode, map):
                nodes.add(antinode)
    return nodes

def get_all_nodes_1(map):
    nodes = set()
    freqs = get_frequencies(map)
    for key in freqs.keys():
        nodes = nodes.union(get_nodes_1(map, freqs[key]))
    return nodes

#---------------------------------------------------------------------
#8.2

def get_nodes_2(map, antennas):
    nodes = set()
    for antenna_1 in antennas:
        for antenna_2 in antennas:
            if antenna_1 == antenna_2:
                continue
            
            diff_x = antenna_1[0] - antenna_2[0]
            diff_y = antenna_1[1] - antenna_2[1]

            antinode = antenna_1
            while is_in_map(antinode, map):
                nodes.add(antinode)
                antinode = (antinode[0] + diff_x,
                            antinode[1] + diff_y)
            antinode = antenna_1
            while is_in_map(antinode, map):
                nodes.add(antinode)
                antinode = (antinode[0] - diff_x,
                            antinode[1] - diff_y)
    return nodes

def get_all_nodes_2(map):
    nodes = set()
    freqs = get_frequencies(map)
    for key in freqs.keys():
        nodes = nodes.union(get_nodes_2(map, freqs[key]))
    return nodes

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    lines = init_data()

    print("8.1:")
    print(len(get_all_nodes_1(lines)))
    print("")

    print("8.2:")
    print(len(get_all_nodes_2(lines)))
    print("")