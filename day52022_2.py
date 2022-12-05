# Day5 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/5
import os
import re

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 5, part 2 .... >')
    print()

def do_the_moves(matrix, instr):
    moveX = int(instr[1])
    moveY = moveX - 1   #starting position in list
    fromX = int(instr[3]) -1 
    toX = int(instr[5]) - 1
    i = 0
    while i < moveX:
        x = matrix[fromX].pop(moveY)
        matrix[toX].insert(0, x)
        i += 1
        moveY -= 1

    return matrix

def process_instructions(matrix, theData):
    for row in theData:
        #check if row starts with 'move' if not skip .....
        if row.startswith('move'):
            row = row.strip()
            instr = row.split(' ')
            matrix = do_the_moves(matrix, instr)
    
    return matrix

def tidy_row(row):
    #some initial variables
    i = 0
    noOfCols = 3
    #noOfCols = 9
    rowlength = len(row)
    newRow = re.split(r"\s+", row)
    while i < noOfCols:
        newRow[i] = newRow[i].strip('[')
        newRow[i] = newRow[i].strip(']')
        i += 1
        
    return newRow

def find_cols(theData):
    # loop thru the list and split the row into .. 
    noOfCols = 3
    row = 0
    col = 0
    matrix = []

    #loop thru first rows and find all columns
    while col < noOfCols:
        #next column
        list = []
        for row in theData:
            #for all rows
            newRow = tidy_row(row)
            if newRow[1].startswith('1'):
                break
            else:
                if newRow[col] != '':
                    list.append(newRow[col])
        col += 1
        matrix.append(list)

    return matrix

def process_the_data(theData):
    #find all the columns from the dataset
    matrix = find_cols(theData)

    # process the instructions
    matrix = process_instructions(matrix, theData)
    answer = matrix[0][0]+matrix[1][0]+matrix[2][0]
    
    return answer

def get_the_data():
    #read the test puzzle input 
    theData = open('day52022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day52022_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        data_list.append(element)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: ...
    valueX = process_the_data(theData) 
    
    print('what crate ends up on top of each stack -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()

