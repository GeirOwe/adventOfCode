# Day2 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/2

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 2, part 1 .... >')
    print()

def calc_score(elfPlay, yourPlay):
    # The score for a single round is the score for the shape you selected 
    # (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome 
    # of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    #Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both 
    # players choose the same shape, the round instead ends in a draw.
    roundScore = 1
    return roundScore

def process_the_data(theData):
    #set initial position for the dataset
    noOfRows = len(theData)
    row = 0
    totalScore = 0
    valueX = len(theData)
    
    # loop thru the list and calculate no of cals for the Elf. Empty means no more cals for this Elf.
    while row < noOfRows:
        #split at ' ' - the right part cotnains the jump " 
        # the left part contains the instruction
        split = theData[row].split(' ')
        elfPlay = split[0].strip()
        yourPlay = split[1].strip()

        roundScore = calc_score(elfPlay, yourPlay)
        totalScore += roundScore
        
        # move to next row in dataset
        row += 1

    return valueX

def get_the_data():
    #read the test puzzle input 
    theData = open('day22022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day22022_puzzle_input.txt', 'r')

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
    
    print('What would your total score be  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()