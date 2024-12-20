# Template for Advent of Code
# source: https://adventofcode.com/

import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 1 part 1 .... >')
    print()

def find_numbers(row):
    sumRow = 0
    fistDigitFound = False
    lastDigitFound = False
    #find first number and last number
    #if just one number, then last number equals first number
    for charX in row:
        if charX.isdigit():
            if fistDigitFound == False:
                firstNum = charX
                fistDigitFound = True
            else:
                lastNum = charX
                lastDigitFound = True
    
    if lastDigitFound == False:
        lastNum = firstNum

    sumChar = firstNum + lastNum
    sumRow = int(sumChar)
    return sumRow

#start function
def process_codes(theData):
    sumTotal = 0
    sumRow = 0
    #loop thru all rows and find the two numbers and summarize
    for row in theData:
        sumRow = find_numbers(row)
        sumTotal += sumRow
    return sumTotal
#end function

def get_the_data():
    #read the test puzzle input like this if separated by comma
    #intcodes_f = open('dayx_test_puzzle_input.txt', 'r')
    #the codes are separated by comma - transfer them to a list
    #theData = intcodes_f.read().split(',')

    #read the puzzle input like this if a list without separation chars
    #theData = open('day12023_test_puzzle_input.txt', 'r')
    theData = open('day12023_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)

    return data_list

#start function
def start_the_challenge():
    #get the data and read the into  list
    theData = get_the_data()

    #process the codes and return the answer
    valueX = process_codes(theData) 
    
    print('\nWhat is the sum of all of the calibration values? ->', valueX, '\n')

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()