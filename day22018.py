# Day1 - 2018 Advent of code
# source: https://adventofcode.com/2018

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2018 Day 2, part 1 .... >')
    print()
    return

def check_occurences(a):
    k = {}
    for j in a:
        if j in k:
            k[j] +=1
        else:
            k[j] =1
    return k

def process_the_data(theData):
    checksum = 42
    totalTwo = 0
    totalThree = 0
    #loop thru data and look for 
    #exactly two or three of any letter 
    for id in theData:
        count_dict = check_occurences(id)
        #the dict contains each char(k) and the number of occurences(v) of that char
        noOfTwo = sum(value == 2 for value in count_dict.values())
        noOfThree = sum(value == 3 for value in count_dict.values())
        # one id can only be counted once
        if noOfTwo > 0: totalTwo += 1
        if noOfThree > 0: totalThree += 1
    
    checksum = totalTwo * totalThree
    return checksum

def get_the_data():
    #read the test puzzle input 
    #theFile = open('day22018_test_puzzle_input.txt', 'r')
    theFile = open('day22018_puzzle_input.txt', 'r')

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