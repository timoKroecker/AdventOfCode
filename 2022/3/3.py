import os

#read text file
with open(os.path.dirname(__file__) + '/data.txt') as file:
    lines = file.readlines()

#return letter, shared by 2 arrays/strings
def find_letter(array1, array2):
    for letter1 in array1:
        for letter2 in array2:
            if(letter1 == letter2):
                return letter1
    return None

#return letter, shared by 3 arrays/strings
def find_badge(array1, array2, array3):
    for letter1 in array1:
        for letter2 in array2:
            if(letter1 == letter2):
                for letter3 in array3:
                    if(letter2 == letter3):
                        return letter1
    return None

#return priority value for letter
def get_prio(letter):
    ascii_num = ord(letter)
    if(ascii_num > 96):
        return ascii_num - 96
    if(ascii_num < 91):
        return ascii_num - 38
    return None

#first challenge
sum_prios = 0
for line in lines:
    half_len = len(line) // 2
    sum_prios += get_prio(find_letter(line[:half_len], line[half_len:]))
print("3.1:")
print(sum_prios)
print("")

#second challenge
sum_prios = 0
for i in range(0, len(lines), 3) :
    sum_prios += get_prio(find_badge(lines[i], lines[i + 1], lines[i + 2]))
print("3.2:")
print(sum_prios)