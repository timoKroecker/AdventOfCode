import os
import re
import numpy as np

#---------------------------------------------------------------------
#init

def init_lines():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        split_index = lines[i].find(":") + 2
        lines[i] = lines[i][split_index:].replace("\n", "")

    return lines

def lines_to_data(lines):
    data = []
    for line in lines:
        split = line.split("|")
        winning_nums = re.findall(r'\d+', split[0])
        my_nums = re.findall(r'\d+', split[1])
        data.append([winning_nums, my_nums])
    return data

#-------------------------------------------------------------------------
#3.1

def sum_points(data):
    sum = 0

    for card in data:
        hits = len(set.intersection(set(card[0]), set(card[1])))
        if(hits > 0):
            sum += (pow(2, hits - 1))
    return sum

#-------------------------------------------------------------------------
#3.2

def sum_scratch_cards(data):
    num_scratchcards = np.ones(len(data))
    
    for i in range(len(data)):
        hits = len(set.intersection(set(data[i][0]), set(data[i][1])))
        for j in range(hits):
            index = i + j + 1
            try:
                num_scratchcards[index] += num_scratchcards[i]
            except:
                pass
    return int(np.sum(num_scratchcards))

#---------------------------------------------------------------------------
#main

if __name__ == "__main__":
    lines = init_lines()
    data = lines_to_data(lines)

    print("")
    print("4.1:")
    print(sum_points(data))

    print("")
    print("4.2:")
    print(sum_scratch_cards(data))