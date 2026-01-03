# 2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 5, part 2 .... >')
    print()
    return

def process_the_data(theData):
    """
    Find all unique ingredient IDs that are considered fresh by the ranges.
    An ID is fresh if it falls into any of the fresh ID ranges.
    Returns the total count of unique fresh IDs.
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
    
    # Merge overlapping intervals and calculate total coverage
    # Sort ranges by start value
    ranges.sort()
    
    # Merge overlapping intervals
    merged = []
    for start, end in ranges:
        if not merged:
            merged.append([start, end])
        else:
            # Check if this range overlaps or is adjacent to the last merged range
            last_start, last_end = merged[-1]
            if start <= last_end + 1:  # Overlaps or adjacent (inclusive ranges)
                # Merge: extend the end if needed
                merged[-1][1] = max(last_end, end)
            else:
                # No overlap, add as new interval
                merged.append([start, end])
    
    # Calculate total count: sum of (end - start + 1) for each merged interval
    total_count = 0
    for start, end in merged:
        total_count += (end - start + 1)
    
    return total_count

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
    
    print('How many total unique ingredient IDs are considered fresh -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()