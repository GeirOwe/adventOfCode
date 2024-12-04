# Day13 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/13

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 13, part 2 .... >')
    print()
    return

def fold_horizontally(the_map,fold, splitPos, maxCol):
    row = len(the_map)-1 #starting at zero
    maxCol -= 1 #starting at zero
    # use shape instead
    shapeX = the_map.shape
    row = shapeX[0] - 1
    maxCol = shapeX[1] -1
    #repeat from last row and up till split poistion
    rows_processed = 0
    while row > splitPos:
        col = 0
        while col < maxCol:
            #take the content of this col in the row to be folded, and add to 
            # the top row i.e. row = 0+rows_processed
            if the_map[row, col] == "#": the_map[0+rows_processed, col] = "#"
            #move to next column
            col += 1
        #increase number of rows folded
        rows_processed += 1
        #process next row
        row -= 1
    #delete all the folded rows, do not include the splitPos line
    splitPos += 1
    # n = 2 -> rsyntax to remove last two rows of array -> a[:-n, :]
    folded_map = the_map[:-splitPos, :]
    return folded_map

def fold_vertically(the_map,fold, splitPos, maxCol):
    maxRow = len(the_map)-1 #starting at zero
    col = maxCol - 1 #starting at zero
    # use shape instead
    shapeX = the_map.shape
    maxRow = shapeX[0] - 1
    col = shapeX[1] -1
    #repeat from last column and up till split poistion
    cols_processed = 0
    while col > splitPos:
        row = 0
        while row < maxRow:
            #take the content of this row in the col to be folded, and add to 
            # the first col i.e. col = 0+cols_processed
            if the_map[row, col] == "#": the_map[row, 0+cols_processed] = "#"
            #move to next row
            row += 1
        #increase number of cols folded
        cols_processed += 1
        #process next col
        col -= 1
    #delete all the folded columns, do not include the splitPos column
    splitPos += 1
    # n = 2 -> rsyntax to remove last two columns of array -> a[:, :-n]
    folded_map = the_map[:, :-splitPos]
    return folded_map

def fold_the_map(the_map, fold_instr, maxCol):
    #part 2 - do all first folding instruction
    noOfFolds = len(fold_instr)
    folded_map = the_map
    i = 0
    while i < noOfFolds:
        split = fold_instr[i].split("=")
        #find split position
        splitPos = int(split[1])
        #fold along x or y
        #fold according to first fold_instructions only
        if "y" in split[0]: 
            fold = "y"
            folded_map = fold_horizontally(folded_map,fold, splitPos, maxCol)
        else: 
            fold = "x"
            folded_map = fold_vertically(folded_map,fold, splitPos, maxCol)
        #print("split instruction ", fold, ":", splitPos)
        i += 1
    return folded_map

def process_the_data(the_map, coord_list, numOfRows, numOfCols, fold_instr):
    valueX = 0
    # x coordinates equals column
    #y coordinates equals row
    for row in coord_list:
        col = int(row[0])
        row = int(row[1])
        the_map[row, col] = "#"
    
    folded_map = fold_the_map(the_map, fold_instr, numOfCols)
    #replace all "." with "" - it will be easier to read the letters
    #x[x=='d'] = 'z'
    folded_map[folded_map=="."] = " "
    #print the letters
    print(folded_map[0:, 0:15]) #x[1::2, 1::2]
    print()
    print(folded_map[0:, 15:30]) #x[1::2, 1::2]
    print()
    print(folded_map[0:, 30:]) #x[1::2, 1::2]
    # then, count number of  #  in the folded map
    # syntax:   y = np.array([1, 2, 2, 2, 2, 0, 2, 3, 3, 3, 0, 0, 2, 2, 0])
    #           np.count_nonzero(y == 1)
    valueX = np.count_nonzero(folded_map == "#")
    return valueX

def build_map(theData):   
    #theData contains a string element with x, y coord

    numOfRows = len(theData)
    coord_list = []
    maxRow = 0
    maxCol = 0
    for row in theData:
        splitRow = row.split(",")
        x = int(splitRow[0])
        y = int(splitRow[1])
        #add numbers on the borad to along list - it will be reshaped into a numpy array later
        coord_list.append(splitRow)
        #store max X and Y to create array later
        if x > maxCol: maxCol = x #columns
        if y > maxRow: maxRow = y # rows
    
    #increase rows and cols with one to allow for fold
    maxRow += 1
    maxCol += 1

    #move them into numpy arrays - to make it easier to process
    #array (x, y) -> rows, columns -> : means all elements
    a=np.empty(maxRow * maxCol, dtype = "str")
    a.fill(".")
    the_map = a.reshape(maxRow, maxCol)
    return the_map, coord_list, maxRow, maxCol

def get_the_data():
    #read the test puzzle input 
    #theData = open('day132021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day132021_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    fold_instr = []
    for element in theData:
        elementTrimmed = element.strip()
        if elementTrimmed == "": print()
        elif "fold" in elementTrimmed: fold_instr.append(elementTrimmed)
        else: data_list.append(elementTrimmed)
    return data_list, fold_instr

def start_the_engine():
    #get the data and read them into a list
    theData, fold_instr = get_the_data()
    the_map, coord_list, numOfRows, numOfCols = build_map(theData)
    
    #process the data and return the answer
    valueX = process_the_data(the_map, coord_list, numOfRows, numOfCols, fold_instr)

    # Next, you need to 
    print('\nexpected -> RKH FZG UB\n')
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()