# Template for Advent of Code
# source: https://adventofcode.com/

import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 2 part 1 .... >')
    print()
    return

def process_row(row):
    #the play
    playBlue = 14
    playRed = 12
    playGreen = 13
    noOfCubes = 0
    #collect max
    maxBlue = 0
    maxRed = 0
    maxGreen = 0
    #process row
    game, allSets = row.split(':')
    sets = allSets.split(';')
    x, gameId = game.split()

    #procss all sets
    for cubes in sets:
        #counters
        noBlue = 0
        noRed = 0
        noGreen = 0
        i = 0
        while i < len(cubes):
            if cubes[i].isdigit():
                if cubes[i+1].isdigit():
                    noOfCubes = int(cubes[i] + cubes[i+1])
                    i += 1
                else:
                    noOfCubes = int(cubes[i])

                if cubes[i+2] == 'b': noBlue += noOfCubes
                if cubes[i+2] == 'r': noRed += noOfCubes
                if cubes[i+2] == 'g': noGreen += noOfCubes
            i += 1
            if noBlue > maxBlue: maxBlue = noBlue
            if noRed > maxRed: maxRed = noRed
            if noGreen > maxGreen: maxGreen = noGreen

        if playBlue >= maxBlue and playRed >= maxRed and playGreen >= maxGreen: 
            gamePossible = True
        else:
            gamePossible = False
        
    #after all sets are process, is this game possible
    if gamePossible:
        return int(gameId)
    else:
        return 0

#start function
def process_codes(theData):
    idNo = 0
    sumTotal = 0
    #process all rows
    for row in theData:
        idNo = process_row(row)
        sumTotal += idNo
    
    return sumTotal
#end function

def get_the_data():
    #read the puzzle input like this if a list without separation chars
    theData = open('day22023_test_puzzle_input.txt', 'r')
    #theData = open('day22023_puzzle_input.txt', 'r')
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
    
    print('\nWhat is the sum of the IDs of those games?', valueX, '\n')

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()