# Day5 - 2018 Advent of code
# source: https://adventofcode.com/2018

import os
from collections import deque

def clear_console():
    os.system('clear')
    print('< .... AoC 2018 Day 5, part 1 .... >')
    print()
    return

def isSimilar(char1, char2):
    answer = False
    #loop thru the list and remove two adjacent units of the same type 
    # and opposite capitalization
    if char1 != char2:
        if char1.upper() == char2:
            # cC
            answer = True
        if char1.lower() == char2:
            #Cc
            answer = True

    return answer

def process_the_data(myList):
    #loop thru the list and remove two adjacent units of the same type 
    # and opposite capitalization
    not_done = True
    while not_done:
        not_done = False
        for i in range(len(myList)-1):
            if isSimilar(myList[i], myList[i+1]):
                #then delete the two elements
                del myList[i:i+2]
                #start over
                not_done = True
                break

    return myList

def get_the_data():
    #read the test puzzle input 
    #theFile = open('day52018_test_puzzle_input.txt', 'r')
    theFile = open('day52018_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theFile:
        elementTrimmed = element.strip()
        for letter in elementTrimmed:
            data_list.append(letter)
    
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('How many units remain after fully reacting the polymer you scanned??  -> ', len(valueX),'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()
