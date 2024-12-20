# Day5 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/5

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 4, part 1 .... >')
    print()
    return

def add_signal_to_row(fra, til, row, signalGrid):
    if fra < til:
        fromX = fra
        toX = til
    else:
        fromX = til
        toX = fra
    #increase number in grid for all cells in row in the range
    while fromX <= toX:
        signalGrid[row, fromX] += 1
        fromX += 1
    return signalGrid

def add_signal_to_col(fra, til, column, signalGrid):
    if fra < til:
        fromY = fra
        toY = til
    else:
        fromY = til
        toY = fra
    #increase number in grid for all cells in row in the range
    while fromY <= toY:
        signalGrid[fromY, column] += 1
        fromY += 1
    return signalGrid

def process_the_data(linesData, signalGrid):
    #les linje for linje
    i = 0
    while i < len(linesData):
    #hvis lik y ( linesData[i, 1] == linesData[i, 3] ) -> sett inn signal på en rad
    # ifra linesData[i, 0] t.o.m linesData[i, 2]
    #hvis lik x ( linesData[i, 0] == linesData[i, 2] ) -> sett inn signal på en kolonne
    # ifra linesData[1] t.o.m linesData[3]
        y1 = linesData[i, 1]
        y2 = linesData[i, 3]
        x1 = linesData[i, 0]
        x2 = linesData[i, 2]
        #add signals to a row if y1 = y2
        if y1 == y2:
            signalGrid = add_signal_to_row(x1, x2, y1, signalGrid) # -> fromX, toX, row, grid
        #add signals to a column if x1 = x2
        if x1 == x2:
            signalGrid = add_signal_to_col(y1, y2, x1, signalGrid) # -> fromY, toY, column, grid

        i += 1
    #the signalgrid is done -> now calculate no of points (cells) > 1
    valueX = (signalGrid > 1).sum()

    return valueX

def get_coord(row):
    temp = row.split("->")
    temp1 = temp[0].split(",")
    temp2 = temp[1].split(",")
    x1 = int(temp1[0].strip())
    y1 = int(temp1[1].strip())
    x2 = int(temp2[0].strip())
    y2 = int(temp2[1].strip())
    return x1, y1, x2, y2

def optimize_the_data(theData):
    coords = []
    noOfRows = 0
    rowsInGrid = 0 #used when reshaping the arrayGrid
    colsInGrid = 0 #used when reshaping the arrayGrid

    for row in theData:
        #find coordinates and save largest y-coordinate
        x1, y1, x2, y2 = get_coord(row)
        if y1 > colsInGrid:
            colsInGrid = y1
        if y2 > colsInGrid:
            colsInGrid = y2
        if x1 > rowsInGrid:
            rowsInGrid = x1
        if x2 > rowsInGrid:
            rowsInGrid = x2

        if x1 == x2 or y1 == y2:
            #add them to a list, reshape in the numpy array
            coords.append(x1)
            coords.append(y1)
            coords.append(x2)
            coords.append(y2)
            noOfRows += 1
    
    #move them into numpy arrays - to make it easier to process
    #array (x, y) -> rows, columns -> : means all elements
    #add 1 to rowsInGrid / colsInGrid since we started on zero
    rowsInGrid += 1
    colsInGrid += 1
    linesData = np.array(coords, dtype = "int").reshape(noOfRows, 4)
    signalGrid = np.zeros(int(rowsInGrid*colsInGrid), dtype = "int").reshape(rowsInGrid, colsInGrid)
    #print(linesData[1, :], " -> expect 2nd row, all numbers -> 9 4 3 4")
    #print(linesData)
    #print(signalGrid)
    print("rows: ", rowsInGrid, " cols: ", colsInGrid)
    return linesData, signalGrid

def get_the_data():
    #read the test puzzle input 
    #theData = open('day52021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day52021_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        if elementTrimmed != "":
            data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    linesData, signalGrid = optimize_the_data(theData)
    
    #process the data and return the answer
    valueX = process_the_data(linesData, signalGrid) 
    
    print('the number of points where at least two lines overlap -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()