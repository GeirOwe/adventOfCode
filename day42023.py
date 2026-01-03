# Day4 2023 for Advent of Code
# source: https://adventofcode.com/

import os
import numpy as np

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 4 part 1 .... >')
    print()
    return

def process_card(row):
    xx = row.split('|')
    #my numbers
    my_numbers = sorted(xx[1].split())
    #winning numbers
    xx2 = xx[0].split(':')
    winning_numbers = sorted(xx2[1].split())
    return winning_numbers, my_numbers

#start function
def process_data(theData):
    valueX = 0
    point = 0
    for row in theData:
        winning_numbers, my_numbers = process_card(row)
        # returns common elements in the two lists
        common_elements = list(set(winning_numbers).intersection(my_numbers))
        #1 for the first match, 
        if len(common_elements) <= 1:
            point = (len(common_elements) * 1)
        else:
            #1 for the first match, then doubled three times for each of the three matches after the first
            j = 1
            point = 1
            while j < (len(common_elements)):
                point = point * 2
                j += 1
        #print(point)
        valueX += point

    return valueX
#end function

def get_the_data():
    #read the test puzzle input 
    #theData = open('day42023_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day42023_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        element = element.strip()
        data_list.append(element)
    return data_list

#start function
def start_the_challenge():
    #get the data and read the into  list
    theData = get_the_data()

    #process the codes and return the answer
    valueX = process_data(theData) 
    
    print('How many points are they worth in total? -> ', valueX, '\n')

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()