import os
import re
import numpy as np

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    return "".join(line for line in lines).replace("\n", "")

#---------------------------------------------------------------------
#3.1

def get_muls(line):
    number = "\d{1,3}"
    regex = "mul\(" + number + "," + number + "\)"
    finds = re.findall(regex, line)
    array = [list(map(int, re.findall(r'\d+', find))) for find in finds]
    return np.sum(np.array([x[0] * x[1] for x in array]))

#---------------------------------------------------------------------
#3.2

def delete_disabled_sections(line):
    dont = "don't\(\)"
    do = "do\(\)"

    #winner of the ugliest code award goes to:
    dont_search = [(False, x.start()) for x in re.finditer(dont, line)]
    do_search = [(True, x.end()) for x in re.finditer(do, line)]
    total_search = sorted(dont_search + do_search, key=lambda x: x[1])
    delete_intervals = []
    start = None
    for element in total_search:
        if not element[0] and start is None:
            start = element[1]
        elif element[0] and start is not None:
            end = element[1]
            delete_intervals.append([start, end])
            start = None
    delete_intervals.reverse()
    for interval in delete_intervals:
        line = line[:interval[0]] + line[interval[1]:]
    return line

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    line = init_data()

    print("3.1:")
    print(get_muls(line))
    print("")

    line = delete_disabled_sections(line)

    print("3.2:")
    print(get_muls(line))
    print("")