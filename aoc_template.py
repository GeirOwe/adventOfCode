# Dayx - 2024 Advent of code
# source: https://adventofcode.com/2024

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day X, part 1 .... >')
    print()
    return

def process_the_data(theData):
    #set initial position for the dataset
    totalScore = 42
    
    # loop thru the list
    for theRow in theData:
        split = theRow.split(' ')
        first = split[0].strip()
        second = split[1].strip()

    return totalScore

def get_the_data():
    #read the test puzzle input 
    theData = open('aoc_template_test_puzzle_input.txt', 'r')
    
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
    
    print('What would your total score be  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()