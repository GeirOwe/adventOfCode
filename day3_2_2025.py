# 2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 3, part 2 .... >')
    print()
    return

def process_the_data(theData):
    """
    For each bank (line), find the largest possible 12-digit joltage
    by selecting exactly 12 batteries (digits) in order.
    Return the sum of all maximum joltages.
    """
    total_joltage = 0
    num_digits_to_select = 12
    
    for bank in theData:
        # Convert bank string to list of digits
        digits = [int(d) for d in bank]
        n = len(digits)
        
        # Greedy approach: for each of the 12 positions,
        # pick the largest digit available while ensuring we can
        # still select the remaining digits
        selected_indices = []
        start_pos = 0
        
        for pos in range(num_digits_to_select):
            # Calculate the range of positions we can pick from
            # We need to leave (num_digits_to_select - pos - 1) digits for later
            remaining_digits = num_digits_to_select - pos - 1
            end_pos = n - remaining_digits
            
            # Find the maximum digit in the available range
            max_digit = -1
            max_index = -1
            for i in range(start_pos, end_pos):
                if digits[i] > max_digit:
                    max_digit = digits[i]
                    max_index = i
            
            # Select this digit
            selected_indices.append(max_index)
            start_pos = max_index + 1
        
        # Form the number from selected digits
        joltage = 0
        for idx in selected_indices:
            joltage = joltage * 10 + digits[idx]
        
        total_joltage += joltage
    
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