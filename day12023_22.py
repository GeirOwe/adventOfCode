# Template for Advent of Code
# source: https://adventofcode.com/

import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 1 part 2 .... >')
    print()
    return

#start function
def process_codes(theData):
    total = 0
    #loop thru all rows
    for line in theData:
        digits = []
        for i in range(len(line)):
            #if char is a digit, append it
            if line[i].isdigit():
                digits.append(int(line[i]))
            else:
                # if char is not a digit, check if there is a number written from that position
                # and onwards -> [i:1]
                # enumerate contains a number (j), starting from zero, connected to each item (w)
                # hence j+1 in the append. w refers to the text in enumerate
                # do not replace as first tried -> e.g. 'eightwothree' contains [8, 2, 3] and not '8wo3'
                for j, w in enumerate("one two three four five six seven eight nine".split()):
                    remain_string = line[i:]
                    if remain_string.startswith(w):
                        digits.append(j+1)
        
        total += int(str(digits[0])+str(digits[-1]))

    return total
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