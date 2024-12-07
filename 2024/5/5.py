import os
import re

#---------------------------------------------------------------------
#init

def init_data():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        text = file.read()
    rules, updates = text.split("\n\n")
    rules = [rule.split("|") for rule in rules.split("\n")]
    updates = [update.split(",") for update in updates.split("\n")]
    return rules, updates

#---------------------------------------------------------------------
#5.1

def is_rule_conform(rules, update):
    return all(len(re.findall(rule[1] + ".*" + rule[0],
                              ",".join(update))) == 0
                              for rule in rules)

def get_sum_corrects(rules, updates):
    sum_ = 0
    for update in updates:
        if is_rule_conform(rules, update):
            sum_ += int(update[len(update) // 2])
    return sum_

#---------------------------------------------------------------------
#5.2

def sort_update(rules, update):
    while not is_rule_conform(rules, update):
        for rule in rules:
            if len(re.findall(rule[1] + ".*" + rule[0],
                              ",".join(update))) == 0:
                continue
            left_inds = [i for i, x in enumerate(update)
                         if x == rule[1]]
            right_inds = [i for i, x in enumerate(update)
                         if x == rule[0]]
            update[left_inds[0]] = rule[0]
            update[right_inds[-1]] = rule[1]
    return update


def get_sum_incorrects(rules, updates):
    sum_ = 0
    for update in updates:
        if not is_rule_conform(rules, update):
            update = sort_update(rules, update)
            sum_ += int(update[len(update) // 2])
    return sum_

#---------------------------------------------------------------------
#main

if __name__ == "__main__":
    rules, updates = init_data()

    print("5.1:")
    print(get_sum_corrects(rules, updates))
    print("")

    print("5.2:")
    print(get_sum_incorrects(rules, updates))
    print("")