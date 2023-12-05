import os

def init_moves():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()
    moves = []
    for line in lines:
        move = line.replace("\n", "").split(" ")
        move[1] = int(move[1])
        moves.append(move)
    return moves

def get_new_pos(old_pos, movement):
    return (old_pos[0] + movement[0], old_pos[1] + movement[1])

def get_new_head_pos(head, move):
    movement =  {
                        "L":    (0, -1),
                        "R":    (0, 1),
                        "U":    (1, 0),
                        "D":    (-1, 0)
                }
    return get_new_pos(head, movement[move])

def get_new_tail_pos(head, tail):
    #for the following square
    # tail is at T and
    # head is relative to tail at one of the numbers or T
    #       5 5 2 3 3
    #       5 1 1 1 3
    #       2 1 T 1 2
    #       4 1 1 1 6
    #       4 4 2 6 6
    vertical_difference = head[0] - tail[0]
    horizontal_difference = head[1] - tail[1]
    #head is at a 1 or at T,
    # so tail doesn't change
    if(abs(vertical_difference) < 2 and abs(horizontal_difference) < 2):
        return tail
    #head is at a 2
    if(abs(vertical_difference) + abs(horizontal_difference) == 2):
        movement = (vertical_difference // 2, horizontal_difference //2)
    #head is at a 3
    elif(vertical_difference + horizontal_difference > 2):
        movement = (1, 1)
    #head is at a 4
    elif(vertical_difference + horizontal_difference < -2):
        movement = (-1, -1)
    #head is at a 5
    elif(vertical_difference > 0):
        movement = (1, -1)
    #head is at a 6
    else:
        movement = (-1, 1)
    return get_new_pos(tail, movement)

def execute_iterated_move(knots, all_past_last_knots, iterated_move):
    for i in range(iterated_move[1]):
        knots[0] = get_new_head_pos(knots[0], iterated_move[0])
        for i in range(len(knots) - 1):
            j = i + 1
            knots[j] = get_new_tail_pos(knots[i], knots[j])
            if(j == len(knots) - 1):
                all_past_last_knots.add(knots[j])
    return knots, all_past_last_knots

def calculate_last_knot_trail(num_knots, moves):
    knots = []
    all_past_last_knots = set([(0, 0)])
    for i in range(num_knots):
        knots.append((0, 0))
    for iterated_move in moves:
        knots, all_past_last_knots = execute_iterated_move( knots,
                                                            all_past_last_knots,
                                                            iterated_move)
    return len(all_past_last_knots)

if __name__ == "__main__":
    moves = init_moves()

    print("9.1:")
    print(calculate_last_knot_trail(2, moves))
    print("")

    print("9.2:")
    print(calculate_last_knot_trail(10, moves))