import os
import re

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    return [x.replace("\n", "") for x in lines]

#---------------------------------------------------------------------
#4.1

def count_xmas(lines):
    count = 0
    for line in lines:
        for regex in ["XMAS", "SAMX"]:
            count += len(re.findall(regex, line))
    return count

def get_rotation(lines):
    return ["".join(char for char in tuple_)
            for tuple_ in list(zip(*lines[::-1]))]

def get_diagonals(lines):
    num_diags = len(lines) + len(lines[0]) - 1
    diags = ["" for i in range(num_diags)]
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            diags[i + j] += char
    return diags

def count_all_xmas(lines):
    count = count_xmas(lines)
    count += count_xmas(get_diagonals(lines))
    lines = get_rotation(lines)
    count += count_xmas(lines)
    count += count_xmas(get_diagonals(lines))
    return count

#---------------------------------------------------------------------
#4.2

def count_x_mas(lines):
    count = 0
    for i, line in enumerate(lines):
        if i in [0, len(lines) - 1]:
            continue
        for j, char in enumerate(line):
            if (j in [0, len(line) - 1] or
                char != "A"):
                continue
            spikes = [lines[i + 1][j + 1],
                      lines[i + 1][j - 1],
                      lines[i - 1][j + 1],
                      lines[i - 1][j - 1]]
            if (spikes.count("M") + spikes.count("S") != 4 or
                spikes[0] == spikes[3] or
                spikes[1] == spikes[2]):
                continue
            count += 1
    return count

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    lines = init_data()

    print("4.1:")
    print(count_all_xmas(lines))
    print("")

    print("4.2:")
    print(count_x_mas(lines))
    print("")