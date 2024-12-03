import os
import numpy as np

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = np.array([int(x) for x in lines[i].replace("\n", "").split()])
    return lines

#---------------------------------------------------------------------
#9.1 / 9.2

def create_matrix(size):
    matrix = np.zeros((size - 1, size), int)
    for i in range(size - 1):
        matrix[i, i] = -1
        matrix[i, i + 1] = 1
    return matrix

def create_matrices(max_size):
    matrices = []
    for i in range(max_size):
        matrices.append(create_matrix(max_size - i))
    return matrices

def deduct_difference_vectors(matrices, input_vector):
    all_vectors = [input_vector]
    for matrix in matrices:
        if(not np.any(all_vectors[-1])):
            return all_vectors
        all_vectors.append(np.matmul(matrix, all_vectors[-1]))
    return None

def backward_pass(vector):
    while(len(vector) > 1):
        vector[-2] -= vector[-1]
        vector = vector[:-1]
    return vector[0]

def extrapolate(matrices, input_vector):
    vectors = deduct_difference_vectors(matrices, input_vector)
    return sum([vector[-1] for vector  in vectors]), backward_pass([vector[0] for vector  in vectors])

def get_extrapolation_sums(matrices, input_vectors):
    forward_sum = 0
    backward_sum = 0
    for input_vector in input_vectors:
        forward_value, backward_value = extrapolate(matrices, input_vector)
        forward_sum += forward_value
        backward_sum += backward_value
    return forward_sum, backward_sum

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    data = init_data()
    matrices = create_matrices(len(data[0]))
    forward_sum, backward_sum = get_extrapolation_sums(matrices, data)

    print("")
    print("9.1")
    print(forward_sum)

    print("")
    print("9.2")
    print(backward_sum)