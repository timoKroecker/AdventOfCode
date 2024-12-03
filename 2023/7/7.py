import os
import numpy as np

#---------------------------------------------------------------------
#init

def init_data(assignment):
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    full_string = ""
    for line in lines:
        full_string += line
    lines = full_string.split("\n")
    tuples = [x.split() for x in lines]
    return [[convert_to_np_array(x, assignment), int(y)] for [x, y] in tuples]

def convert_to_np_array(string, assignment):
    card_values_1 =     {
                            "2": 2,
                            "3": 3,
                            "4": 4,
                            "5": 5,
                            "6": 6,
                            "7": 7,
                            "8": 8,
                            "9": 9,
                            "T": 10,
                            "J": 11,
                            "Q": 12,
                            "K": 13,
                            "A": 14
                        }
    card_values_2 =     {
                            "2": 2,
                            "3": 3,
                            "4": 4,
                            "5": 5,
                            "6": 6,
                            "7": 7,
                            "8": 8,
                            "9": 9,
                            "T": 10,
                            "J": 1,
                            "Q": 12,
                            "K": 13,
                            "A": 14
                        }
    all_card_values =   {
                            1: card_values_1,
                            2: card_values_2
                        }
    array = np.zeros(5)
    for i in range(len(string)):
        array[i] = all_card_values[assignment][string[i]]
    return array

#---------------------------------------------------------------------
#7.1 / 7.2

def custom_remove(array, element):
    prev_length = len(array)
    array = np.delete(array, np.where(array == element)[0])
    return array, prev_length - len(array)

def get_type(array, assignment):
    hand_type = {}
    for i in range(5):
        hand_type[i + 1] = {}
    hand_type[1][5] = 1     #high card
    hand_type[2][4] = 2     #one pair
    hand_type[2][3] = 3     #two pair
    hand_type[3][3] = 4     #three oak
    hand_type[3][2] = 5     #full house
    hand_type[4][2] = 6     #four oak
    hand_type[5][1] = 7     #five oak

    highest_occurance = None
    num_uniques = None
    if(assignment == 1):
        unique, counts = np.unique(array, return_counts=True)
        highest_occurance = np.sort(counts)[-1]
        num_uniques = len(unique)
    elif(assignment == 2):
        copy = np.copy(array)
        copy, num_Js = custom_remove(copy, 1)
        unique, counts = np.unique(copy, return_counts=True)
        if(len(counts) == 0):
            return hand_type[5][1]
        highest_occurance = np.sort(counts)[-1] + num_Js
        num_uniques = len(unique)
    return hand_type[highest_occurance][num_uniques]

def is_first_hand_better(hand_1, hand_2, assignment):
    type_difference = get_type(hand_1, assignment) - get_type(hand_2, assignment)
    
    if(type_difference < 0):
        return False
    if(type_difference > 0):
        return True
    
    for i in range(5):
        card_difference = hand_1[i] - hand_2[i]
        if(card_difference < 0):
            return False
        if(card_difference > 0):
            return True
    print("we should have never gotten here")
    return False

def get_insert_index(sorted_tuples, new_tuple, assignment):
    lower_bound = 0
    upper_bound = len(sorted_tuples)

    if(len(sorted_tuples) > 0
       and not is_first_hand_better(new_tuple[0], sorted_tuples[0][0], assignment)):
        return 0

    while (upper_bound - lower_bound > 1):
        middle = lower_bound + (upper_bound - lower_bound) // 2
        if(is_first_hand_better(new_tuple[0], sorted_tuples[middle][0], assignment)):
            lower_bound = middle
        else:
            upper_bound = middle
    return upper_bound
    
def sort_tuples(tuples, assignment):
    sorted_tuples = []
    while(len(tuples) > 0):
        new_tuple = tuples.pop(0)
        index = get_insert_index(sorted_tuples, new_tuple, assignment)
        sorted_tuples = sorted_tuples[:index] + [new_tuple] + sorted_tuples[index:]
    return sorted_tuples

def get_vector_product(tuples, assignment):
    sorted_tuples = sort_tuples(tuples, assignment)
    sorted_bets = np.array([x[1] for x in sorted_tuples])
    ranks = np.arange(len(sorted_bets)) + 1

    return np.matmul(sorted_bets, ranks)
#---------------------------------------------------------------------
#main

if __name__ == "__main__":

    print("7.1")
    task = 1
    tuples = init_data(task)
    print(get_vector_product(tuples, task))
    print("")

    print("7.2")
    task = 2
    tuples = init_data(task)
    print(get_vector_product(tuples, task))
    print("")