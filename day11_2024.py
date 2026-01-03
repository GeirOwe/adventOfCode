# 2024 Advent of code
# source: https://adventofcode.com/2024

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 11, part 1 .... >')
    print()
    return  

#checking the rules
def transform_stone(stone):
    #If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        # If the stone is engraved with a number that has an even number of digits, it is replaced by two 
        # stones. The left half of the digits are engraved on the new left stone, and the right half of 
        # the digits are engraved on the new right stone.
        mid = len(str(stone)) // 2
        left = int(str(stone)[:mid])
        right = int(str(stone)[mid:])
        return [left, right]
    else:
        #If none of the other rules apply, the stone is replaced by a new stone; the old stone's 
        # number multiplied by 2024
        return [stone * 2024]

#run the rules for every blink and add the resulting stones to a new list
def blink(stones, times):
    for _ in range(times):
        new_stones = []
        for stone in stones:
            new_stones.extend(transform_stone(stone))
        stones = new_stones
    return stones

def process_the_data(theData):
    initial_stones = []
    # convert input to a list of ints
    initial_list = theData[0].split()
    for item in initial_list:
        initial_stones.append(int(item)) 

    blinks = 75  # You can change this to any number of blinks

    result = blink(initial_stones, blinks)
    #print(f"After {blinks} blink(s), the stones are: {result}")

    return len(result)

def get_the_data():
    #read the test puzzle input 
    #theData = open('day11_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day11_2024_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('ow many stones will you have after blinking 25 times? -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()