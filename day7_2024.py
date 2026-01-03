# 2024 Advent of code
# source: https://adventofcode.com/2024

import os
from itertools import product

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 7, part 1 .... >')
    print()
    return

#calculate result with these operators
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

def can_form_equation(test_value, numbers):
    # Generate all possible combinations of operators
    operator_combinations = product('+*', repeat=len(numbers) - 1)
    
    #test with all operators and see if any of them match the test value
    for operators in operator_combinations:
        result = evaluate_expression(numbers, operators)
        if  result == test_value:
            return True
    return False

def process_the_data(theData):
    equations = [] 
    #process the input to a list of tuples
    for row in theData:
        test_val, ops  = row.split(':')
        #catch test value and operations
        test_val = int(test_val.strip())
        ops = ops.strip()
        ops_list = ops.split(' ')

        #convert ops list from string to int
        i = 0
        while i < len(ops_list):
            ops_list[i] = int(ops_list[i])
            i += 1
        
        #add test value and the operations list to an equations list
        equations.append((test_val, ops_list))
    
    #do the quiz
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