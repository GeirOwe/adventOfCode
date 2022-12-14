# Day9 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/9
from itertools import count
import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 9, part 1 .... >')
    print()
    return

def trail_size(theData):
    trail = []
    rad = [] 
    x = 0
    y = 0
    for row in theData:
        splitX = row.split()
        dir = splitX[0]
        move = int(splitX[1])
        #find borders
        if dir == 'R':
            if (move*2) > x: x = move*2
        if dir == 'L':
            if (move*2) > x: x = move*2
        if dir == 'U':
            if (move*2) > y: y = move*2
        if dir == 'D':
            if (move*2) > y: y = move*2
    
    i = 0
    j = 0
    # prepare trail
    while j < y:
        while i < x:
            rad.append('.')
            i += 1
        trail.append(rad)
        j += 1 

    return trail

# do the move and watch the tail
# If the head is ever two steps directly up, down, left, or right from the tail, 
# the tail must also move one step in that direction
def do_the_move(trail, dir, move, hX, hY, tX, tY):
    # move head once and check distance to tail
    # fter each step, you'll need to update the position of the tail. 
    # head moves only in straight lines - tail moves vertically when needed
    return trail, hX, hY, tX, tY

def process_the_data(theData):
    #find answer
    valueX = 0
    #current pos
    hX = 0
    hY = 0
    tX = 0
    tY = 0
    trail = trail_size(theData)
    
    for row in theData:
        # fetch instruction
        splitX = row.split()
        dir = splitX[0]
        move = splitX[1]
        trail, hX, hY, tX, tY  = do_the_move(trail, dir, move, hX, hY, tX, tY)
    
    #count where tail has been
    for row in trail:
        valueX = valueX + trail[0].count('.')

    return valueX

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

