# Template for Advent of Code
# source: https://adventofcode.com/

import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day X .... >')
    print()

#start function
def process_codes(theData):
    #set initial position
    for dataElement in theData:
        cleanedDataElement = int(dataElement.strip()) #remove spaces or EOL
        print(cleanedDataElement)
    
    expectedResult = 6730673
    return expectedResult
#end function

def get_the_data():
    #read the test puzzle input like this if separated by comma
    intcodes_f = open('dayx_test_puzzle_input.txt', 'r')
    #the codes are separated by comma - transfer them to a list
    theData = intcodes_f.read().split(',')

    #read the puzzle input like this if a list without separation chars
    # theData = open('dayx_test_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    #data_list = []
    #for element in theData:
    #    elementTrimmed = element.strip()
    #    data_list.append(elementTrimmed)
    #return data_list

    return theData

#start function
def start_the_challenge():
    #get the data and read th