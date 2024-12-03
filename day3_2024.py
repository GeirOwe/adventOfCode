# 2024 Advent of code
# source: https://adventofcode.com/2024

from dis import Instruction
import os
import re

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 3, part 1 .... >')
    print()
    return

def find_instruct(row):
    instructions = []
    # Define the pattern to match
    #$$: Matches an opening parenthesis (escaped because parentheses have 
    # special meaning in regex)
    # \s*: Matches zero or more whitespace characters
    # \d+: Matches one or more digits
    # ,: Matches a literal comma
    # $$: Matches a closing parenthesis
    pattern = r"mul\(\s*\d+\s*,\s*\d+\s*\)"

    # Find all matches
    matches = re.findall(pattern, row)
    return matches

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
    #theData = open('day3_2024_test_puzzle_input.txt', 'r')
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