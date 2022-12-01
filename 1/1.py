import os
import numpy as np

#reading text file
with open(os.path.dirname(__file__) + '/data.txt') as file:
    lines = file.readlines()

#storing numbers in ndarrays
matrix = []
row = np.array([])
for line in lines:
    if(len(line) == 1):
        matrix.append(row)
        row = np.array([])
    else:
        row = np.append(row, int(line[:-1]))

#calculating and storing all sums
sums = np.array([])
for elem in matrix:
    sums = np.append(sums, np.sum(elem))

#calculating maximum
print("1.1:")
print(np.max(sums))
print("")

#storing the top three values and calculating their sum
print("1.2:")
top_three = np.array([])
for i in range(3):
    current_max = np.max(sums)
    top_three = np.append(top_three, current_max)
    sums = np.delete(sums, np.where(sums == current_max)[0][0])
print(np.sum(top_three))