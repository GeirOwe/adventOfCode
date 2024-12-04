# Day3 - 2018 Advent of code
# source: https://adventofcode.com/2018

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2018 Day 3, part 1 .... >')
    print()
    return

def init_grid(rows, cols):
    # Opprett en 2D-array med 6 rader og 4 kolonner fylt med dots
    array_2d = [['.' for j in range(cols)] for i in range(rows)]

    return array_2d

def split_row(row):
    #format: #1 @ 1,3: 4x4 -> id @ col,row: colxrow
    res = row.split()
    #start
    start = res[2].strip(':')
    start2 = start.split(',')
    col_start = int(start2[0])
    row_start = int(start2[1])
    #end
    end = res[3].split('x')
    col_end = int(end[0])
    row_end = int(end[1])

    return col_start, row_start, col_end, row_end

def update_grid(col_start, row_start, col_end, row_end, grid): 
    #loop thru the grid and upate pattern with marks
    # X -> marked more than once
    # # -> marked once
    # . -> never marked
    for col in range(col_end):
        for row in range(row_end):
            if grid[row_start+row][col_start+col] == '.': 
                grid[row_start+row][col_start+col] = '#'
            else:
                grid[row_start+row][col_start+col] = 'X'
    return grid

def process_the_data(theData):
    #grid is 8 x 8 in test. 1000 x 1000 in real run
    col_max = 1000
    row_max = 1000
    grid = init_grid(row_max, col_max)

    #loop thru all the data
    for row in theData:
        col_start, row_start, col_end, row_end = split_row(row)
        grid = update_grid(col_start, row_start, col_end, row_end, grid)
    
    # Tell antall forekomster av 'X'
    checksum = 0
    for row in grid:
        checksum += row.count('X')
    return checksum

def get_the_data():
    #read the test puzzle input 
    #theFile = open('day32018_test_puzzle_input.txt', 'r')
    theFile = open('day32018_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theFile:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)

    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('How many square inches of fabric are within two or more claims?  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()
