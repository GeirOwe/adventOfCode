# Day1 - 2021 Advent of code
# source: https://adventofcode.com/2022/day/1

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 2, part 1 .... >')
    print()

def process_the_data(theData):
    #set initial position for the dataset
    noOfRows = len(theData)
    noOfCals = 0
    maxCals = 0
    row = 0

    # loop thru the list and calculate no of cals for the Elf. Empty means no more cals for this Elf.
    while row < noOfRows:
        # find next instruction in the dataset
        if theData[row] != "":
            noOfCals = noOfCals + int(theData[row])
        elif maxCals < noOfCals:
            maxCals = noOfCals  #check if this ELF has the most calories
            noOfCals = 0
        else:
            noOfCals = 0

        # move to next row in dataset
        row += 1
    
    return maxCals

def get_the_data():
    #read the test puzzle input 
    #theData = open('day12022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day12022_puzzle_input.txt', 'r')

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
    
    print('How many Calories are being carried by the Elf carrying the most Calories -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()