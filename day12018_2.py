# Day1 - 2018 Advent of code
# source: https://adventofcode.com/2018

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2018 Day 1, part 2 .... >')
    print()
    return

def check_freq(frequency_change_list, freq, prev_freq_list, theOne):
    for change in frequency_change_list:
        freq += int(change)
        if freq in prev_freq_list:
            theOne = freq
            break
        else:
            prev_freq_list.append(freq)
    return freq, prev_freq_list, theOne

def process_the_data(theData):
    #set initial position for the dataset
    signal = 0
    theOne = -99
    signal_list = []
    # loop thru the list and calculate frequency change in the signal
    while theOne == -99: 
        signal, signal_list, theOne = check_freq(theData, signal, signal_list, theOne)
       
    return theOne

def get_the_data():
    #read the test puzzle input 
    theFile = open('day12018_2_test_puzzle_input.txt', 'r')
    #theFile = open('day12018_puzzle_input.txt', 'r')
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
    
    print('What is the first frequency your device reaches twice?  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()