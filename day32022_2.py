# Day3 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/3
import os
import itertools as it

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 3, part 2 .... >')
    print()

def checkforBadge(theList):
    list1 = theList[0]
    list2 = theList[1]
    list3 = theList[2]

    #check for common chars
    badge = list(set(list1).intersection(list2))
    badge = list(set(badge).intersection(list3))
    return badge

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
    lastRow = noOfRows
    row = 0
    allBadges = []
    theList = []
    y=0
    
    # loop thru the file 
    while row <= noOfRows:
        if y < 3:
            # .. and collect next 3 rows into a list
            theList.append(theData[row])
            y += 1
        else:
        # check for common letters in those 3 rows
            badge = checkforBadge(theList)
            # add the badges to a list
            allBadges.append(badge[0])
            #reset help variables, to be used for the next 3 rows
            y = 0
            theList = []
            if row != lastRow: row -= 1
  
        # move to next row in dataset
        row += 1

    # calculate the value of all badges
    valueX = calc(allBadges)
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
    
    print('What is the sum of the priorities of all badges -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()