# Day4 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/4
import os
def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 4, part 2 .... >')
    print()
def  get_all_numbers(section):
    theList = []
    #split the data into a from .. and a to to get the range
    x = section.split()
    splitX = x[0].split('-')
    fromX = int(splitX[0])
    toX = int(splitX[1])
    #loop thru the range and add the specific numbers to the list
    i = fromX
    while i <= toX:
        theList.append(i)
        i += 1
    return theList
def process_the_data(theData):
    #set initial position for the dataset
    noOfOverlaps = 0
    elf1 = []
    elf2 = []
    # loop thru the list and split the row into the two elf's assignments
    for row in theData:
        # split the input
        part = row.split(',')
        firstElf = part[0]
        secondElf = part[1]
        #get the complete list based on from .. to
        elf1 = get_all_numbers(firstElf)
        elf2 = get_all_numbers(secondElf)
        #check if one list has any overlap with the other
        overlap = any(elem in elf1 for elem in elf2)
        if overlap:
            noOfOverlaps += 1
    
    return noOfOverlaps
def get_the_data():
    #read the test puzzle input 
    #theData = open('day42022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day42022_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list
def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 4 for the test data
    valueX = process_the_data(theData) 
    
    print('In how many assignment pairs do the ranges overlap -> ', valueX,'\n') 
    return 
#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()
