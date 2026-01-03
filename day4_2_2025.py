# 2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 4, part 2 .... >')
    print()
    return

def process_the_data(theData):
    """
    Iteratively remove accessible rolls of paper until no more can be removed.
    A roll can be accessed if there are fewer than 4 rolls in the 8 adjacent positions.
    Returns the total number of rolls removed.
    """
    # Convert grid to mutable list of lists
    grid = [list(row) for row in theData]
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Directions for 8 adjacent positions (including diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    total_removed = 0
    
    # Keep removing rolls until no more can be removed
    while True:
        # Find all accessible rolls in this iteration
        accessible_positions = []
        
    for i in range(rows):
        for j in range(cols):
            # Only check positions that have a roll of paper
            if grid[i][j] == '@':
                # Count adjacent rolls
                adjacent_rolls = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    # Check if position is within bounds and contains a roll
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == '@':
                            adjacent_rolls += 1
                
                # If fewer than 4 adjacent rolls, this roll is accessible
                if adjacent_rolls < 4:
                        accessible_positions.append((i, j))
        
        # If no accessible rolls found, we're done
        if len(accessible_positions) == 0:
            break
        
        # Remove all accessible rolls
        for i, j in accessible_positions:
            grid[i][j] = '.'
            total_removed += 1
    
    return total_removed

def get_the_data():
    #read the puzzle input 
    #theData = open('day4_2025_test_puzzle_input.txt', 'r')
    theData = open('day4_2025_puzzle_input.txt', 'r')
    
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
    
    print('How many total rolls of paper can be removed -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()