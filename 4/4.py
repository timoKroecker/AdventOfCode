import os
import re
import numpy as np

#read text file
with open(os.path.dirname(__file__) + '/data.txt') as file:
    lines = file.readlines()

def total_containment(array):
    if(array[0] <= array[2] and array[1] >= array[3]):
        return True
    if(array[0] >= array[2] and array[1] <= array[3]):
        return True
    return False

def any_overlap(array):
    if(array[0] <= array[3] and array[1] >= array[2]):
        return True
    if(array[1] >= array[2] and array[0] <= array[3]):
        return True
    return False

overlap_score = 0
containment_score = 0
for line in lines:
    nums = list(map(int, re.findall(r'\d+', line)))
    if(any_overlap(nums)):
        overlap_score += 1
        if(total_containment(nums)):
            containment_score += 1
print("4.1:")
print(containment_score)
print("")
print("4.2:")
print(overlap_score)