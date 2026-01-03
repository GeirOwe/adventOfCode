# Template for Advent of Code
# source: https://adventofcode.com/

import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 18 part 1 .... >')
    print()
    return

def create_matrix(theData):
    matrix = []
    rows = 2000
    cols = 2000
    j = 0
    while j < rows:
        i = 0
        x = []
        while i < cols:
            x.append('.')
            i += 1
        
        #add row to matrix
        matrix.append(x)
        j += 1

    return matrix

def paintRight(length, matrix, row, col):
    for i in range(length):
        col += 1
        matrix[row][col] = '#'
    return matrix, row, col

def paintLeft(length, matrix, row, col):
    for i in range(length):
        col -= 1
        matrix[row][col] = '#'
    return matrix, row, col

def paintUp(length, matrix, row, col):
    for i in range(length):
        row -= 1
        matrix[row][col] = '#'
    return matrix, row, col

def paintDown(length, matrix, row, col):
    for i in range(length):
        row += 1
        matrix[row][col] = '#'
    return matrix, row, col

def paint(direction, length, matrix, row, col):
    if direction == 'R': matrix, row, col = paintRight(length, matrix, row, col)
    if direction == 'L': matrix, row, col = paintLeft(length, matrix, row, col)
    if direction == 'U': matrix, row, col = paintUp(length, matrix, row, col)
    if direction == 'D': matrix, row, col = paintDown(length, matrix, row, col)
    return matrix, row, col

def countX(row):
    numberX = 0
    #find first and last and count the number of #
    first = False
    last = False
    pos = 0
    firstPos = 0
    lastPos = 0
    for char in row:
        if char == '#':
            if first == False:
                first = True
                firstPos = pos
            else:
                lastPos = pos
        pos += 1        

    # calculate from first to last
    numberX = lastPos - firstPos
    if numberX > 0: numberX = (lastPos - firstPos) + 1
    return numberX

#start function
def process_codes(theData):
    # move theData into a list of lists
    matrix = create_matrix(theData)
    # find any number adjacent to a symbol
    total = 0
    row = 200
    col = 200
    # pos 0,0 is to be marked with a #
    matrix[row][col] = '#'
    for theRow in theData:
        direction, length, _ = theRow.split()
        #paint the pos in the matrix
        matrix, row, col = paint(direction, int(length), matrix, row, col)
        
    #calculate the interior
    numberX = 0
    for row in matrix:
        numberX = countX(row) 
        total = total + numberX
        
    return total
#end function

def get_the_data():
    #read the puzzle input like this if a list without separation chars
    #theData = open('day182023_test_puzzle_input.txt', 'r')
    theData = open('day182023_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)

    return data_list

#start function
def start_the_challenge():
    #get the data and read the into  list
    theData = get_the_data()

    #process the codes and return the answer
    valueX = process_codes(theData) 
    
    print('\nhow many cubic meters of lava could it hold? ->', valueX, '\n')

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()