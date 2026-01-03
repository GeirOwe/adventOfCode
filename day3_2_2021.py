# Day3 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/3

import os
import pandas as pd

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 3, part 2 .... >')
    print()

def reduce_dataset(theData, theSignal, currPos):
    reduced_dataset = []
    for row in theData:
        if int(row[currPos]) == theSignal:
            #reduce data set to only keep rows with zeroes in current column
            reduced_dataset.append(row)
    return reduced_dataset

def process_co2(theData):
    #set initial position for the dataset
    noOfColumns = 5
    #noOfColumns = 12
    currColumn = 0
    # loop thru the list and calculate changes to horizontal position and depth
    while currColumn < noOfColumns:
        zeroes = 0
        ones = 0
        #count 0 and 1 in current row
        for row in theData:
            if int(row[currColumn]) == 0:
                zeroes += 1
            else:
                ones += 1
        
        #find least common bit
        if zeroes <= ones:
            #reduce data set to only keep rows with zeroes in current column
            theData = reduce_dataset(theData, 0, currColumn)
        else:
            #reduce data set to only keep rows with ones in current column
            theData = reduce_dataset(theData, 1, currColumn)
        
         # if only one row left -> done. keep that row as the oxy_gen_rate
        if len(theData) == 1:
            currColumn = noOfColumns
        else:
            currColumn += 1
   
    co2_rating = int(row.strip(), 2)
    return co2_rating

def process_oxy(theData):
    #set initial position for the dataset
    noOfColumns = 5
    #noOfColumns = 12
    currColumn = 0
    # loop thru the list and calculate changes to horizontal position and depth
    while currColumn < noOfColumns:
        zeroes = 0
        ones = 0
        #count 0 and 1 in current row
        for row in theData:
            if int(row[currColumn]) == 0:
                zeroes += 1
            else:
                ones += 1
        
        #find most common bit
        if zeroes > ones:
            #reduce data set to only keep rows with zeroes in current column
            theData = reduce_dataset(theData, 0, currColumn)
        else:
            #reduce data set to only keep rows with ones in current column
            theData = reduce_dataset(theData, 1, currColumn)
        
         # if only one row left -> done. keep that row as the oxy_gen_rate
        if len(theData) == 1:
            currColumn = noOfColumns
        else:
            currColumn += 1
   
    oxy_gen_rate = int(row.strip(), 2)
    return oxy_gen_rate

def process_the_data(theData):
    oxy_gen_rate = process_oxy(theData)
    co2_rating = process_co2(theData)
     
    #calculate final value 
    valueX = oxy_gen_rate * co2_rating
    return valueX

def get_the_data():
    #read the test puzzle input 
    theData = open('day32021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day32021_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer 
    valueX = process_the_data(theData) 
    
    print('What is the power consumption of the submarine -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()