# Day8 - 2023 Advent of code

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 9, part 2 .... >')
    print()
    return

def process_the_row(row_list):
    next_row = []
    all_zeroes = False
    #process all numbers in the row list
    i = 1
    while i < len(row_list):
        #start at second item in the list
        diff = (row_list[i]) - (row_list[i-1])
        next_row.append(diff)

        #next number
        i += 1
    
    #check if all zeroes
    x=[i for i in next_row if i==0]
    if len(x) == len(next_row): 
        #print(next_row)
        all_zeroes = True 

    #if not all zeroes repeat
    if all_zeroes != True:
        #recursion until zeroes
        next_row = process_the_row(next_row)
        row_list.insert(0, (row_list[0] - next_row[0]))
        #print(row_list)
    else:
        #append to the row and repeat back thru all recursion
        #insert in the eginning of the list
        row_list.insert(0, (row_list[0] - next_row[0]))
        #print(row_list)

    return row_list

def process_the_data(theData):
    #set initial position for the dataset
    sumX = 0
    num_list = []
    for row in theData:
        row_list = row.split()
        #convert to int
        for num in row_list: 
            num_list.append(int(num))
        #process row
        num_list = process_the_row(num_list)
        sumX += num_list[0]
        #empty num list before next row
        num_list = []
        #print()

    return sumX

def get_the_data():
    #read the test puzzle input 
    #theData = open('day92023_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day92023_puzzle_input.txt', 'r')
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
    
    print('What is the sum of these extrapolated values? -> ', valueX,'\n') 
    return

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()