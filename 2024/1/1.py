import os
import numpy as np

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    left = []
    right = []
    for line in lines:
        row_values = line.replace("\n", "").split("   ")
        left.append(int(row_values[0]))
        right.append(int(row_values[1]))
    return sorted(left), sorted(right)

#---------------------------------------------------------------------
#1.1

def get_total_distance(left, right):
    distances = [abs(left[i] - right[i])
                 for i in range(len(left))]
    return np.sum(np.array(distances))

#---------------------------------------------------------------------
#1.2

def get_similarity_score(left, right):
    score = 0
    for number in left:
        score += number * len([x for x in right
                               if x == number])
    return score

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    left, right = init_data()
    
    print("1.1:")
    print(get_total_distance(left, right))
    print("")

    print("1.2:")
    print(get_similarity_score(left, right))
    print("")