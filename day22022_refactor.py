# Day2 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/2

import os

ROCK = "Rock"
PAPER = "Paper"
SCISSOR = "Scissor"
LOOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 2, part 2 .... >')
    print()

def calc_score(elfPlay, theStrategy):
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    roundScore = 0
    
    #how you play is based on the strategy
    if theStrategy == LOOSE:
        if elfPlay == ROCK: myPlay = SCISSOR
        if elfPlay == SCISSOR: myPlay = PAPER
        if elfPlay == PAPER: myPlay = ROCK
    else:
        if theStrategy == DRAW: 
            myPlay = elfPlay
        else:
            if theStrategy == WIN:
                if elfPlay == ROCK: myPlay = PAPER
                if elfPlay == SCISSOR: myPlay = ROCK
                if elfPlay == PAPER: myPlay = SCISSOR
    
    #score for choice
    if myPlay == ROCK: roundScore += 1
    if myPlay == PAPER: roundScore += 2
    if myPlay == SCISSOR: roundScore += 3

    #score for play
    if (myPlay == ROCK and elfPlay == SCISSOR) or (myPlay == SCISSOR and elfPlay == PAPER) or (myPlay == PAPER and elfPlay == ROCK):
        #you win
        roundScore += 6
    elif (myPlay == ROCK and elfPlay == ROCK) or (myPlay == SCISSOR and elfPlay == SCISSOR) or (myPlay == PAPER and elfPlay == PAPER):
        #draw
        roundScore += 3

    return roundScore

def process_the_data(theData):
    #set initial position for the dataset
    noOfRows = len(theData)
    row = 0
    totalScore = 0
    
    # loop thru the list and calculate no of cals for the Elf. Empty means no more cals for this Elf.
    while row < noOfRows:
        #split input at ' ' the left part[0] contains the elfPlay, the right[1] contain my strategy
        split = theData[row].split(' ')
        elfPlay = split[0].strip()
        myStrategy = split[1].strip()
        
        # A for Rock, B for Paper, and C for Scissors.
        if elfPlay == 'A': elfPlay = ROCK
        if elfPlay == 'B': elfPlay = PAPER
        if elfPlay == 'C': elfPlay = SCISSOR

        roundScore = calc_score(elfPlay, myStrategy)
        totalScore += roundScore
        
        # move to next row in dataset
        row += 1

    return totalScore

def get_the_data():
    #read the test puzzle input 
    #theData = open('day22022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day22022_puzzle_input.txt', 'r')

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
    
    print('what would your total score be according to your strategy guide  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()