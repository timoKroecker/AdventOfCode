import os

def init_moves():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    moves = []
    for line in lines:
        move = line.replace("\n", "").split(" ")
        if(len(move) == 2):
            move[1] = int(move[1])
        moves.append(move)
    return moves

def is_measured(cycles):
    for i in range(6):
        if(cycles == 40 * i + 20):
            return True
    return False

def update(cycles, x, signal_strenghts):
    if(is_measured(cycles)):
        signal_strenghts.append(x * cycles)
    return cycles + 1, signal_strenghts

def init_crt():
    crt = []
    for i in range(6):
        row = []
        for j in range(40):
            row += "."
        crt.append(row)
    return crt

def draw_crt_pixel(cycles, x, crt):
    position = ((cycles - 1) // 40, (cycles - 1) % 40)
    if(len(set([x - 1, x, x + 1, position[1]])) == 3):
        crt[position[0]][position[1]] = "#"
    return crt

if __name__ == "__main__":
    commands = init_moves()
    x = 1
    cycles = 1
    signal_strenghts = []
    crt = init_crt()
    for command in commands:
        crt = draw_crt_pixel(cycles, x, crt)
        cycles, signal_strenghts = update(cycles, x, signal_strenghts)
        if(command[0] == "addx"):
            crt = draw_crt_pixel(cycles, x, crt)
            cycles, signal_strenghts = update(cycles, x, signal_strenghts)
            x += command[1]
    
    print("10.1:")
    print(sum(signal_strenghts))
    print("")

    print("10.2:")
    for row in crt:
        for character in row:
            print(character, end="")
        print("")