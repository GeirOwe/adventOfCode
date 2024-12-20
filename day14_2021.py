# Day14 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/14

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 14, part 1 .... >')
    print()
    return


# Program to find most & min frequent
# element in a list
def most_frequent(List):
    most = max(set(List), key = List.count)
    return most

def least_frequent(List):
    mini = min(set(List), key = List.count)
    return mini

def extend_polymer(pair_list, polymer):
    i = 0
    newPolymer = ""
    while i < (len(polymer)-1):
        currStr = polymer[i:i+2]
        stillSearching = True
        for row in pair_list:
            if stillSearching:
                if row[0] == currStr:
                    #insert the char in the list into the polymer
                    #except for first char; do not repeat first char into new polymer
                    if i == 0: newPolymer = newPolymer + ( currStr[:1] + row[1] + currStr[1:])
                    else: newPolymer = newPolymer + (row[1] + currStr[1:])
                    stillSearching = False
        i += 1
    return newPolymer

def process_the_data(pair_list, polymer):
    i = 0
    charMost = ""
    #extend the polymer 40 times
    while i < 40:
        polymer = extend_polymer(pair_list, polymer)
        i +=1
    #find the most used & least char
    print("length of polymer after 10x ->", len(polymer))
    charMost = most_frequent(polymer)
    print("most frequent: ", charMost)
    charMin = least_frequent(polymer)
    print("least frequent: ", charMin)    
    #taking the quantity of the most common element and subtracting 
    # the quantity of the least common element
    maxCount = polymer.count(charMost)
    minCount = polymer.count(charMin)
    valueX = maxCount - minCount
    return valueX

def refine_list(theData):   
    numOfRows = len(theData)
    pair_list = []
    for row in theData:
        splitR = row.split(" -> ")
        pair_list.append(splitR)
    return pair_list

def get_the_data():
    #read the test puzzle input 
    #theData = open('day14_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day14_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    pair_list = []
    row = 0
    for element in theData:
        elementTrimmed = element.strip()
        if row == 0: polymer = elementTrimmed
        elif row == 1: print()
        else: pair_list.append(elementTrimmed)
        row += 1
    return pair_list, polymer

def start_the_engine():
    #get the data and read them into a list
    pair_list, polymer = get_the_data()
    pair_list = refine_list(pair_list)
    
    #process the data and return the answer
    valueX = process_the_data(pair_list, polymer)
    
    # What do you get if you take the quantity of the most common element and 
    # subtract the quantity of the least common element?.
    
    print('\nmost common element - least common element -> ', valueX,'\n')
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()