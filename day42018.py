# Day4 - 2018 Advent of code
# source: https://adventofcode.com/2018

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2018 Day 4, part 1 .... >')
    print()
    return

def process_the_data(theData):
    checksum = 42

    return checksum

def get_the_data():
    #read the test puzzle input 
    theFile = open('day42018_test_puzzle_input.txt', 'r')
    #theFile = open('day42018_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theFile:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)

    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('How many square inches of fabric are within two or more claims?  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()
