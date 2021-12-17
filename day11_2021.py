# Day11 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/11

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 11, part 1 .... >')
    print()
    return

def increase_all_fields(grid):
    nrows, ncols = grid.shape
    for i in range(nrows):
        for j in range(ncols):
            grid[i][j] += 1
    return grid

def find_10(grid, list_of_10):
    nrows, ncols = grid.shape
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 10:
                list_of_10.append([i,j])
                grid[i][j]  = -1
    return list_of_10, grid

def increase_adjacent(grid, element):
    adjacent_pos = []
    maxRow, maxCol = grid.shape
    maxRow -= 1 #starting from zero
    maxCol -= 1 #starting from zero
    elementProcessed = False
    # check all 4 corners
    if element == [0,0]: 
        adjacent_pos.append([0, 1]); adjacent_pos.append([1, 1]); adjacent_pos.append([1, 0]) #right, vertical, down
        elementProcessed = True
    if element == [0,maxCol]: 
        adjacent_pos.append([0, maxCol-1]); adjacent_pos.append([1, maxCol-1]); adjacent_pos.append([1, maxCol]) #left, vertical, down
        elementProcessed = True
    if element == [maxRow,maxCol]: 
        adjacent_pos.append([maxRow, maxCol-1]); adjacent_pos.append([maxRow-1, maxCol-1]); adjacent_pos.append([maxRow-1, maxCol]) #left, vertical, up
        elementProcessed = True
    if element == [maxRow,0]: 
        adjacent_pos.append([maxRow, 1]); adjacent_pos.append([maxRow-1, 1]); adjacent_pos.append([maxRow-1, 0]) #right, vertical, up
        elementProcessed = True
   
    #check if first column or last column
    if elementProcessed != True:
        if element[1] == 0: #first column
            row = element[0]
            adjacent_pos.append([row-1, 0]); adjacent_pos.append([row+1, 0]); adjacent_pos.append([row, 1]) #up, down, right
            adjacent_pos.append([row-1, 1]); adjacent_pos.append([row+1, 1]);    #vertical up, vertical down
            elementProcessed = True
        elif element[1] == maxCol: #last column
            row = element[0]
            adjacent_pos.append([row-1, maxCol]); adjacent_pos.append([row+1, maxCol]); adjacent_pos.append([row, maxCol-1]) #up, down, left
            adjacent_pos.append([row-1, maxCol-1]); adjacent_pos.append([row+1, maxCol-1])   #vertical up, vertical down
            elementProcessed = True

    #check if first row or last row
    if elementProcessed != True:
        if element[0] == 0: #first row
            col = element[1]
            adjacent_pos.append([0, col-1]); adjacent_pos.append([0, col+1]); adjacent_pos.append([1, col]) #left, right, down
            adjacent_pos.append([1, col-1]); adjacent_pos.append([1, col+1])     #vertical down left, vertical down right
            elementProcessed = True
        elif element[0] == maxRow: #last row
            col = element[1]
            adjacent_pos.append([maxRow, col-1]); adjacent_pos.append([maxRow, col+1]); adjacent_pos.append([maxRow-1, col]) #left, right, up
            adjacent_pos.append([maxRow-1, col-1]); adjacent_pos.append([maxRow-1, col+1]) #vertical up left, vertical up right
            elementProcessed = True
    
    #the position is in the middle if still false
    if elementProcessed != True:
        row = element[0]
        col = element[1]
        #left, right, up, down
        adjacent_pos.append([row, col-1]); adjacent_pos.append([row, col+1]); adjacent_pos.append([row-1, col]); adjacent_pos.append([row+1, col])
        #vert up left, vert up right
        adjacent_pos.append([row-1, col-1]); adjacent_pos.append([row-1, col+1])
        #vert down left, vert down right
        adjacent_pos.append([row+1, col-1]); adjacent_pos.append([row+1, col+1])
    
    #process all positions in the adjacent_pos list
    for element in adjacent_pos:
        row = element[0]
        col = element[1]
        if grid[row, col] != -1 and grid[row, col] < 10: 
            grid[row, col] += 1

    return grid

def step_away(grid, valueX):
    list_of_10 = []
    #increase all fields in grid with one
    grid = increase_all_fields(grid)
    
    #add all 10's in grid to a list of to_be_flashed, set number in grid to -1 afterwards
    list_of_10, grid = find_10(grid, list_of_10)
    while len(list_of_10) > 0:
        #increase valueX when flashing
        valueX += 1
        #process each element in to_be_flashed; and pop element afterwards
        element = list_of_10.pop()
    #   when flashing, increase all adjacent numbers with 1 unless they are -1
        grid = increase_adjacent(grid, element)
    #   add all new 10's in grid to a list of to_be_flashed, set number in grid to -1 afterwards
        list_of_10, grid = find_10(grid, list_of_10)

    # change all -1 to zeros in grid at the end of the step
    grid[grid < 0] = 0
    return valueX, grid

def process_the_data(grid):
    valueX = 0
    #number of steps
    noSteps = 100
    i = 0
    list_of_10 = []
    while i < noSteps:
        #do a step and check for flashes in grid. flashes are added to list_of_10
        valueX, grid = step_away(grid, valueX)
        i += 1
    return valueX

def get_the_data():
    #read the test puzzle input 
    #theData = open('day11_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day11_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    rows = 0
    #process each row in the data
    for element in theData:
        rows += 1
        elementTrimmed = element.strip()
        cols = 0
        #process each number in the row
        for numX in elementTrimmed:
            data_list.append(numX)
            cols += 1
    
    maxCols = len(elementTrimmed)
    maxRows = rows
    #create a numpy array
    data_array = np.array(data_list, dtype="int").reshape(maxRows, maxCols)
    return data_array

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer
    valueX = process_the_data(theData)

    # Next, you need to 
    print('\nHow many total flashes are there after 100 steps ->', valueX, '\n')
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()