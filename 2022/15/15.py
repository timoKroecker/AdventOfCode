import os

TASK_1_CONSTANT = 2000000
TASK_2_CONSTANT = 4000000

def init_coords():
    #read text file
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    sensors = []
    beacons = []

    for line in lines:
        words = line.split(" ")
        sensor_position = (int(words[2][2:-1]), int(words[3][2:-1]))
        beacon_position = (int(words[8][2:-1]), int(words[9][2:].replace("\n", "")))
        sensors.append(sensor_position)
        beacons.append(beacon_position)

    return sensors, beacons

def get_mahattan_distance(position_1, position_2):
    return abs(position_1[0] - position_2[0]) + abs(position_1[1] - position_2[1])

def get_nonbeacon_positions_per_sensor(sensor, beacon, row_num):
    nearest_point = (sensor[0], row_num)
    radius = get_mahattan_distance(sensor, beacon)
    distance_to_row = get_mahattan_distance(sensor, nearest_point)
    if(distance_to_row > radius):
        return set()
    positions = set()
    positions.add(sensor[0])
    for i in range(radius - distance_to_row):
        positions.add(sensor[0] + (i + 1))
        positions.add(sensor[0] - (i + 1))
    return positions

def get_nonbeacon_positions(sensors, beacons, row_num):
    nonbeacon_positions = set()
    for i in range(len(sensors)):
        new_positions = get_nonbeacon_positions_per_sensor(sensors[i], beacons[i], row_num)
        nonbeacon_positions = nonbeacon_positions.union(new_positions)

    nonbeacon_positions = remove_known_beacons(nonbeacon_positions, beacons, row_num)

    return nonbeacon_positions

def remove_known_beacons(nonbeacon_positions, beacons, row_num):
    for beacon in beacons:
        if(beacon[1] == row_num and nonbeacon_positions.__contains__(beacon[0])):
            nonbeacon_positions.remove(beacon[0])
    return nonbeacon_positions

def get_distress_positions(sensors, beacons):
    overlapping_points = get_circle_edge_overlaps(sensors, beacons)
    print(len(overlapping_points), "OVERLAPPING POINTS TOTAL")
    distress_positions = []

    for point in overlapping_points:
        if(not is_position_in_some_radius(sensors, beacons, point)):
            distress_positions.append(point)
            print("distress", point)
    return distress_positions
    

def is_position_in_some_radius(sensors, beacons, position):
    for i in range(len(sensors)):
        radius = get_mahattan_distance(sensors[i], beacons[i])
        distance = get_mahattan_distance(sensors[i], position)
        if(distance <= radius):
            return True
    return False

def get_circle_edge(sensor, beacon):
    edge = set()
    radius = get_mahattan_distance(sensor, beacon) + 1
    for x in range(-radius, radius + 1):
        y = radius - abs(x)
        if(0 <= sensor[0] + x <= TASK_2_CONSTANT):
            if(0 <= sensor[1] + y <= TASK_2_CONSTANT):
                edge.add((sensor[0] + x, sensor[1] + y))
            if(y != 0 and 0 <= sensor[1] - y <= TASK_2_CONSTANT):
                edge.add((sensor[0] + x, sensor[1] - y))
    return edge

def get_circle_edge_overlaps(sensors, beacons):
    edges = []
    overlapping_points = set()
    for i in range(len(sensors)):
        edges.append(get_circle_edge(sensors[i], beacons[i]))
        print("edge", i)
    for i in range(len(sensors)):
        for j in range(len(sensors)):
            if(i < j):
                overlapping_points = overlapping_points.union(set.intersection(edges[i], edges[j]))
                print("intersection", i, j)
    return overlapping_points

if __name__ == "__main__":
    sensors, beacons = init_coords()

    #nonbeacon_positions = get_nonbeacon_positions(sensors, beacons, TASK_1_CONSTANT)

    print("15.1:")
    #print(len(nonbeacon_positions))
    print("")

    distress_positions = get_distress_positions(sensors, beacons)

    print("15.2:")
    print(distress_positions)

    for distress_position in distress_positions:
        print(distress_position[0] * TASK_2_CONSTANT + distress_position[1])