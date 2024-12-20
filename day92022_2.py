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
    def __init__(self, row_length, col_height, start_row, start_col):
        self.row_length = row_length
        self.col_height = col_height
        self.start_row = start_row
        self.start_col = start_col
        self.grid_row = []
        self.grid = []
        self.trail_length = 0

    #the row length of the grid
    def get_row_length(self):
        return self.row_length

    #the column height of the grid
    def get_col_height(self):
        return self.col_height

    def mark_snake(self, row, col):
        self.grid[row][col] = '#'

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
            #next row, start in column zero with an empty row
            j += 1
            i = 0
            self.grid_row = []
        self.grid = np.array(self.grid)
        self.mark_snake(self.start_row, self.start_col)

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
        self.prev_tail_pos_row = 0
        self.prev_tail_pos_col = 0
        self.tail = []
        self.tail_rc = []
    
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
    def get_prev_tail_pos_row(self):
        return self.prev_head_pos_row
    def get_prev_tail_pos_col(self):
        return self.prev_head_pos_col

    def set_head_pos_row(self, pos):
        self.head_pos_row = pos
    def set_head_pos_col(self, pos):
        self.head_pos_col = pos
    def set_tail_pos_row(self, pos):
        self.tail_pos_row = pos
    def set_tail_pos_col(self, pos):
        self.tail_pos_col = pos

    #the tail length
    def get_tail_length(self):
        return self.tail_length
    #the tail
    def get_tail_length(self):
        return self.tail    
    #move head one pos in the direction
    def move_head(self, dir):
        #save current pos
        self.prev_head_pos_row = self.head_pos_row
        self.prev_head_pos_col = self.head_pos_col
        #the, move
        if dir == 'R': self.head_pos_col += 1     #move right on same row
        if dir == 'L': self.head_pos_col -= 1     #move left on same row
        if dir == 'U': self.head_pos_row += 1     #move up a row
        if dir == 'D': self.head_pos_row -= 1     #move down a row
    
    def move_tail(self, grid):
        #add initial coordinates for tail
        if len(self.tail) == 0:
            self.tail_rc.append(self.tail_pos_row)
            self.tail_rc.append(self.tail_pos_col)
            self.tail.append(self.tail_rc)
            self.tail_rc = []
        #check if first element in tail need to move
        if abs(self.head_pos_row-self.tail_pos_row) > 1 or abs(self.head_pos_col-self.tail_pos_col) > 1:
            #save current pos
            self.prev_tail_pos_row = self.tail_pos_row
            self.prev_tail_pos_col = self.tail_pos_col
            #move the current pos of the tail
            self.tail_pos_row = self.prev_head_pos_row
            self.tail_pos_col = self.prev_head_pos_col
            #mark new tail pos in grid
            grid.mark_snake(self.tail_pos_row, self.tail_pos_col) 
            # add a new element to the tail
            self.tail_rc.append(self.tail_pos_row)
            self.tail_rc.append(self.tail_pos_col)
            self.tail.append(self.tail_rc)
            self.tail_rc = []

            #delete first row if larger than 9
            if len(self.tail) > 9:
                self.tail.pop(0)

            # manage the move of the rest of the tail
            # it is to make the same movement as the one before - if it needs to move!!
            # self.tail_row_move = self.tail_pos_row - self.prev_tail_pos_row
            # self.tail_col_move = self.tail_pos_col - self.prev_tail_pos_col
            # loop thru rest of the tail - maybe by a new method that is called recursively
            # i from 1 to len og tail
            #   tail to head & tail[i] to tail
            #   tail + tail to move
            #   row + row to move
            #   grid.mark_snake(
            #   repeat
               
        return
#end class definition

# do the move and watch the tail
# If the head is ever two steps directly up, down, left, or right from the tail, 
# the tail must also move one step in that direction
def do_the_move(grid, snake, dir, move):
    i = 0
    # move head once and check distance to tail
    while i < move:
        #move the head
        snake.move_head(dir)
        # after each step, you'll need to update the position of the tail.
        snake.move_tail(grid)
        #next move
        i += 1
    return

def process_the_data(theData):
    #start pos in grid
    row = 5
    col = 11
    #create a snake object
    snake = Snake(9)
    #create a grid object
    grid = Grid(1000, 1000, row, col)
    grid.initialize_grid()
    #set initial pos
    snake.set_head_pos_row(row)
    snake.set_head_pos_col(col)
    snake.set_tail_pos_row(row)
    snake.set_tail_pos_col(col)
    #do all the moves
    for row in theData:
        # fetch instruction
        splitCol = row.split()
        dir = splitCol[0]
        move = int(splitCol[1])
        #do the move
        do_the_move(grid, snake, dir, move)

    return grid.get_trail_length()

def get_the_data():
    #read the test puzzle input 
    theData = open('day92022_test_puzzle_input.txt', 'r')
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

