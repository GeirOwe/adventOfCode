# 2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 6, part 2 .... >')
    print()
    return

def process_the_data(theData):
    """
    Parse the worksheet for part 2: numbers are read vertically (top to bottom)
    in each column, and problems are read right-to-left.
    Each column represents one digit position.
    """
    if not theData or len(theData) < 2:
        return 0
    
    # Separate data lines from operator line (keep original, don't strip)
    operator_line = theData[-1]
    data_lines = theData[:-1]
    max_col = len(operator_line)
    
    # First, find all problem boundaries (columns where ALL rows including operator line have spaces)
    # A separator is a column where all rows (data + operator) are spaces
    separator_cols = []
    for c in range(max_col):
        # Check if this column is all spaces in ALL rows (data + operator)
        all_spaces = True
        # Check data lines
        for row in data_lines:
            if c >= len(row) or row[c] != ' ':
                all_spaces = False
                break
        # Check operator line
        if all_spaces and (c >= len(operator_line) or operator_line[c] != ' '):
            all_spaces = False
        
        if all_spaces:
            separator_cols.append(c)
    
    # Find all operators and their positions
    operators = []
    for c in range(max_col):
        if c < len(operator_line) and operator_line[c] in ['+', '*']:
            operators.append((c, operator_line[c]))
    
    # Process problems from right to left
    problems = []
    
    # Group operators by problem (between separators)
    # Find problem boundaries: separators divide problems
    # Problems are between separators (or start/end)
    problem_boundaries = sorted(separator_cols)
    problem_boundaries.insert(0, -1)  # Add start (before first column)
    problem_boundaries.append(max_col)  # Add end
    
    # Process each problem from right to left
    for op_col, op_char in reversed(operators):
        # Find which problem this operator belongs to
        # Problem is from after previous separator to before next separator
        problem_start = 0
        problem_end = max_col
        
        for i in range(1, len(problem_boundaries)):
            if problem_boundaries[i] > op_col:
                problem_end = problem_boundaries[i]  # End at separator (exclusive)
                problem_start = problem_boundaries[i - 1] + 1  # Start after previous separator
                break
        
        # Get columns in this problem (from right to left)
        problem_cols = list(range(problem_end - 1, problem_start - 1, -1))
        problem_cols.reverse()  # Now left to right
        
        # Read numbers from this problem (right to left)
        # Each column represents one number - read all digits from top to bottom
        numbers = []
        
        for pc in reversed(problem_cols):  # Process right to left
            # Read all digits from this column (top to bottom)
            column_digits = []
            for row in data_lines:
                if pc < len(row) and row[pc].isdigit():
                    column_digits.append(row[pc])
            
            # If this column has digits, it's a number
            if column_digits:
                number_str = ''.join(column_digits)
                if number_str:
                    numbers.append(int(number_str))
        
        # Calculate result for this problem
        if numbers and op_char:
            if op_char == '+':
                result = sum(numbers)
            elif op_char == '*':
                result = 1
                for n in numbers:
                    result *= n
            else:
                result = 0
            
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