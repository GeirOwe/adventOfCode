# 2023 for Advent of Code
# source: https://adventofcode.com/
import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 15 part 1 .... >')
    print()
    return

def hash_it(row):
    result = 0
    for char in row:
        # The current value starts at 0.
        # The first character ->; its ASCII code value
        # The current value increases with asci code value
        # The current value is multiplied by 17 .
        # The current value becomes the remainder of calue divided by 256.
        result = result + ord(char)
        result = result * 17
        result = result % 256

    return result

#start function
def process_data(theData):
    result = 0
    sumX = 0
    for row in theData:
        result = hash_it(row)
        sumX += result

    return sumX
#end function

def get_the_data():
    #read the test puzzle input 
    #theData = open('day15_2023_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day15_2023_puzzle_input.txt', 'r')
    #the codes are separated by comma - transfer them to a list
    data_list = theData.read().split(',')

    return data_list

#start function
def start_the_challenge():
    #get the data and read the into  list
    theData = get_the_data()
    #process the codes and return the answer
    valueX = process_data(theData) 
    
    print('What is the sum of the results -> ', valueX, '\n')
    return 

#end function
#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()
