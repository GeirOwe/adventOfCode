# Day8 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/8
import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 8, part 2 .... >')
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

def check_element(matrix, row, col, rowlength, noOfRows):
    #start at zero
    rowlength -= 1
    noOfRows -= 1
    #the element to measure
    element = int(matrix[row][col])
    #retrieve row
    rowX = matrix[row][:]
    #convert from string to int in row
    rowX = [eval(i) for i in rowX]
    colY = []
    #fetch all int in the column of the element
    for rad in matrix:
        colY.append(int(rad[col]))

    # stop if you reach an edge or at the first tree 
    # that is the same height or taller than the tree under consideration
    #check up
    up = 1
    y = row
    while y > 1:
        if element > colY[y-1]: up +=1
        elif element == colY[y-1]: break
        #move up none row
        y -= 1
    #check down
    down = 1
    y = row
    while y < (noOfRows-1): #stop but count last row
        if element > colY[y+1]: down +=1
        elif element == colY[y+1]: break
        #move down one row
        y += 1
    #check left
    left = 1
    x = col
    while x > 1:
        if element > rowX[x-1]: left +=1
        elif element == rowX[x-1]: break
        #move up none row
        x -= 1
    #check right
    right =1
    x = col
    while x < (rowlength-1): #stop but count last column
        if element > rowX[x+1]: right +=1
        elif element == rowX[x+1]: break
        #move down one row
        x += 1

    #calculate the score for the element
    score = up * down * right * left

    return score

def check_visibility(matrix, rowlength, noOfRows):
    row = 0
    col = 0
    count = 0
    high_score = 0
    visible = False
    #process all columns in all rows
    while row < noOfRows:
        #process all columns
        while col < rowlength:
            if row == 0 or row == (noOfRows-1): count = 0 # in first & last row, all cols are visible
            else:
                if col == 0 or col == (rowlength-1): count = 0 # in first & last column row, all cols are visible
                else: 
                    count = check_element(matrix, row, col, rowlength, noOfRows)
                    if count > high_score: high_score = count
            col += 1
        row += 1
        col = 0

    return high_score

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
    
    print('What is the highest scenic score possible for any tree -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()

