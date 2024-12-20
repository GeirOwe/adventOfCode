# Day3 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/3
import os
import itertools as it

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 3, part 1 .... >')
    print()

def check_common(theList):
    #divide list in two
    moreChars = []
    length = len(theList)
    middle = length//2
    #split the list in half
    list1 = theList[:middle]
    list2 = theList[middle:]

    #check for common chars
    moreChars = list(set(list1).intersection(list2))
    return moreChars

def calc(commonChars):
    sum = 0
    score = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x','y', 'z', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X','Y', 'Z']
    for char in commonChars:
        pos = score.index(char)
        #pos starts in zero so, add 1
        pos += 1
        sum += pos
    return sum

def process_the_data(theData):
    #initial the variables
    noOfRows = len(theData)
    row = 0
    commonChars = []
    
    # loop thru the file and calculate no of cals for each Elf. 
    # Empty row means no more cals for this Elf.
    while row < noOfRows:
        # split the row in half and check for common chars
        moreChars = check_common(theData[row])
        commonChars.extend(moreChars)
  
        # move to next row in dataset
        row += 1
    # calculate the value of the common chars
    valueX = calc(commonChars)
    return valueX

def get_the_data():
    #read the test puzzle input 
    #theData = open('day32022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day32022_puzzle_input.txt', 'r')
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
    
    print('What is the sum of the priorities of those item types -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()