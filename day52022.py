# Day5 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/5
import os
import re

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 5, part 1 .... >')
    print()

def do_the_moves(col1, col2, col3, instr):
    moveX = instr[1]
    fromX = instr[3]
    toX = instr[5]

    return col1, col2, col3

def process_instructions(col1, col2, col3, theData):
    for row in theData:
        #check if row starts with 'move' if not skip .....
        if row.startswith('move'):
            row = row.strip()
            instr = row.split(' ')
            print(row)
            col1, col2, col3 = do_the_moves(col1, col2, col3, instr)
    
    return col1, col2, col3

def tidy_row(row):
    #some initial variables
    i = 0
    noOfCols = 3
    #noOfCols = 9
  
    newRow = re.split(r"\s+", row)
    while i < noOfCols:
        newRow[i] = newRow[i].strip('[')
        newRow[i] = newRow[i].strip(']')
        i += 1
        
    return newRow

def find_cols(theData):
    # loop thru the list and split the row into .. 
    noOfCols = 3
    #noOfCols = 9
    col1 = []
    col2 = []
    col3 = []
    #col4 = []
    #col5 = []
    #col6 = []
    #col7 = []
    #col8 = []
    #col9 = []
    allColsCaptured = ['', '1', '2', '3', '']
    #allColsCaptured = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '']
    #loop thru first rows and find all columns
    for row in theData:
        newRow = tidy_row(row)
        if newRow == allColsCaptured:
            break
        else:
            i = 0
            while i < noOfCols:
                # go thru the row and add to col1, col2, or col3
                if i == 0 and newRow[i] != '': col1.append(newRow[i])
                if i == 1 and newRow[i] != '': col2.append(newRow[i])
                if i == 2 and newRow[i] != '': col3.append(newRow[i])
                i += 1
    return col1, col2, col3

def process_the_data(theData):
    #set initial position for the dataset
    noOfRows = len(theData)
    fully = 0

    #find all the columns from the dataset
    col1, col2, col3 = find_cols(theData)
    # process the instructions
    col1, col2, col3 = process_instructions(col1, col2, col3, theData)

    print(col1)
    print(col2)
    print(col3)
    return fully

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

