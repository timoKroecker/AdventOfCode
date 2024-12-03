import os

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    return [list(map(int, line.replace("\n", "").split(" ")))
            for line in lines]

#---------------------------------------------------------------------
#2.1

def is_asc_or_desc(report):
    differences = [report[i] - report[i + 1]
                   for i in range(len(report) - 1)]
    desc = all(x in [1, 2, 3] for x in differences)
    asc = all(x in [-1, -2, -3] for x in differences)
    return asc or desc

def get_safe_score(report):
    return {True: 1, False: 0}[is_asc_or_desc(report)]

#---------------------------------------------------------------------
#2.2

def get_dampened_safe_score(report):
    for i in range(len(report)):
        damp_rep = report[:i] + report[i + 1:]
        if is_asc_or_desc(damp_rep):
            return 1
    return 0

#---------------------------------------------------------------------
#main

def get_num_safe(data, dampened=False):
    num = 0
    for report in data:
        if dampened:
            num += get_dampened_safe_score(report)
        else:
            num += get_safe_score(report)
    return num

if __name__ == "__main__":
    data = init_data()
    
    print("2.1:")
    print(get_num_safe(data))
    print("")

    print("2.2:")
    print(get_num_safe(data, dampened=True))
    print("")