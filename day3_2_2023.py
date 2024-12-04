# Template for Advent of Code
# source: https://adventofcode.com/

import os
import re

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 3 part 1 .... >')
    print()
    return

def find_num(row):
    #find number in row
    a_num = re.compile(r'\d+')
    all_num = re.findall(a_num, row)
    return all_num

# find any number adjacent to a symbol in the row
# this includes above, below, right and left
def check_numb(matrix,current_row, last_row, frompos, topos):
    #symbols defined
    a_sym = re.compile(r'[0-9]')
    #initialize
    symb_adjacent = False
    fromRow = current_row
    toRow = current_row
    #check to the left, right of frompos, topos startpos if possible to get all adjacent
    #define rectangel to check
    if frompos > 0: frompos -= 1
    if topos < len(matrix[current_row]): topos += 1
    if current_row > 0: fromRow -= 1
    if current_row < last_row: toRow += 1
    #check row above
    i = fromRow
    j = frompos
    while i <= toRow:
        while j < topos:
            # check if cell is a non-numeriq symbol
            match = re.search(a_sym, matrix[i][j])
            if match:
                symb_adjacent = True
                break
            #next column
            j += 1
        
        #next row if not found
        if symb_adjacent:
            break
        else:
            i += 1
            j = frompos #start from left most position of the next row

    return symb_adjacent

def create_matrix(theData):
    matrix = []
    for row in theData:
        x = list(row)
        matrix.append(x)
    return matrix

#start function
def process_codes(theData):
    # move theData into a list of lists
    matrix = create_matrix(theData)
    # find any number adjacent to a symbol

    return 42
#end function

def get_the_data():
    #read the puzzle input like this if a list without separation chars
    theData = open('day32023_test_puzzle_input.txt', 'r')
    #theData = open('day32023_puzzle_input.txt', 'r')
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
    
    print('\nWhat is the sum of all of the part numbers? ', valueX, '\n')

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()