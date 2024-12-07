# 2024 Advent of code
# source: https://adventofcode.com/2024

import os
from itertools import product
from functools import lru_cache

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 7, part 2 .... >')
    print()
    return

@lru_cache(maxsize=None)
def can_form_equation(target, numbers):
    if len(numbers) == 1:
        return numbers[0] == target
    
    for i in range(1, len(numbers)):
        left = numbers[:i]
        right = numbers[i:]
        
        # Try addition
        if can_form_equation(target - sum(right), left):
            return True
        
        # Try multiplication
        if target % prod(right) == 0 and can_form_equation(target // prod(right), left):
            return True
        
        # Try concatenation
        right_value = int(''.join(map(str, right)))
        if target > right_value and can_form_equation(int(str(target)[:-len(str(right_value))]), left):
            return True
    
    return False

def prod(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

#read the file
def read_equations_from_file(filename):
    equations = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            test_value = int(parts[0])
            numbers = tuple(int(num) for num in parts[1].split())
            equations.append((test_value, numbers))
    return equations

def process_the_data(theData):
    equations = read_equations_from_file('day7_2024_test_puzzle_input.txt')
    #equations = read_equations_from_file('day7_2024_puzzle_input.txt.txt')
    total_calibration_result = 0

    for test_value, numbers in equations:
        if can_form_equation(test_value, numbers):
            total_calibration_result += test_value
            
    return total_calibration_result

def get_the_data():
    #read the test puzzle input 
    theData = open('day7_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day7_2024_puzzle_input.txt', 'r')
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
    
    print('what is their total calibration result -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()



