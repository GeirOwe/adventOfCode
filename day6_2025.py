# 2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 6, part 1 .... >')
    print()
    return

def process_the_data(theData):
    """
    Parse the worksheet: columns are defined by operator positions.
    Each column has numbers and an operator at the bottom.
    """
    import re
    
    if not theData or len(theData) < 2:
        return 0
    
    # Separate data lines from operator line (keep original, don't strip)
    operator_line = theData[-1]
    data_lines = theData[:-1]
    
    # Find operator positions in the operator line
    operator_positions = []
    for i, char in enumerate(operator_line):
        if char in ['+', '*']:
            operator_positions.append((i, char))
    
    if not operator_positions:
        return 0
    
    num_columns = len(operator_positions)
    
    # Define column boundaries: columns extend from one gap end to the next gap end
    # Find all gap positions (2+ consecutive spaces)
    gap_positions = []
    i = 0
    while i < len(operator_line) - 1:
        if operator_line[i:i+2] == '  ':
            # Found a gap, find where it ends
            gap_start = i
            while i < len(operator_line) and operator_line[i] == ' ':
                i += 1
            gap_end = i
            gap_positions.append((gap_start, gap_end))
        else:
            i += 1
    
    # Build column boundaries: from start/gap_end to next gap_end/end
    column_boundaries = []
    for i, (op_pos, operator) in enumerate(operator_positions):
        # Column starts after previous gap (or at start)
        if i == 0:
            col_start = 0
        else:
            # Start after the gap that ends before or at this operator
            col_start = 0
            for gap_start, gap_end in gap_positions:
                if gap_end <= op_pos:
                    col_start = gap_end
                else:
                    break
        
        # Column ends at next gap end (or end of line)
        if i == len(operator_positions) - 1:
            col_end = len(operator_line)
        else:
            # End at the gap that starts after this operator
            col_end = len(operator_line)
            for gap_start, gap_end in gap_positions:
                if gap_start > op_pos:
                    col_end = gap_end
                    break
        
        column_boundaries.append((col_start, col_end, operator))
    
    # Initialize matrix: one list per column
    kol_matrise = [[] for _ in range(num_columns)]
    
    # Parse each data line and assign numbers to columns based on boundaries
    for row in data_lines:
        # Find all numbers with their positions
        for match in re.finditer(r'\d+', row):
            num_start = match.start()
            num_end = match.end()
            num_value = int(match.group())
            
            # Find which column this number belongs to based on boundaries
            # Use the center of the number to determine which column it belongs to
            num_center = (num_start + num_end) // 2
            
            for col_idx, (col_start, col_end, _) in enumerate(column_boundaries):
                # Number is in column if its center is within the range
                if col_start <= num_center < col_end:
                    kol_matrise[col_idx].append(num_value)
                    break
    
    # Calculate results for each column
    # Only process columns that have the expected number of numbers (one per data line)
    problems = []
    expected_numbers_per_column = len(data_lines)
    
    for col_idx in range(num_columns):
        numbers = kol_matrise[col_idx]
        # Only process if column has the expected number of numbers
        if len(numbers) == expected_numbers_per_column:
            _, _, operator = column_boundaries[col_idx]
            
            if operator == '+':
                result = sum(numbers)
            elif operator == '*':
                result = 1
                for n in numbers:
                    result *= n
            else:
                continue
            
            problems.append(result)
    
    # Return grand total
    return sum(problems)

def get_the_data():
    #read the puzzle input 
    #theData = open('day6_2025_test_puzzle_input.txt', 'r')
    theData = open('day6_2025_puzzle_input.txt', 'r')
    
    #move data into a list - read a line and remove newline but keep spacing
    data_list = []
    for element in theData:
        # Remove newline but keep original spacing (don't strip)
        elementTrimmed = element.rstrip('\n\r')
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('The grand total is  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()