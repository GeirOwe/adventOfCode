# Day20 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/20

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 20, part 1 .... >')
    print()
    return

# convert from pixels to binary "...#...#." -> "000100010"
def pix_2_binary(the_9_pixels):
    i = 0
    binaryX = ""
    pix = the_9_pixels
    #check all fields in list. "." -> 0 and "#" -> 1
    while i < 9:
        if pix[i] == ".": binaryX += "0"
        else: binaryX += "1"
        i += 1
    return binaryX

# find all adjacent cells and add content of all cells to a string
def find_adjacent_pixels(grid, element):
    #the 9 pixels - around and including the pos - visualised here with a zero:
    #   # . . # .
    #   #[. . .].
    #   #[# 0 .]#
    #   .[. # .].
    #   . . # # #
    the_9_pixels = ""
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
        the_9_pixels = the_9_pixels + "." + grid[maxRow-1, 0] + grid[maxRow-1, 1] + "." + grid[maxRow, 0] + grid[maxRow, 1] + "..."
        elementProcessed = True
   
    #check if first column or last column
    if elementProcessed != True:
        if element[1] == 0: #first column
            row = element[0]
            the_9_pixels = the_9_pixels + "."+grid[row-1, 0]+grid[row-1, 1] + "."+grid[row, 0]+grid[row, 1] + "."+grid[row+1, 0]+grid[row+1, 1]
            elementProcessed = True
        elif element[1] == maxCol: #last column
            row = element[0]
            the_9_pixels = the_9_pixels + grid[row-1, maxCol-1]+grid[row-1, maxCol]+"."+ grid[row, maxCol-1]+grid[row, maxCol]+"." + grid[row+1, maxCol-1]+grid[row+1, maxCol]+"."
            elementProcessed = True

    #check if first row or last row
    if elementProcessed != True:
        if element[0] == 0: #first row
            col = element[1]
            the_9_pixels = the_9_pixels + "..."+grid[0, col-1]+grid[0, col]+grid[0, col+1]+grid[1, col-1]+grid[1, col]+grid[1, col+1]
            elementProcessed = True
        elif element[0] == maxRow: #last row
            col = element[1]
            the_9_pixels = the_9_pixels + grid[maxRow-1, col-1]+grid[maxRow-1, col]+grid[maxRow-1, col+1]+grid[maxRow, col-1]+grid[maxRow, col]+grid[maxRow, col+1] + "..."
            elementProcessed = True
    
    #the position is in the middle if still false
    if elementProcessed != True:
        row = element[0]
        col = element[1]
        the_9_pixels = the_9_pixels + grid[row-1, col-1]+grid[row-1, col]+grid[row-1, col+1]+grid[row, col-1]+grid[row, col]+grid[row, col+1] + grid[row+1, col-1]+grid[row+1, col]+grid[row+1, col+1]

    return the_9_pixels

# do a new step
def step_away(input_image, image_algo, valueX):
    maxRow, maxCol = input_image.shape
    #start with an empty output image
    data_list = ["."] * (maxRow * maxCol)
    output_image = np.array(data_list, dtype="str").reshape(maxRow, maxCol)

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

    return valueX, output_image

# process the data with all indicated steps
def process_the_data(input_image, image_algo):
    #number of steps
    noSteps = 2
    i = 0
    #list_of_10 = []
    while i < noSteps:
        #valueX holds the number of lit pixels
        valueX = 0
        #do a step and see what changes are done to the input image
        #the resulting image from the setp is the new input image for next cycle
        valueX, input_image = step_away(input_image, image_algo, valueX)

        i += 1
    #print(input_image, "\n")
    return valueX

#add some empty columns
def add_cols(data_list, cols):
    n = 0
    while n < cols:
        data_list.append(".")
        n += 1
    return data_list

#add some empty rows
def add_rows(data_list, rows, cols):
    n = 0
    while n < rows*cols:
        data_list.append(".")
        n += 1
    return data_list

def get_the_data():
    #read the test puzzle input 
    theData = open('day20_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day20_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    rows = 0 # in image
    firstRow = True
    emptyRows = 5

    #process each row in the data
    for element in theData:
        elementTrimmed = element.strip()
        if firstRow:
            image_algo = elementTrimmed
            firstRow = False
        elif elementTrimmed != "": 
            #add X empty rows and X empty cols before or after data; to simulate the infinity outwards of the grid
            if rows == 0:
                data_list = add_rows(data_list, emptyRows, len(elementTrimmed)+emptyRows*2) # *2 -> i begynnelsen og slutten av linjen

            rows += 1   #one more row in input image
            #add each single char to a list - reformat to numpy array later
            i = 0
            while i < len(elementTrimmed):
                #add 5 empty cols before the data; to simulate the infinity outwards of the grid
                if i == 0: 
                    data_list = add_cols(data_list, emptyRows)
                
                data_list.append(elementTrimmed[i])
                i += 1
                
                #add 5 empty cols after the data; to simulate the infinity outwards of the grid
                if i == len(elementTrimmed): 
                    data_list = add_cols(data_list, emptyRows)

    #add 5 empty rows and 5 empty cols before or after data; to simulate the infinity outwards of the grid
    data_list = add_rows(data_list, emptyRows, len(elementTrimmed)+emptyRows*2)

    maxCols = len(elementTrimmed) + emptyRows*2
    maxRows = rows + emptyRows*2
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