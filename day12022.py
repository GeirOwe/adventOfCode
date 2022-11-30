# Day1 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/1

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 1, part 1 .... >')
    print()

def process_the_data(theData):
    #set initial position 
    valueX = len(theData)
    
    return valueX

def get_the_data():
    #read the test puzzle input 
    theData = open('day12022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day12022_puzzle_input.txt', 'r')

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
    
    print('the answer -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()