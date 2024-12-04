# Day3 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/3

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 3, part 1 .... >')
    print()

def process_the_data(theData):
    #set initial position for the dataset
    #noOfColumns = 5
    noOfColumns = 12
    currColumn = 0
    valueX = 0
    # Your horizontal position and depth both start at 0. so does aim.
    gamma_rate = []
    epsilon_rate = []
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
            gamma_rate.append("0")
            epsilon_rate.append("1")
        else:
            gamma_rate.append("1")
            epsilon_rate.append("0")
        
        #reduce data set to only include rows with most common bit in current column
        # if only one row left -> done. keep that row as the oxy_gen_rate
        currColumn += 1
   
    currColumn = 0
    gamma_str = ""
    epsilon_str = ""
    while currColumn < noOfColumns:
        gamma_str = gamma_str + gamma_rate[currColumn]
        epsilon_str = epsilon_str + epsilon_rate[currColumn]
        currColumn += 1
    
    gamma_int = int(gamma_str, 2)
    epsilon_int = int(epsilon_str, 2)
       

    #calculate final value based on horizontal_pos and depth
    valueX = gamma_int * epsilon_int
    return valueX

def get_the_data():
    #read the test puzzle input 
    #theData = open('day32021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day32021_puzzle_input.txt', 'r')

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
    
    print('What is the power consumption of the submarine -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()