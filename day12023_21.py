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

    #create a pattern to match the numbers dict with the chars in the row
    #   re.compile('|'.join(map(re.escape, numbers.keys()))): This line creates a regular expression 
    #   pattern by joining the keys from the numbers dictionary using the | (pipe) as a separator. 
    #   re.escape is used to escape any special characters in the keys.
    pattern = re.compile('|'.join(map(re.escape, numbers.keys())))
    #   lambda match: numbers[match.group(0)]: This is a lambda function (replace_function) that takes a 
    #   match object and returns the corresponding value from the numbers dictionary for the matched key.
    replace_function = lambda match: numbers[match.group(0)]
    #move the replaces pattern to a new row
    newrow = pattern.sub(replace_function, row)

    return newrow

def find_numbers2(row):
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

def find_numbers(row):
    # Use regular expression to find all digits in the string
    row = fix_row(row)
    digits = re.findall(r'\d', row)
    
    if digits:
        # Return the first and last digits
        sumChar = digits[0] + digits[-1]
    print(row, ' -> ', sumChar)
    return int(sumChar)

#start function
def process_codes(theData):
    sumRow = 0
    sum_list = []
    #loop thru all rows and find the two numbers and summarize
    for row in theData:
        sumRow = find_numbers(row)
        sum_list.append(sumRow)
    
    return sum(sum_list)
#end function

def get_the_data():
    #read the puzzle input like this if a list without separation chars
    #theData = open('day12023_2_test_puzzle_input.txt', 'r')
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