# Day9 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/9

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 9, part 2 .... >')
    print()
    return

#define a grid object
class Grid():
    def __init__(self, row_length, col_height):
        self.row_length = row_length
        self.col_height = col_height
        self.grid_row = []
        self.grid = []
        self.trail_length = 0

    #the row length of the grid
    def get_row_length(self):
        return self.row_length

    #the column height of the grid
    def get_col_height(self):
        return self.col_height

    #add dots to grid
    def initialize_grid(self):
        i = 0
        j = 0
        # prepare trail with dots
        while j < self.col_height:
            while i < self.row_length:
                self.grid_row.append('.')
                i += 1
            #row is complete
            self.grid.append(self.grid_row)
            #next row start in column zero
            i = 0
            #next row
            j += 1 
        self.grid = np.array(self.grid)

    def mark_snake(self, row, col):
        self.grid[row][col] = '#'
    def get_trail_length(self):     #count where tail has been
        self.trail_length = np.sum(self.grid == '#')
        return self.trail_length
#end class definition

#define a snake object
class Snake():
    def __init__(self, tail_length):
        self.tail_length = tail_length
        self.head_pos_row = 0
        self.head_pos_col = 0
        self.prev_head_pos_row = 0
        self.prev_head_pos_col = 0
        self.tail_pos_row = 0
        self.tail_pos_col = 0
    
    #the row length of the grid
    def get_head_pos_row(self):
        return self.head_pos_row
    def get_head_pos_col(self):
        return self.head_pos_col
    def get_tail_pos_row(self):
        return self.tail_pos_row
    def get_tail_pos_col(self):
        return self.tail_pos_col
    def get_prev_head_pos_row(self):
        return self.prev_head_pos_row
    def get_prev_head_pos_col(self):
        return self.prev_head_pos_col

    #the column height of the grid
    def get_tail_length(self):
        return self.tail_length
#end class definition


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
def do_the_move(snake, dir, move):
    i = 0
    # move head once and check distance to tail
    while i < move:
        #move the head
        snake.move_head(dir)
        # after each step, you'll need to update the position of the tail.
        snake.move_tail()
        j = snake.get_tail_length
        while j > 0:
            snake.move_tail()
        i += 1
    return

def process_the_data(theData):
    #create a snake object
    snake = Snake(1)
    #create a grid object
    grid = Grid(5, 5)
    grid.initialize_grid()
    #grid.mark_snake(0, 0)
    #print(snake.get_tail_pos_row(), snake.get_tail_pos_col())

    #do all the moves
    for row in theData:
        # fetch instruction
        splitCol = row.split()
        dir = splitCol[0]
        move = int(splitCol[1])
        #do the move
        do_the_move(snake, grid, dir, move)

    return grid.get_trail_length()

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

