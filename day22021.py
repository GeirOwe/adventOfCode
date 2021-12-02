# Day2 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/2

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 2, part 2 .... >')
    print()

def move_sub(instruction, movement, horizontal_pos, depth, aim):
    # down X increases your aim by X units. up X decreases your aim by X units.
    # forward X does two things: It increases your horizontal position by X units. It increases your depth by your aim multiplied by X.

    #forward 5 adds 5 to your horizontal position 
    if instruction == 'forward':
        horizontal_pos = horizontal_pos + movement
        depth = depth + (aim * movement)
    #down 5 adds 5 to your depth
    if instruction == 'down':
        #depth = depth + movement -> removed in part 2 due to introduction of aim
        aim = aim + movement
    #up 3 decreases your depth by 3
    if instruction == 'up':
        #depth = depth - movement  -> removed in part 2 due to introduction of aim
        aim = aim - movement
    return horizontal_pos, depth, aim

def find_instr(theMove):
    #split the line at column. left part, xxx.[0], is the instruction. right part, xxx.[1], is the movement. 
    splitElement = theMove.split(' ')
    instruction = splitElement[0].strip().lower()
    movement = int(splitElement[1])
    return instruction, movement

def process_the_data(theData):
    #set initial position for the dataset
    noOfRows = len(theData)
    row = 0
    valueX = 0
    # Your horizontal position and depth both start at 0. so does aim.
    horizontal_pos = 0
    depth = 0
    aim = 0
    # loop thru the list and calculate changes to horizontal position and depth
    while row < noOfRows:
        # find next instruction in the dataset
        instruction, movement = find_instr(theData[row])
        
        # move the submarine accordingly, from current position, 
        # and find the new position; i.e. the horizontal_pos, depth and aim of sub.
        horizontal_pos, depth, aim = move_sub(instruction, movement, horizontal_pos, depth, aim)
        
        # move to next row in dataset
        row += 1
    
    #calculate final value based on horizontal_pos and depth
    valueX = horizontal_pos * depth
    return valueX

def get_the_data():
    #read the test puzzle input 
    #theData = open('day22021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day22021_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 1856459736
    valueX = process_the_data(theData) 
    
    print('multiply your final horizontal position by your final depth -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()