# Day1 - 2018 Advent of code
# source: https://adventofcode.com/2018

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2018 Day 1, part 1 .... >')
    print()
    return

def process_the_data(theData):
    #set initial position for the dataset
    signal = 0
    
    # loop thru the list and calculate frequency change in the signal
    for freq in theData:
        signal = signal + int(freq)
        
    return signal

def get_the_data():
    #read the test puzzle input 
    #theFile = open('day12018_test_puzzle_input.txt', 'r')
    theFile = open('day12018_puzzle_input.txt', 'r')
    #the codes are separated by comma - transfer them to a list
    #theData = theFile.read().split(',')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theFile:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)

    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('what is the resulting frequency  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()