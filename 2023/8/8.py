import os
import math

from Node import Node
from Network import Network

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    
    instructions = lines[0]
    maps = [[line[:3], line[7:10], line[12:15]] for line in lines[2:]]

    return instructions, create_network(maps)

def create_network(maps):
    network = Network()

    for entry in maps:
        node = Node(entry[0])
        network.add_node(node)

    all_nodes = network.get_all_nodes()
    for i in range(len(maps)):
        node = all_nodes[i]
        left = network.get_node_by_name(maps[i][1])
        right = network.get_node_by_name(maps[i][2])
        node.set_left(left)
        node.set_right(right)

    return network

#---------------------------------------------------------------------
#8.1

def traverse_network(instructions, network):
    current_node = network.get_root()
    steps = 0

    while(True):
        for character in instructions:
            current_node = current_node.get_child(character)
            steps += 1
            if(current_node.get_name() == "ZZZ"):
                return steps
            
#---------------------------------------------------------------------
#8.2

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def traverse_network_individually(instructions, root):
    current_node = root
    steps = 0
    counter = 0

    while(True):
        for character in instructions:
            current_node = current_node.get_child(character)
            steps += 1
            if(current_node.get_name()[-1] == "Z"):
                counter += 1
                if(counter == 2):
                    return steps
                steps = 0

def traverse_network_in_parallel(instructions, network):
    roots = network.get_roots()
    total_lcm = 1
    for root in roots:
        new_value = traverse_network_individually(instructions, root)
        total_lcm = lcm(total_lcm, new_value)
    return total_lcm

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    instructions, network = init_data()

    print("8.1")
    print(traverse_network(instructions, network))
    print("")

    print("8.2")
    print(traverse_network_in_parallel(instructions, network))
    print("")