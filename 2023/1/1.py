import os

def init_lines():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    return lines

def get_digit_arrays_1(lines):
    digit_arrays = []

    for line in lines:
        digits = []
        for character in line:
            try:
                digits.append(int(character))
            except:
                pass
        digit_arrays.append(digits)

    return digit_arrays

def get_digit_arrays_2(lines):
    digit_arrays = []
    for line in lines:
        digits = []
        while(len(line) > 0):
            try:
                digits.append(int(line[0]))
            except:
                possible_digit = get_digit_from_words(line)
                if(possible_digit != None):
                    digits.append(possible_digit)
            line = line[1:]
        digit_arrays.append(digits)
    return digit_arrays

def get_digit_from_words(line):
    digit_words =   [
                        "one", "two", "three", "four",
                        "five", "six", "seven", "eight", "nine"
                    ]
    for index in range(len(digit_words)):
        if(line.find(digit_words[index]) == 0):
            return index + 1
    return None

def get_calibration_values(digit_arrays):
    calibration_values = []
    for digits in digit_arrays:
        number = int(str(digits[0]) + str(digits[-1]))
        calibration_values.append(number)
    return calibration_values

if __name__ == "__main__":
    lines = init_lines()

    digit_arrays_1 = get_digit_arrays_1(lines)
    calibration_values_1 = get_calibration_values(digit_arrays_1)
    print("")
    print("1.1:")
    print(sum(calibration_values_1))

    digit_arrays_2 = get_digit_arrays_2(lines)
    calibration_values_2 = get_calibration_values(digit_arrays_2)
    print("")
    print("1.2:")
    print(sum(calibration_values_2))