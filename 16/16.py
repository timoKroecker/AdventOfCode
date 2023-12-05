import os

from network import Network
from network import Node

import itertools

TIME_TASK_1 = 30

def init_network():
    #read text file
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    network = Network()
    successor_names = []

    for line in lines:
        string_snippets = line.replace("\n", "")
        string_snippets = string_snippets.replace(",", "")
        string_snippets = string_snippets.replace(";", "")
        string_snippets = string_snippets.split(" ")

        name = string_snippets[1]
        flow = int(string_snippets[4][5:])
        successors = string_snippets[9:]
        successor_names.append((name, successors))

        network.add_node(Node(name, flow))

    for tuple in successor_names:
        node = network.get_node_by_name(tuple[0])
        for name in tuple[1]:
            successor = network.get_node_by_name(name)
            node.add_successor(successor)

    network.set_start_node()

    return network

if __name__ == "__main__":
    network = init_network()

    print("16.1:")
    #print(network.get_max_released_pressure(TIME_TASK_1))
    print("")

    print("BEF")
    permutations = list(itertools.permutations([1, 2, 3, 4, 5, 6]))
    print(len(permutations))
    print("AFT")