# Day20 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/20

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 20, part 1 .... >')
    print()
    return

# convert from pixels to binary ["...#...#."] -> ["000100010"]
def pix_2_binary(the_9_pixels):
    i = 0
    binaryX = ""
    pix = the_9_pixels[0]
    #check all fields in list. "." -> 0 and "#" -> 1
    while i < 9:
        if pix[i] == ".": binaryX += "0"
        else: binaryX += "1"
        i += 1
    return binaryX

# find all adjacent cells and add content of all cells to a list
def find_adjacent_pixels(grid, element):
    the_9_pixels = ["...#...#."]
    return the_9_pixels

def find_adjacent_pixelsOLD(grid, element):
    #the 9 pixels - around and including the pos - visualised here with a zero:
    #   # . . # .
    #   #[. . .].
    #   #[# 0 .]#
    #   .[. # .].
    #   . . # # #
    the_9_pixels = ""

    adjacent_pos = []
    maxRow, maxCol = grid.shape
    maxRow -= 1 #starting from zero
    maxCol -= 1 #starting from zero
    elementProcessed = False
    # check all 4 corners - use dots for all positions "outside the grid"
    if element == [0,0]: 
        the_9_pixels = the_9_pixels + "...." + grid[0,0] + grid[0, 1] + "." + grid[1, 0] + grid[1, 1]
        elementProcessed = True
    if element == [0,maxCol]: 
        the_9_pixels = the_9_pixels + "..." + grid[0, maxCol-1] + grid[0,maxCol] + "." + grid[1, maxCol-1] + grid[1, maxCol] + "."
        elementProcessed = True
    if element == [maxRow,maxCol]: 
        the_9_pixels = the_9_pixels + grid[maxRow-1, maxCol-1] + grid[maxRow-1, maxCol] + "." + grid[maxRow, maxCol-1] + grid[maxRow,maxCol] + "...."
        elementProcessed = True
    if element == [maxRow,0]: 
        adjacent_pos.append([maxRow, 1]); adjacent_pos.append([maxRow-1, 1]); adjacent_pos.append([maxRow-1, 0]) #right, vertical, up
        the_9_pixels = the_9_pixels + "." + 
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
        # we are only to flash once pr step
        if grid[row, col] != -1 and grid[row, col] < 10: 
            grid[row, col] += 1

    return the_9_pixels

# do a new step
def step_away(input_image, image_algo, valueX):
    output_image = input_image
    maxRow, maxCol = input_image.shape
    row = 0
    while row < maxRow: 
    #REPEAT for all pixels i input picture
    #   for each dot in input image - find the 9 pixels around a dot -> e.g. [...#...#.]
        col = 0
        while col < maxCol:
            cell = [row, col]
            the_9_pixels = find_adjacent_pixels(input_image, cell)
            #   transform from pixel to binary -> e.g. [000100010]
            binaryX = pix_2_binary(the_9_pixels)
            #   convert from binary to decimal -> e.g. 34
            numX = int(binaryX, 2)
            #   find the symbol in that specific pos in image algo -> image_algo[34] -> "#"
            outSymbol = image_algo[numX]
            #   add that symbol to the OUTPUT PICTURE in same position as in input image
            output_image[row, col] = outSymbol
            #   if pixel is lit in output picture (i.e. "#") -> , valueX += 1
            if outSymbol == "#": valueX += 1
            #next column
            col += 1
        
        #next row
        row += 1

    resulting_image = output_image

    return valueX, resulting_image

# process the data with all indicated steps
def process_the_data(input_image, image_algo):
    #number of steps
    noSteps = 1
    i = 0
    #list_of_10 = []
    while i < noSteps:
        #valueX holds the number of lit pixels
        valueX = 0
        #do a step and see what changes are done to the input image
        #the resulting image from the setp is the new input image for next cycle
        valueX, input_image = step_away(input_image, image_algo, valueX)
        i += 1
    return valueX

def get_the_data():
    #read the test puzzle input 
    theData = open('day20_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day20_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    rows = 0 # in image
    firstRow = True
    #process each row in the data
    for element in theData:
        elementTrimmed = element.strip()
        if firstRow:
            image_algo = elementTrimmed
            firstRow = False
        elif elementTrimmed != "": 
            rows += 1   #one more row in input image
            #add each single char to a list - reformat to numpy array later
            i = 0
            while i < len(elementTrimmed):
                data_list.append(elementTrimmed[i])
                i += 1

    maxCols = len(elementTrimmed)
    maxRows = rows
    #create a numpy array
    input_image = np.array(data_list, dtype="str").reshape(maxRows, maxCols)
    return input_image, image_algo

def start_the_engine():
    #get the data and read them into a list
    input_image, image_algo = get_the_data()
    
    #process the data and return the answer
    valueX = process_the_data(input_image, image_algo)

    # Next, you need to 
    print('\nHow many pixels are lit in the resulting image ->', valueX, '\n')
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()