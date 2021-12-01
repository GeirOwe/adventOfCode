# Day1 - 2021 Advent of code
# source: https://adventofcode.com/

import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 1, part 2 .... >')
    print()

#start function
def process_the_data(theData):
    #set initial position
    length = len(theData)
    i = 0
    increased = 0
    # loop thru the list and count the number of times where
    # next sum of three is higher than the current one
    while i < length:
        # check if there are still three more numbers in list; if not we are done
        if i < (length-3):
            # calculate the sum_of_three's
            current_sumOfThree = theData[i] + theData[i+1] + theData[i+2]
            next_sumOfThree = theData[i+1] + theData[i+2] + theData[i+3]
            # check if the next sum of three is higher than the current one
            if next_sumOfThree > current_sumOfThree:
                increased += 1
        i += 1
    return increased
#end function

#start function
def get_the_data():
    #read the test puzzle input 
    #theData = open('day12021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day12021_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        numberTrimmed = int(element.strip())
        data_list.append(numberTrimmed)
    return data_list
#end get_the_data function

#start function
def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer
    valueX = process_the_data(theData) 
    
    print('the number of times the sum of measurements increases -> ', valueX,'\n') 
    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()