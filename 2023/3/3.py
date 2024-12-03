import os
import re

#--------------------------------------------------------------------------
#classes

class Number:

    def __init__(self, value):
        self.value = value
        self.symbols = []

    def get_value(self):
        return self.value
    
    def get_symbols(self):
        return self.symbols

    def set_all_symbols(self, all_symbols):
        self.symbols = all_symbols

    def has_symbols(self):
        return len(self.symbols) > 0

#--------------------------------------------------------------------------
#init

def init_lines():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")
    return lines

def lines_to_number_matrix(lines):
    number_matrix = []

    for i in range(len(lines)):
        row = []
        integer_strings = re.findall(r'\d+', lines[i])
        for string in integer_strings:
            j = lines[i].find(string)
            lines = erase_number((i, j), len(string), lines)
            symbols = get_symbols((i, j), len(string), lines)
            number = Number(int(string))
            number.set_all_symbols(symbols)
            row.append(number)
        number_matrix.append(row)
    return number_matrix

def get_symbols(position, number_size, lines):
    symbols = []
    for i in range(3):
        for j in range(number_size + 2):
            try:
                x = position[0] - 1 + i
                y = position[1] - 1 + j
                character = lines[x][y]
                if(x >= 0 and y >= 0 and is_symbol(character)):
                    symbols.append([character, (x, y)])
            except:
                pass
    return symbols

def is_symbol(character):
    return ".0123456789".find(character) == -1

def erase_number(position, number_size, lines):
    for i in range(number_size):
        lines[position[0]] = lines[position[0]][:position[1] + i] + "." + lines[position[0]][position[1] + i + 1:]
    return lines

#--------------------------------------------------------------------------
#3.1

def sum_of_part_numbers(number_matrix):
    sum = 0
    for row in number_matrix:
        for number in row:
            if(number.has_symbols()):
                sum += number.get_value()
    return sum

#--------------------------------------------------------------------------
#3.2

def sum_of_gear_ratios(number_matrix, lines):
    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            sum += get_gear_ratio((i, j), number_matrix, lines)
    return sum

def get_gear_ratio(position, number_matrix, lines):
    if(lines[position[0]][position[1]] != "*"):
        return 0
    surrounding_values = get_surrounding_values(["*", position], number_matrix)
    if(len(surrounding_values) != 2):
        return 0
    return surrounding_values[0] * surrounding_values[1]
    

def get_surrounding_values(symbol, number_matrix):
    values = []
    position = symbol[1]
    for i in range(3):
        x = position[0] - 1 + i
        if(x >= 0):
            for number in number_matrix[x]:
                if(symbol in number.get_symbols()):
                    values.append(number.get_value())
    return values

#--------------------------------------------------------------------------
#main

if __name__ == "__main__":
    lines = init_lines()
    number_matrix = lines_to_number_matrix(lines)

    print("")
    print("3.1:")
    print(sum_of_part_numbers(number_matrix))

    print("")
    print("3.2:")
    print(sum_of_gear_ratios(number_matrix, lines))