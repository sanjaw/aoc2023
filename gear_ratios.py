import math
from utils.file import read_lines 

SKIP = "."
SYMBOLS = "+*#/=&@$%-"
GEAR = "*"

def main():
    grid = read_lines("data/gear_ratios.txt")

    print("-- Part One --")
    part_numbers, gear_parts = find_part_numbers(grid)
    print(f"Total value: {sum(part_numbers)}\n")
    
    print("-- Part Two --")
    total_val = 0
    for _, gear_part_nums in gear_parts.items():
        if len(gear_part_nums) == 2:
            total_val += gear_part_nums[0] * gear_part_nums[1]
    print(f"New total value: {total_val}\n")


def find_part_numbers(grid):
    part_numbers = []
    gear_parts = {}

    for row in range(len(grid)):
        col_start = col_end = None
        for col in range(len(grid[row])):
            if grid[row][col].isdigit() and col_start == None:
                col_start = col
            if not grid[row][col].isdigit() and col_start != None:
                col_end = col - 1

            if col_start != None and col_end != None:
                if check_neighbors(grid, row, col_start, col_end, SYMBOLS):
                    part_num = 0
                    for col in range(col_start, col_end + 1):
                        part_num += int(grid[row][col]) * int(math.pow(10, (col_end - col)))
                    part_numbers.append(part_num)
                    
                # If type of neighbor is a gear (*) then add to gear_parts
                neighbor_position = get_neighbors_position(grid, row, col_start, col_end, GEAR)
                if neighbor_position != None:
                    gear_part_num = 0
                    for col in range(col_start, col_end + 1):
                        gear_part_num += int(grid[row][col]) * int(math.pow(10, (col_end - col)))
                    try:
                        gear_parts[neighbor_position].append(gear_part_num)
                    except KeyError:
                         gear_parts[neighbor_position] = [gear_part_num]
                col_start = col_end = None
    
    return part_numbers, gear_parts


def check_neighbors(grid, row, col_start, col_end, symbols):
    '''
    Example:
    .................              col_start+1,r-1                 
    ......455........   col_start-1,r-1         col_end+1,r-1
    .........#....... col_start-1   4      5      5   col_end+1
    .................   col_start-1,r+1         col_end+1,r+1 [#]
    .................              col_start+1,r+1
    '''
    if col_start > 0 and ((row > 0 and grid[row-1][col_start-1] in symbols) \
            or grid[row][col_start-1] in symbols \
            or (row < len(grid) - 1 and grid[row+1][col_start-1] in symbols)):
        return True
    
    if col_end < len(grid[row]) - 1 and ((row > 0 and grid[row-1][col_end+1] in symbols) \
            or grid[row][col_end+1] in symbols \
            or (row < len(grid) - 1 and grid[row+1][col_end+1] in symbols)):
        return True

    for col in range(col_start, col_end + 1):
        if grid[row-1][col] in symbols \
            or ((row < len(grid) - 1) and grid[row+1][col] in symbols):
            return True

    return False



def get_neighbors_position(grid, row, col_start, col_end, symbols):
    '''
    Returns the coordinates of the character as a tuple or returns None if no character is nearby

    Example:
    .................              col_start+1,r-1                 
    ......455........   col_start-1,r-1         col_end+1,r-1
    .........#....... col_start-1   4      5      5   col_end+1
    .................   col_start-1,r+1         col_end+1,r+1 [#]
    .................              col_start+1,r+1
    '''
    if col_start > 0 and (row > 0 and grid[row-1][col_start-1] in symbols):
        return (row-1, col_start-1)
    if col_start > 0 and grid[row][col_start-1] in symbols:
        return (row, col_start-1)
    if col_start > 0 and (row < len(grid) - 1 and grid[row+1][col_start-1] in symbols):
        return (row+1, col_start-1)
    
    if col_end < len(grid[row]) - 1 and (row > 0 and grid[row-1][col_end+1] in symbols):
        return (row-1,col_end+1)
    if col_end < len(grid[row]) - 1 and grid[row][col_end+1] in symbols:
        return (row, col_end+1)
    if col_end < len(grid[row]) - 1 and (row < len(grid) - 1 and grid[row+1][col_end+1] in symbols):
        return (row+1, col_end+1)

    for col in range(col_start, col_end + 1):
        if grid[row-1][col] in symbols:
            return (row-1, col)
        if ((row < len(grid) - 1) and grid[row+1][col] in symbols):
            return (row+1, col)

    return None


if __name__ == "__main__":
    main()
