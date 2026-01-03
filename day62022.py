# Day6 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/6
import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 6, part 1 .... >')
    print()
    return

#marker is found if no doucle chars in list
def check_for_marker(fourChar):
    noMarker = True
    occurrences = {}
    # Checking the element from list present as key in dictionary
    # if yes than increment by 1 or create new key with value 1
    for i in fourChar:
        if i in occurrences:
            occurrences[i] += 1
            noMarker = False
        else:
            occurrences[i] = 1

    return noMarker

# add the new char to the end and remove first; so still 4 chars
def update_Chars(char, fourChar):
    fourChar.pop(0)
    fourChar.append(char)

    return fourChar

def process_the_data(theData):
    #set initial position for the dataset
    fourChar = []
    buffer = theData[0]
    pos = 0
    valueX = 1000
    for char in buffer:
        if pos < 4:
            #find first 4 chars
            fourChar.append(char)
        else:
            #check if we have a marker
            marker = check_for_marker(fourChar)
            if marker:
                valueX = pos
                break
            else:
                #add the new char to the list of 4 chars
                fourChar = update_Chars(char, fourChar)
        pos +=1

    return valueX

def get_the_data():
    #read the test puzzle input 
    #theData = open('day62022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day62022_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer
    valueX = process_the_data(theData) 
    
    print('How many characters need to be processed -> ', valueX,'\n')
    return

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()