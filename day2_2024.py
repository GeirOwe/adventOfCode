# Dayx - 2024 Advent of code
# source: https://adventofcode.com/2024

from operator import truediv
import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 2, part 1 .... >')
    print()
    return

def allIncDec(lst):
    safe = False
    # Check if the list is increasing
    is_increasing = all(int(lst[i]) < int(lst[i+1]) for i in range(len(lst) - 1))
    # Check if the list is decreasing
    is_decreasing = all(int(lst[i]) > int(lst[i+1]) for i in range(len(lst) - 1))
    
    # Return True if the list is either increasing or decreasing
    if is_increasing or is_decreasing: safe = True

    return safe

def adjacentOk(row):
    safe = True
    i = 0
    while i < (len(row) -1):
        # Any two adjacent levels differ by at least one and at most three.
        diff = abs(int(row[i]) - int(row[i+1]))
        if (diff == 0) or (diff > 3): safe = False
        i += 1

    return safe

def process_the_data(theData):
    noOfReports = 0
    #check if the report is safe
    for row in theData:
        row_list = row.split(' ')
        safe1 = allIncDec(row_list)
        safe2 = adjacentOk(row_list)

        #it both conditions are true, the report is safe    
        if safe1 and safe2: noOfReports += 1
    return noOfReports

def get_the_data():
    #read the test puzzle input 
    #theData = open('day2_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day2_2024_puzzle_input.txt', 'r')
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
    
    print('How many reports are safe -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()