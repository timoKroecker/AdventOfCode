import os

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    results = []
    operator_lists = []
    for line in lines:
        line = line.replace("\n", "").split(":")
        results.append(int(line[0]))
        operator_lists.append(list(map(int, line[1].split(" ")[1:])))
    return results, operator_lists

#---------------------------------------------------------------------
#7.1

def has_term_1(res, left_op, ops):
    if ops == []:
        return res == left_op
    return (has_term_1(res, left_op + ops[0], ops[1:]) or
            has_term_1(res, left_op * ops[0], ops[1:]))

def get_calibration_res_1(results, operator_lists):
    sum_ = 0
    for i, ops in enumerate(operator_lists):
        res = results[i]
        if has_term_1(res, ops[0], ops[1:]):
            sum_ += res
    return sum_

#---------------------------------------------------------------------
#7.2

def has_term_2(res, left_op, ops):
    if ops == []:
        return res == left_op
    return (has_term_2(res, left_op + ops[0], ops[1:]) or
            has_term_2(res, left_op * ops[0], ops[1:]) or
            has_term_2(res, int(str(left_op) + str(ops[0])), ops[1:]))

def get_calibration_res_2(results, operator_lists):
    sum_ = 0
    for i, ops in enumerate(operator_lists):
        res = results[i]
        if has_term_2(res, ops[0], ops[1:]):
            sum_ += res
    return sum_

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    results, operator_lists = init_data()

    print("7.1:")
    print(get_calibration_res_1(results, operator_lists))
    print("")

    print("7.2:")
    print(get_calibration_res_2(results, operator_lists))
    print("")