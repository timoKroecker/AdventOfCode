import os

class Monkey:

    def __init__(self, name, starting_items, operation, test):
        self.name = name
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.true_monkey = None
        self.false_monkey = None
        self.inspections = 0

    def get_name(self):
        return self.name

    def get_items(self):
        return self.items

    def get_test(self):
        return self.test

    def get_inspections(self):
        return self.inspections

    def set_true_monkey(self, true_monkey):
        self.true_monkey = true_monkey

    def set_false_monkey(self, false_monkey):
        self.false_monkey = false_monkey

    def turn_1(self):
        for old in self.items:
            self.inspections += 1
            old = (eval(self.operation)) // 3
            if(old % self.test == 0):
                self.true_monkey.catch(old)
            else:
                self.false_monkey.catch(old)
        self.items = []

    def turn_2(self):
        for old in self.items:
            self.inspections += 1
            new = eval(self.operation)
            mod = new % self.test
            if(mod == 0.0):
                self.true_monkey.catch(new)
            else:
                self.false_monkey.catch(new)
        self.items = []

    def catch(self, item):
        self.items.append(item)

    def adjust_stress(self, test_product):
        for i in range(len(self.items)):
            self.items[i] = self.items[i] % test_product

def crop_line(lines, lines_per_monkey, index, element):
    return lines[lines_per_monkey * index  + element].replace(",", "").replace("\n", "")

def get_monkey_by_name(monkeys, name):
    for monkey in monkeys:
        if(monkey.get_name() == name):
            return monkey
    return None

def init_monkeys():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    lines_per_monkey = 7
    monkeys = []
    for i in range(len(lines) // lines_per_monkey):
        starting_items = [eval(x) for x in crop_line(lines, lines_per_monkey, i, 1).split(" ")[4:]]
        operation = crop_line(lines, lines_per_monkey, i, 2)[19:]
        test = int(crop_line(lines, lines_per_monkey, i, 3).split(" ")[-1])
        new_monkey = Monkey(i, starting_items, operation, test)
        monkeys.append(new_monkey)
    for i in range(len(lines) // lines_per_monkey):
        current_monkey = get_monkey_by_name(monkeys, i)
        true_monkey = get_monkey_by_name(monkeys, int(crop_line(lines, lines_per_monkey, i, 4)[-1]))
        false_monkey = get_monkey_by_name(monkeys, int(crop_line(lines, lines_per_monkey, i, 5)[-1]))
        current_monkey.set_true_monkey(true_monkey)
        current_monkey.set_false_monkey(false_monkey)
    return monkeys

def round_1(monkeys):
    for monkey in monkeys:
        monkey.turn_1()

def round_2(monkeys, test_product):
    for monkey in monkeys:
        monkey.adjust_stress(test_product)
    for monkey in monkeys:
        monkey.turn_2()

def get_monkey_business(monkeys):
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.get_inspections())
    inspections.sort()
    return inspections[-1] * inspections[-2]

def get_test_product(monkeys):
    test_product = 1
    for monkey in monkeys:
        test_product *= monkey.get_test()
    return test_product

if __name__ == "__main__":
    monkeys_1 = init_monkeys()
    monkeys_2 = init_monkeys()
    for i in range(20):
        round_1(monkeys_1)
    for i in range(10000):
        round_2(monkeys_2, get_test_product(monkeys_2))
    
    print("11.1:")
    print(get_monkey_business(monkeys_1))
    print("")
    print("11.2:")
    print(get_monkey_business(monkeys_2))