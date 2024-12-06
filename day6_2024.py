# Day6 - 2024 Advent of code
# source: https://adventofcode.com/2024

from operator import truediv
import os
from collections import Counter

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 6, part 1 .... >')
    print()
    return

def simulate_guard_patrol(grid):
    #movements
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    dir_index = 0
    
    # Find the guard's starting position
    guard_pos = None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            # '^' represents the guard facing up. '>' represents the guard facing right
            # 'v' represents the guard facing down. '<' represents the guard facing left
            if cell in '^>v<':
                guard_pos = (i, j)
                dir_index = '^>v<'.index(cell)
                break
        if guard_pos:
            break
    
    if not guard_pos:
        return grid  # Guard not found
    
    #track the steps of the guard
    steps = 0
    max_steps = len(grid) * len(grid[0]) * 4  # Arbitrary limit to prevent infinite loops
    while steps < max_steps:
        row, col = guard_pos
        dx, dy = directions[dir_index]
        new_row, new_col = row + dx, col + dy
        
        # Check if the next position is within the grid and not obstructed
        if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and
            grid[new_row][new_col] != '#'):
            # Move forward
            grid[row][col] = '.'
            guard_pos = (new_row, new_col)
            grid[new_row][new_col] = '^>v<'[dir_index]
        else:
            # Turn right
            dir_index = (dir_index + 1) % 4
            grid[row][col] = '^>v<'[dir_index]
        
        steps += 1
        # Mark the current position with 'X'
        if grid[row][col] not in '#X':
            grid[row][col] = 'X'
        
        # Check if guard has left the grid
        if (guard_pos[0] == 0 or guard_pos[0] == len(grid) - 1 or
            guard_pos[1] == 0 or guard_pos[1] == len(grid[0]) - 1):
            break
    
    return grid

# track the number of steps by the guard
def count_x(grid):
    return sum(row.count('X') for row in grid)

def process_the_data(theData):
    # move the input to the grid
    initial_grid = []
    for row in theData:
        row = row.strip()
        initial_grid.append(list(row))

    #traverse the grid
    final_grid = simulate_guard_patrol(initial_grid)

    # Count and print the number of 'X', add one for the final step
    steps = count_x(final_grid) + 1
    return steps

def get_the_data():
    #read the test puzzle input 
    #theData = open('day6_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day6_2024_puzzle_input.txt', 'r')
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
    
    print('How many distinct positions will the guard visit before leaving -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()