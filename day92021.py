# Day9 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/9

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 9, part 1 .... >')
    print()
    return

def find_low_points(the_map, numOfRows, numOfCols):
    low_points_list = []
    row = 0
    lastRow = numOfRows -1  #since we start at zero
    while row < numOfRows:
        col = 0
        while col < numOfCols:
            if row == 0:
                #process first row
                if col == 0:
                    #process first col
                    if (the_map[row, col+1] > the_map[row, col] and      #signal to the right
                        the_map[row+1, col] > the_map[row, col]):       #signal below
                        low_points_list.append(the_map[row, col])
                elif col == (numOfCols -1):
                    #process last col
                    if (the_map[row, col-1] > the_map[row, col] and      #signal to the left
                        the_map[row+1, col] > the_map[row, col]):          #signal below
                        low_points_list.append(the_map[row, col])
                else:
                    #process the other cols
                    if (the_map[row, col-1] > the_map[row, col] and      #signal to the left
                        the_map[row, col+1] > the_map[row, col] and      #signal to the right
                        the_map[row+1, col] > the_map[row, col]):        #signal below
                        low_points_list.append(the_map[row, col])
            elif row == lastRow:
                #process last row
                if col == 0:
                    #process first col
                    if (the_map[row, col+1] > the_map[row, col] and     #signal to the right
                        the_map[row-1, col] > the_map[row, col]):         # signal above
                        low_points_list.append(the_map[row, col])
                elif col == (numOfCols -1):
                    #process last col
                    if (the_map[row, col-1] > the_map[row, col] and      #signal to the left
                        the_map[row-1, col] > the_map[row, col]):     # signal above
                        low_points_list.append(the_map[row, col])
                else:
                    #process the other cols
                    if (the_map[row, col-1] > the_map[row, col] and      #signal to the left
                        the_map[row, col+1] > the_map[row, col] and     #signal to the right
                        the_map[row-1, col] > the_map[row, col]):         # signal above
                        low_points_list.append(the_map[row, col])
            else:
                #process the other rows
                if col == 0:
                    #process first col
                    if (the_map[row, col+1] > the_map[row, col] and     #signal to the right
                        the_map[row-1, col] > the_map[row, col] and     # signal above
                        the_map[row+1, col] > the_map[row, col]):       #signal below
                        low_points_list.append(the_map[row, col])
                elif col == (numOfCols -1):
                    #process last col
                    if (the_map[row, col-1] > the_map[row, col] and      #signal to the left
                        the_map[row-1, col] > the_map[row, col] and     # signal above
                        the_map[row+1, col] > the_map[row, col]):       #signal below
                        low_points_list.append(the_map[row, col])
                else:
                    #process the other cols
                    if (the_map[row, col-1] > the_map[row, col] and      #signal to the left
                        the_map[row, col+1] > the_map[row, col] and     #signal to the right
                        the_map[row-1, col] > the_map[row, col] and     # signal above
                        the_map[row+1, col] > the_map[row, col]):       #signal below
                        low_points_list.append(the_map[row, col])
            col += 1
        row += 1       
    return low_points_list

def summarize_risk(low_points_list):
    sumRiskLowPoints = 0
    for element in low_points_list:
        # The risk level of a low point is 1 plus its height.
        sumRiskLowPoints = sumRiskLowPoints + element + 1
    return sumRiskLowPoints

def process_the_data(the_map, numOfRows, numOfCols):
    sumRiskLowPoints = 0
    # Your first goal is to find the low points - the locations that are lower than any of its adjacent locations.
    low_points_list = find_low_points(the_map, numOfRows, numOfCols)
    print('\nthe low points -> ', low_points_list,'\n')
    # What is the sum of the risk levels of all low points on your heightmap
    sumRiskLowPoints = summarize_risk(low_points_list)
    return sumRiskLowPoints

def build_map(theData):   
    numOfRows = len(theData)
    map_list = []
    for row in theData:
        numOfCols = len(row)
        i = 0   #the positio in the row
        while i < numOfCols:
            #add numbers on the borad to along list - it will be reshaped into a 5x5 board in numpy array
            map_list.append(int(row[i]))
            i += 1
     
    #move them into numpy arrays - to make it easier to process
    #array (x, y, z) -> board, rows, columns -> : means all elements
    the_map = np.array(map_list, dtype = "int").reshape(numOfRows, numOfCols)
    return the_map, numOfRows, numOfCols

def get_the_data():
    #read the test puzzle input 
    #theData = open('day92021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day92021_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    the_map, numOfRows, numOfCols = build_map(theData)
    
    #process the data and return the answer
    valueX = process_the_data(the_map, numOfRows, numOfCols)
    
    print('\nthe sum of the risk levels of all low points -> ', valueX,'\n')
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()