# Day4 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/4
import os
def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 4, part 1 .... >')
    print()
def  get_all_numbers(firstE):
    theList = []
    x = firstE.split()
    splitX = x[0].split('-')
    fromX = int(splitX[0])
    toX = int(splitX[1])
    i = fromX
    while i <= toX:
        theList.append(i)
        i += 1
    return theList
def process_the_data(theData):
    #set initial position for the dataset
    noOfRows = len(theData)
    row = 0
    fully = 0
    elf1 = []
    elf2 = []
    # loop thru the list and split the row into the two elf's assignments
    while row < noOfRows:
        # split the input
        part = theData[row].split(',')
        firstE = part[0]
        secondE = part[1]
        #get the complete list based on from .. to
        elf1 = get_all_numbers(firstE)
        elf2 = get_all_numbers(secondE)
        #check if one list is fully part of another
        allin1 = all(elem in elf1 for elem in elf2)
        allin2 = all(elem in elf2 for elem in elf1)
        if allin1 or allin2:
            fully += 1
        
        # move to next row in dataset
        row += 1
    
    return fully
def get_the_data():
    #read the test puzzle input 
    theData = open('day42022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day42022_puzzle_input.txt', 'r')
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
    
    print('In how many assignment pairs does one range fully contain the other -> ', valueX,'\n') 
    return

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()