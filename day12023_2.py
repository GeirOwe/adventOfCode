# Template for Advent of Code
# source: https://adventofcode.com/

import os
import re

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 1 part 2 .... >')
    print()

def fix_row(row):
    #some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, 
    # and nine also count as valid "digits".
    numbers = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    a_string = ''
    pos = 0
    i = 0
    rowlength = len(row)
    newrow = row
    while i < rowlength:
        #if we have a number just skip to next character
        if row[i].isdigit():
            a_string = ''
            #move to next pos
            i += 1
            pos = i
        else:
            a_string += row[i]
        
            #check if the pattern exist in numbers
            res = [val for key, val in numbers.items() if a_string in key]
            #if the pattern is not part of numbers, start over after removing first letter
            if len(res) == 0: 
                    #move back to start and forward oneone back
                    pos += 1
                    i = pos
                    a_string = ''
            else:
                i += 1
                #if there is a match, replave the letters with the number
                if a_string in numbers:
                    newrow = newrow.replace(a_string, numbers[a_string])
                    a_string = ''
                    #move to next pos
                    pos = i
    print(newrow)
    return newrow

def find_numbers(row):
    sumRow = 0
    fistDigitFound = False
    lastDigitFound = False
    #find first number and last number
    #if just one number, then last number equals first number
    #some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, 
    # and nine also count as valid "digits".
    row = fix_row(row)
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
        #print(sumRow)
        sumTotal += sumRow
    return sumTotal
#end function

def get_the_data():
    #read the puzzle input like this if a list without separation chars
    theData = open('day12023_2_test_puzzle_input.txt', 'r')
    #theData = open('day12023_puzzle_input.txt', 'r')
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