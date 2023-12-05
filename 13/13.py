import os
import ast

def init_pairs():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    pairs = []

    iterator = 0
    while(iterator < len(lines)):
        array_one = ast.literal_eval(lines[iterator])
        array_two = ast.literal_eval(lines[iterator + 1])
        pairs.append((array_one, array_two))
        iterator += 3

    return pairs

def init_packets(divider_packets):
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    packets = []

    for line in lines:
        if(line != "\n"):
            packets.append(ast.literal_eval(line))
    for packet in divider_packets:
        packets.append(packet)

    return packets

def is_in_order(pair):
    left = pair[0]
    right = pair[1]

    if(is_int(left) and is_int(right)):
        if(left < right):
            return True
        elif(left > right):
            return False
        else:
            return None

    if(is_list(left) and is_list(right)):
        result = None
        iterator = 0
        bound = min(len(left), len(right))
        while(result == None and iterator < bound):
            result = is_in_order((left[iterator], right[iterator]))
            iterator += 1
        if(result == None):
            if(len(left) < len(right)):
                return True
            if(len(left) > len(right)):
                return False
        return result
    
    if(is_list(left) and is_int(right)):
        return is_in_order((left, [right]))
    
    if(is_int(left) and is_list(right)):
        return is_in_order(([left], right))

def is_int(value):
    return value.__class__.__name__ == "int"

def is_list(value):
    return value.__class__.__name__ == "list"

def sort_packets(packets):
    sorted_packets = []
    for packet in packets:
        sorted_packets = insert_into_sorted_packets(sorted_packets, packet)
    return sorted_packets

def insert_into_sorted_packets(sorted_packets, packet):
    if(sorted_packets == []):
        return [packet]
    for i in range(len(sorted_packets)):
        if(is_in_order((packet, sorted_packets[i]))):
            sorted_packets.insert(i, packet)
            return sorted_packets
    sorted_packets.append(packet)
    return sorted_packets

def get_divider_product(packets, divider_packets):
    product = 1
    index = 1
    for divider in divider_packets:
        for packet in packets:
            if(divider == packet):
                product *= index
                index = 1
                break
            index += 1
    return product

if __name__ == "__main__":
    pairs = init_pairs()

    sum = 0
    for i in range(len(pairs)):
        if(is_in_order(pairs[i])):
            sum += (i + 1)

    print("13.1:")
    print(sum)
    print("")

    divider_packets = [[[2]], [[6]]]
    packets = init_packets(divider_packets)
    packets = sort_packets(packets)

    print("13.2:")
    print(get_divider_product(packets, divider_packets))