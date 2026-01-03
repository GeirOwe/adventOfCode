# 2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 7, part 1 .... >')
    print()
    return

def process_the_data(theData):
    pword = 42

    return pword

def get_the_data():
    #read the puzzle input 
    #theData = open('day7_2025_test_puzzle_input.txt', 'r')
    theData = open('day7_2025_puzzle_input.txt', 'r')
    
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
    
    print('The password is  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()