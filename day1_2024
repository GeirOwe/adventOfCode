# Dayx - 2024 Advent of code
# source: https://adventofcode.com/2024

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day X, part 1 .... >')
    print()
    return

def calc_distance(first_list, second_list):
    totalDiff = 0
    item = 0
    #calculate the difference and add to the total distance
    while item < len(first_list):
        diff = first_list[item] - second_list[item]
        if diff < 0: diff = diff * -1
        
        totalDiff += diff
        item += 1

    return totalDiff

def process_the_data(theData):
    #set initial position for the dataset
    first_list = []
    second_list = []
    # loop thru the input data and split into two lists
    for theRow in theData:
        split = theRow.split('  ')
        first = int(split[0].strip())
        first_list.append(first)
        second = int(split[1].strip())
        second_list.append(second)

    #sort both list with the smallest numbers first
    first_list.sort()
    second_list.sort()
    print('lengden av første liste er: ', len(first_list))
    print('lengden av andre liste er: ', len(second_list))
    #calculate the the total distance between your lists
    totalDistance = calc_distance(first_list, second_list)
    return totalDistance

def get_the_data():
    #read the test puzzle input 
    #theData = open('day1_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day1_2024_puzzle_input.txt', 'r')
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
    
    print('the total distance between your lists  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()