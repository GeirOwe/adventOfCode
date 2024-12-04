# Template for Advent of Code
# source: https://adventofcode.com/

import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 2 part 1 .... >')
    print()
    return

#start function
def process_codes(theData):
    total = 42

    return total
#end function

def get_the_data():
    #read the puzzle input like this if a list without separation chars
    theData = open('day22023_test_puzzle_input.txt', 'r')
    #theData = open('day22023_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)

    return data_list

#start function
def start_the_challenge():
    #get the data and read the into  list
    theData = get_the_data()

    #process the codes and return the answer
    valueX = process_codes(theData) 
    
    print('\nWhat is the sum of ....... ? ->', valueX, '\n')

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()