# Day4 - 2024 Advent of code
# source: https://adventofcode.com/2024

from operator import truediv
import os
from collections import Counter

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 4, part 2 .... >')
    print()
    return

def process_the_data(theData):
    noOfReports = 42
   
    return noOfReports

def get_the_data():
    #read the test puzzle input 
    theData = open('day4_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day4_2024_puzzle_input.txt', 'r')
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
    
    print('How many times does XMAS appear? -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()