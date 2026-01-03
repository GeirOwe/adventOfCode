# 2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 3, part 1 .... >')
    print()
    return

def process_the_data(theData):
    """
    For each bank (line), find the largest possible 2-digit joltage
    by selecting exactly 2 batteries (digits) in order.
    Return the sum of all maximum joltages.
    """
    total_joltage = 0
    
    for bank in theData:
        # Convert bank string to list of digits
        digits = [int(d) for d in bank]
        
        # Find the maximum 2-digit number we can form
        # by selecting two digits in order (i < j)
        max_joltage = 0
        
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                # Form 2-digit number from digits[i] and digits[j]
                joltage = digits[i] * 10 + digits[j]
                max_joltage = max(max_joltage, joltage)
        
        total_joltage += max_joltage
    
    return total_joltage

def get_the_data():
    #read the puzzle input 
    #theData = open('day3_2025_test_puzzle_input.txt', 'r')
    theData = open('day3_2025_puzzle_input.txt', 'r')
    
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
    
    print('what is the total output joltage -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()