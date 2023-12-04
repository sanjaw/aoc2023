import re
from utils.file import read_lines 

digits = {
    "zero":     "0",
    "one":      "1",
    "two":      "2",
    "three":    "3",
    "four":     "4",
    "five":     "5",
    "six":      "6",
    "seven":    "7",
    "eight":    "8",
    "nine":     "9",
}

DIGIT_REGEX_FORWARD = "|".join('(?P<%s>%s)' % (key, key) for key in digits.keys())
DIGIT_REGEX_BACKWARD = "|".join('(?P<%s>%s)' % (key, key[::-1]) for key in digits.keys())    

def match_digit(match):
    return digits.get(match.lastgroup)


def main():
    lines = read_lines("data/trebuchet.txt")

    print("-- Part One --")
    total_val = 0

    for line in lines:
        val = read_value(line.strip())
        total_val += val
    print(f"Total value: {total_val}\n")

    print("-- Part Two --")
    total_val = 0
    for line in lines:
        val = read_value_2(line.strip())
        total_val += val

    print(f"New total value: {total_val}\n")


def read_value(line):
    first = last = 0
    found_first = found_last = False

    for i in range(len(line)):
        if line[i].isdigit() and not found_first:
            first = line[i]
            found_first = True
        
        reversed_line = line[::-1]
        if reversed_line[i].isdigit() and not found_last:
            last = reversed_line[i]
            found_last = True
        
        if found_first and found_last:
            break
    
    try:
        number = int(first + last)
    except TypeError:
        return 0
    else:
        return number


def read_value_2(line):
    first = last = 0

    forward_line = re.sub(DIGIT_REGEX_FORWARD, match_digit, line)
    for i in range(len(forward_line)):
        if forward_line[i].isdigit():
            first = forward_line[i]
            break
    
    reversed_line = line[::-1]
    reversed_line = re.sub(DIGIT_REGEX_BACKWARD, match_digit, reversed_line)
    for i in range(len(line)):
        if reversed_line[i].isdigit():
            last = reversed_line[i]
            break
    
    try:
        number = int(first + last)
    except TypeError:
        return 0
    else:
        return number


if __name__ == "__main__":
    main()
