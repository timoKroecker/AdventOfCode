import os

def init_lines():
    with open(os.path.dirname(__file__) + '/data.txt') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        split_index = lines[i].find(":") + 2
        lines[i] = lines[i][split_index:].replace("\n", "")

    return lines

def lines_to_games(lines):
    games = []

    for line in lines:
        draws = line.split("; ")
        for i in range(len(draws)):
            draws[i] = draws[i].split(", ")
            for j in range(len(draws[i])):
                draws[i][j] = draws[i][j].split(" ")
                draws[i][j][0] = int(draws[i][j][0])
        games.append(draws)

    return games

def is_game_possible(game, bag_contents, colors):
    for draw in game:
        for cubes in draw:
            for color in colors:
                if(cubes[1] == color and cubes[0] > bag_contents[color]):
                    return False
    return True

def get_ids_of_possible_games(games, bag_contents, colors):
    ids = []
    for i in range(len(games)):
        if(is_game_possible(games[i], bag_contents, colors)):
            ids.append(i + 1)
    return ids

def get_power_of_min_bag_contents(game, colors):
    power = 1
    for color in colors:
        color_draws = []
        for draw in game:
            for cubes in draw:
                if(cubes[1] == color):
                    color_draws.append(cubes[0])
        power *= max(color_draws)
    return power

if __name__ == "__main__":
    lines = init_lines()
    games = lines_to_games(lines)
    bag_contents = {}
    bag_contents["red"] = 12
    bag_contents["green"] = 13
    bag_contents["blue"] = 14
    colors = ["red", "green", "blue"]

    ids_of_possible_games = get_ids_of_possible_games(games, bag_contents, colors)
    print("")
    print("2.1:")
    print(sum(ids_of_possible_games))


    print("")
    print("2.2:")
    print(sum([get_power_of_min_bag_contents(game, colors) for game in games]))