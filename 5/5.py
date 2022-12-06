import os
import re

def init_stacks():
    #read text file
    with open(os.path.dirname(__file__) + '/stacks.txt') as file:
        stack_lines = file.readlines()

    stacks =    ["", "", "", "", "", "", "", "", ""]
    for line in stack_lines:
        i = 0
        in_brackets = False
        for letter in line:
            if(letter == "["):
                in_brackets = True
            elif(letter == "]"):
                in_brackets = False
            elif(in_brackets):
                if( ord(letter) >= 65 and
                    ord(letter) <= 90):
                    stacks[i] = stacks[i] + letter
                i += 1
    return stacks

def crate_mover_9000(stacks, source, destination):
    stacks[destination] = stacks[source][0] + stacks[destination]
    stacks[source] = stacks[source][1:]
    return stacks

def crate_mover_9001(stacks, source, destination, num_crates):
    stacks[destination] = stacks[source][0:num_crates] + stacks[destination]
    stacks[source] = stacks[source][num_crates:]
    return stacks

def get_top_elements(stacks):
    output = ""
    for stack in stacks:
        output = output + stack[0]
    return output

#-----------------------------------------------------

stacks_1 = init_stacks()
stacks_2 = init_stacks()

#read text file
with open(os.path.dirname(__file__) + '/moves.txt') as file:
    lines = file.readlines()

#execute moves on stacks
for line in lines:
    move = list(map(int, re.findall(r'\d+', line)))
    for i in range(move[0]):
        stacks_1 = crate_mover_9000(stacks_1, move[1] - 1, move[2] - 1)
    stacks_2 = crate_mover_9001(stacks_2, move[1] - 1, move[2] - 1, move[0])

print("5.1:")
print(get_top_elements(stacks_1))
print("")
print("5.2:")
print(get_top_elements(stacks_2))