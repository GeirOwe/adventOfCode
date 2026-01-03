# 2024 Advent of code
# source: https://adventofcode.com/2024

from dis import Instruction
import os
import re

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 3, part 2 .... >')
    print()
    return

# Combine all patterns into a single regex using capturing groups.
# Use re.finditer() to iterate through all matches.
# Keep track of whether matching is currently disabled.
# Process matches based on which pattern was matched:
# If the anti-pattern is matched, disable further matching.
# If the enable pattern is matched, re-enable matching.
# If the main pattern is matched and matching is not disabled, add it to the results.
def parse_with_patterns(text, pattern, anti_pattern, enable_pattern):
    regex = fr'({pattern})|({anti_pattern})|({enable_pattern})'
    matches = []
    is_disabled = False

    for match in re.finditer(regex, text):
        if match.group(2):  # Anti-pattern matched
            is_disabled = True
        elif match.group(3):  # Enable pattern matched
            is_disabled = False
        elif not is_disabled and match.group(1):  # Main pattern matched and not disabled
            matches.append(match.group(1))

    return matches

def find_instruct(text):
    results = []
    # Define the pattern to match
    #$$: Matches an opening parenthesis (escaped because parentheses have 
    # special meaning in regex)
    # \s*: Matches zero or more whitespace characters
    # \d+: Matches one or more digits
    # ,: Matches a literal comma
    # $$: Matches a closing parenthesis
    pattern = r"mul\(\s*\d+\s*,\s*\d+\s*\)"
    anti_pattern = r"don't\(\)"
    enable_pattern = r"do\(\)"

    results = parse_with_patterns(text, pattern, anti_pattern, enable_pattern)

    return results

def do_the_math(instructions):
    result = 0
    calc = 0
    for instruct in instructions:
        # get the two ints from mul(int1, int2)
        x = instruct.strip('mul(')
        y = x.strip(')')
        z = y.split(',')
        int1 = int(z[0])
        int2 = int(z[1])
        #do the math
        calc = int1 * int2
        result += calc

    return result

def process_the_data(theData):
    totResult = 0
    for row in theData:
        row = row.strip()
        #fetch all math instructions from the text in that row
        instructions = find_instruct(row)
        result = do_the_math(instructions)

        totResult += result

    return totResult

def get_the_data():
    #read the test puzzle input 
    #theData = open('day3_2024_test2_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day3_2024_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('What do you get if you add up all of the results -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()