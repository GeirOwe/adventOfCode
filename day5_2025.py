# 2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 5, part 1 .... >')
    print()
    return

def process_the_data(theData):
    """
    Determine which available ingredient IDs are fresh.
    An ID is fresh if it falls into any of the fresh ID ranges.
    """
    # Find the blank line that separates ranges from IDs
    blank_line_index = -1
    for i, line in enumerate(theData):
        if line == '':
            blank_line_index = i
            break
    
    # Parse fresh ID ranges (before blank line)
    ranges = []
    for i in range(blank_line_index):
        range_str = theData[i]
        parts = range_str.split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))
    
    # Parse available ingredient IDs (after blank line)
    available_ids = []
    for i in range(blank_line_index + 1, len(theData)):
        if theData[i] != '':  # Skip empty lines
            available_ids.append(int(theData[i]))
    
    # Count how many available IDs are fresh
    fresh_count = 0
    
    for ingredient_id in available_ids:
        # Check if this ID falls into any range
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        
        if is_fresh:
            fresh_count += 1
    
    return fresh_count

def get_the_data():
    #read the puzzle input 
    #theData = open('day5_2025_test_puzzle_input.txt', 'r')
    theData = open('day5_2025_puzzle_input.txt', 'r')
    
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
    
    print('How many of the available ingredient IDs are fresh -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()