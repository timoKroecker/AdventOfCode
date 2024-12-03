import os
import numpy as np

#---------------------------------------------------------------------
#init

def init_data_1():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    list = []
    for line in lines:
        string = line.replace("\n", "")
        elements = [int(x) for x in line.split() if x.isdigit()]
        list.append(elements)
    tupels = []
    for i in range(len(list[0])):
        tupels.append([list[0][i], list[1][i]])
    return tupels

def init_data_2():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    list = []
    for line in lines:
        string = line.replace("\n", "").replace(" ", "").replace(":", " ")
        list.append(int(string.split()[1]))
    return list

#---------------------------------------------------------------------
#6.1.

def get_number_of_ways_to_beat(time, distance):
    all_ways = np.arange(time + 1)
    all_ways = all_ways * (time - all_ways)
    the_ways = np.sign(np.sign(all_ways - distance) - 0.5)/2 + 0.5
    return int(sum(the_ways))

def get_winner_product(data):
    product = 1
    for tuple in data:
        product *= get_number_of_ways_to_beat(tuple[0], tuple[1])
    return product

#---------------------------------------------------------------------
#main

if __name__ == "__main__":

    data_1 = init_data_1()
    print("6.1.")
    print(get_winner_product(data_1))
    print("")

    data_2 = init_data_2()
    print("6.2.")
    print(get_number_of_ways_to_beat(data_2[0], data_2[1]))
    print("")