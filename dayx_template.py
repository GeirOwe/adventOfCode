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
    #read the test puzzle input 
    intcodes_f = open('dayx_test_puzzle_input.txt', 'r')
    #the codes are separated by comma - transfer them to a list
    theData = intcodes_f.read().split(',')
    return theData

#start function
def start_the_challenge():
    #get the data and read the into  list
    theData = get_the_data()

    #process the codes and return the answer
    valueX = process_codes(theData) 
    
    print('forventet resultat er ...  6730673 ...') 
    print('What value is left at position 0 after the program halts? - ', valueX)

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()