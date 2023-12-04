from utils.file import read_lines

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

CUBE_COLORS_MAX_VALUE = {
    "red":  MAX_RED, 
    "green": MAX_GREEN, 
    "blue": MAX_BLUE
}

def main():
    lines = read_lines("data/cube_conundrum.txt")

    print("-- Part One --")
    total_val = 0
    for line in lines:
        game_subset = parse_line(line)
        value = check_game_condition(game_subset)
        total_val += value
    print(f"Total value: {total_val}\n")

    print("-- Part Two --")
    total_val = 0
    for line in lines:
        game_subset = parse_line(line)
        value = check_game_condition_2(game_subset)
        total_val += value
    print(f"New total value: {total_val}\n")
    

def parse_line(line: str):
    '''
    Parse line and get consitutent game id and game contents
    Example: "Game 71: 1 blue, 2 green, 13 red; 7 red; 1 green, 5 red"
    @return tuple(game_id, array of red blue green cube counts)
    '''
    game, contents = line.split(":")
    _, game_id = game.split(" ")

    subsets = contents.split(";")
    
    subset_list = []
    for subset in subsets:
        cube_instances = subset.strip().split(",")
        cube_subset = {}
        for cube_type in cube_instances:
            cube_count, cube_color = cube_type.strip().split(" ")
            cube_subset[cube_color.lower()] = cube_count
        subset_list.append(cube_subset)

    return (game_id.strip(), subset_list)


def check_game_condition(game_subset):
    '''
    Check game conditions (the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?)
    if feasible

    return game_id or 0 
    '''
    for cubes_subset in game_subset[1]:
        for key, value in cubes_subset.items():
            try:
                if int(value) > CUBE_COLORS_MAX_VALUE[key]:
                    return 0
            except ValueError:
                return 0
    
    return int(game_subset[0].strip())


def check_game_condition_2(game_subset):
    '''
    Check second condition of fewest number of cubes of each color
    Example:
        r   g   b
        ---	---	---
        4	0	3
        1	2	0
        0	2	6
        --	--	--
    max 4	2	6
        ---	---	---
        0	2	1
        1	3	4
        0	1	1
        --	--	--
    max 1	3	4
        ---	---	---
    
    return power of a minimum of cubes or 0
    '''
    maximum_cubes = { "red": 0, "green": 0, "blue": 0 }
    for cubes_subset in game_subset[1]:
        for key, value in cubes_subset.items():
            maximum_cubes[key] = max(int(value), maximum_cubes[key])
    
    return maximum_cubes["red"] * maximum_cubes["green"] * maximum_cubes["blue"]


if __name__ == "__main__":
    main()
