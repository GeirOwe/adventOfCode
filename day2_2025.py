#  2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 2, part 1 .... >')
    print()
    return

def is_invalid_id(id_num):
    """
    Check if an ID is invalid (made of a sequence of digits repeated twice).
    Examples: 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
    """
    id_str = str(id_num)
    # Must have even number of digits
    if len(id_str) % 2 != 0:
        return False
    
    # Split in half and check if first half equals second half
    mid = len(id_str) // 2
    first_half = id_str[:mid]
    second_half = id_str[mid:]
    
    return first_half == second_half

def process_the_data(theData):
    # theData is now a list of ranges, where each range is [first_id, last_id]
    # Example: [[11, 22], [95, 115], [998, 1012], ...]
    
    invalid_ids = []
    
    # Process each range
    for first_id, last_id in theData:
        # Check all IDs in this range (inclusive)
        for id_num in range(first_id, last_id + 1):
            if is_invalid_id(id_num):
                invalid_ids.append(id_num)
    
    # Print some info for debugging
    print(f"Number of ranges: {len(theData)}")
    print(f"Total invalid IDs found: {len(invalid_ids)}")
    if len(invalid_ids) > 0:
        print(f"First few invalid IDs: {invalid_ids[:10]}")
    
    # Return the sum of all invalid IDs
    return sum(invalid_ids)

def get_the_data():
    #read the puzzle input 
    #theData = open('day2_2025_test_puzzle_input.txt', 'r')
    theData = open('day2_2025_puzzle_input.txt', 'r')
    
    # Read the input line and parse ranges
    # Ranges are separated by commas; each range has first ID and last ID separated by a dash
    input_line = theData.readline().strip()
    theData.close()
    
    # Split by commas to get individual ranges
    ranges = []
    for range_str in input_line.split(','):
        # Split each range by dash to get first and last ID
        parts = range_str.split('-')
        first_id = int(parts[0])
        last_id = int(parts[1])
        ranges.append([first_id, last_id])
    
    return ranges

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('What do you get if you add up all of the invalid IDs  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()