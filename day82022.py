# Day8 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/8
import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 8, part 1 .... >')
    print()
    return

def find_cols(theData):
    matrix = []
    noOfRows = len(theData)
    #loop thru rows and add to matrix
    for row in theData:
        #return a list with all columns filled with chars or space
        list = []
        list[:0] = row
        matrix.append(list)
        rowlength = len(row)

    return matrix, rowlength, noOfRows

def check_element(matrix, row, col):
    visible = 0
    element = int(matrix[row][col])
    #retrieve row
    rowX = matrix[row][:]
    #convert from string to int in row
    rowX = [eval(i) for i in rowX]
    colY = []
    #fetch all int in the column of the element
    for rad in matrix:
        colY.append(int(rad[col]))

    #check row
    if element > max(rowX[:col]) or element > max(rowX[col+1:]):
        visible += 1
    else:
        #check column
        if element > max(colY[:row]) or element > max(colY[row+1:]):
            visible += 1

    return visible

def check_visibility(matrix, rowlength, noOfRows):
    row = 0
    col = 0
    count = 0
    visible = False
    #process all columns in all rows
    while row < noOfRows:
        #process all columns
        while col < rowlength:
            if row == 0 or row == (noOfRows-1): count += 1 # in first & last row, all cols are visible
            else:
                if col == 0 or col == (rowlength-1): count += 1 # in first & last column row, all cols are visible
                else: 
                    visible = check_element(matrix, row, col)
                    if visible: count += 1
            col += 1
        row += 1
        col = 0

    return count

def process_the_data(theData):
    #find answer
    visible = 0
     #find all the columns from the dataset
    matrix, rowlength, noOfRows = find_cols(theData)

    visible = check_visibility(matrix, rowlength, noOfRows)
    
    return visible

def get_the_data():
    #read the test puzzle input 
    #theData = open('day82022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day82022_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        element = element.strip()
        data_list.append(element)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: ...
    valueX = process_the_data(theData) 
    
    print('how many trees are visible from outside the grid -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()

