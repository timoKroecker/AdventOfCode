import os
import numpy as np

#returns inputdata as 2D matrix with a single tree hight in each coordinate
def init_forrest():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    forrest = np.zeros((len(lines), len(lines[0]) - 1), int)
    for i in range(len(lines)):
        forrest[i] = np.array([*lines[i].replace("\n", "")]).astype(int)
    return forrest

#-------------------------------------------------
#Task 1 Functions

def is_visible(ndarray, row, column):
    height = ndarray[row, column]
    if( row == 0 or row == ndarray.shape[0] - 1 or
        column == 0 or column == ndarray.shape[1] - 1):
        return 1
    if( height > np.max(ndarray[row, :column]) or
        height > np.max(ndarray[row, column + 1:]) or
        height > np.max(ndarray[:row, column]) or
        height > np.max(ndarray[row + 1:, column])):
        return 1
    return 0

def get_visible_trees(ndarray):
    rows, columns = ndarray.shape
    visible = 0
    for i in range(rows):
        for j in range(columns):
            visible += is_visible(ndarray, i, j)
    return visible

#-------------------------------------------------
#Task 2 Functions

def get_scenic_score_one_direction(our_height, view):
    score_factor = 0
    for tree_height in view:
        score_factor += 1
        if(tree_height >= our_height):
            break
    return score_factor

def get_scenic_score(ndarray, row, column):
    our_height = ndarray[row, column]
    score_factors = np.zeros(4, int)
    
    left = np.flip(ndarray[row, :column])
    right = ndarray[row, column + 1:]
    up = np.flip(ndarray[:row, column])
    down = ndarray[row + 1:, column]
    score_factors[0] = get_scenic_score_one_direction(our_height, left)
    score_factors[1] = get_scenic_score_one_direction(our_height, right)
    score_factors[2] = get_scenic_score_one_direction(our_height, up)
    score_factors[3] = get_scenic_score_one_direction(our_height, down)
    return np.prod(score_factors)

def get_best_scenic_score(ndarray):
    scores = np.array([], int)
    for i in range(ndarray.shape[0]):
        for j in range(ndarray.shape[1]):
            scores = np.append(scores, get_scenic_score(ndarray, i, j))
    return np.max(scores)

#-------------------------------------------------
#Main

if __name__ == "__main__":
    forrest = init_forrest()
    print("8.1:")
    print(get_visible_trees(forrest))
    print("")

    print("8.2:")
    print(get_best_scenic_score(forrest))