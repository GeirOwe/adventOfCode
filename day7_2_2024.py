# 2024 Advent of code
# source: https://adventofcode.com/2024

import os
from itertools import product

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 7, part 2 .... >')
    print()
    return

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def can_form_equation(test_value, numbers):
    for ops in product(['+', '*', '||'], repeat=len(numbers) - 1):
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False

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

def process_the_data():
    #equations = read_equations_from_file('day7_2024_test_puzzle_input.txt')
    equations = read_equations_from_file('day7_2024_puzzle_input.txt')
    total_calibration_result = 0

    for test_value, numbers in equations:
        if can_form_equation(test_value, numbers):
            total_calibration_result += test_value
            
    return total_calibration_result

def start_the_engine():
  
    #process the data and return the answer
    valueX = process_the_data()
    
    print('what is their total calibration result -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()



