# Day9 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/9

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 9, part 2 .... >')
    print()
    return

def trail_size(theData):
    trail = []
    rad = [] 
    # just preparing a grid / trail of 1000 x 1000
    x = 30
    y = 30
    i = 0
    j = 0
    # prepare trail with dots
    while j < y:
        while i < x:
            rad.append('.')
            i += 1
        trail.append(rad)
        j += 1 

    trailX = np.array(trail)
    return trailX

def move_tail(hCol, hRow, tCol, tRow):
    # head moves only in straight lines - tail moves vertically when needed
    tail_moved = False
    #on same column, move up
    if hCol == tCol and hRow > (tRow+1): 
        tRow += 1
        tail_moved = True
    #on same column, move down
    if hCol == tCol and hRow < (tRow-1): 
        tRow -= 1
        tail_moved = True
    #on same line, move right
    if hRow == tRow and hCol > (tCol+1): 
        tCol += 1
        tail_moved = True
    #on same line, move left
    if hRow == tRow and hCol < (tCol-1): 
        tCol -= 1
        tail_moved = True
    #vertically?
    if hCol != tCol or hRow != tRow:
        #vertically right
        if hCol > tCol+1:
            tRow = hRow
            tCol = hCol-1
            tail_moved = True
        #vertically left
        if hCol < tCol-1: 
            tRow = hRow
            tCol = hCol+1
            tail_moved = True
        #vertically down
        if hRow < tRow-1: 
            tCol = hCol
            tRow = hRow+1
            tail_moved = True
        #vertically up
        if hRow > tRow+1: 
            tCol = hCol
            tRow = hRow-1
            tail_moved = True

    return hCol, hRow, tCol, tRow, tail_moved

# do the move and watch the tail
# If the head is ever two steps directly up, down, left, or right from the tail, 
# the tail must also move one step in that direction
def do_the_move(trail, dir, move, hCol, hRow, tCol, tRow, tail_length):
    i = 0
    # move head once and check distance to tail
    while i < move:
        if dir == 'R': hCol += 1     #move right on same row
        if dir == 'L': hCol -= 1     #move left on same row
        if dir == 'U': hRow += 1     #move up a row
        if dir == 'D': hRow -= 1     #move down a row
        # after each step, you'll need to update the position of the tail.
        # track head_pos before it moves.
        org_hCol = hCol
        org_hRow = hRow
        #move the complete tail
        j = tail_length
        while j > 0:
            # track tail_pos before it moves.
            pt_row = tRow
            pt_col = tCol
            hCol, hRow, tCol, tRow, tail_moved = move_tail(hCol, hRow, tCol, tRow)
            #one less tail to check
            j -= 1
            #whenever head moves to a new spot - mark in the trail
            if tail_moved: 
                trail[tRow][tCol] = '#'

                if tail_length < 9: tail_length += 1
                # the tail becomes the new head, next tail position also needs to move
                hCol = tCol
                hRow = tRow
                tCol = pt_col
                tRow = pt_row
        i += 1
        #reset header data - since used to move tail
        hRow = org_hRow
        hCol = org_hCol

    return trail, hCol, hRow, tCol, tRow, tail_length

def process_the_data(theData):
    #find answer
    valueX = 0
    #current pos
    hCol = 0
    hRow = 0
    tCol = 0
    tRow = 0
    trail = trail_size(theData)
    tail_length = 1
    #start position
    trail[0][0] = '#'
    #do all the moves
    for row in theData:
        # fetch instruction
        splitCol = row.split()
        dir = splitCol[0]
        move = int(splitCol[1])
        #do the move
        trail, hCol, hRow, tCol, tRow, tail_length  = do_the_move(trail, dir, move, hCol, hRow, tCol, tRow, tail_length)
    
    #count where tail has been
    valueX = np.sum(trail == '#')

    return valueX

def get_the_data():
    #read the test puzzle input 
    theData = open('day92022_test2_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day92022_puzzle_input.txt', 'r')
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
    
    print('count up all of the positions the tail visited at least once -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()

