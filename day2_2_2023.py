# Template for Advent of Code
# source: https://adventofcode.com/

import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 2 part 2 .... >')
    print()
    return

def process_row(row):
    #the play
    the_colors = {
        'blue': 0,
        'red': 0,
        'green' : 0
    }
    #collect max
    maxBlue = 0
    maxRed = 0
    maxGreen = 0
    #process row
    game, allSets = row.split(':')
    sets = allSets.split(';')

    #procss all sets
    for cubes in sets:
        colors = cubes.split(',')
        for play in colors:
            play = play.strip()
            numb, color = play.split()
            #update the dict for this color
            the_colors[color] += int(numb) 

        if the_colors['blue'] > maxBlue: maxBlue = the_colors['blue']
        if the_colors['red'] > maxRed: maxRed = the_colors['red']
        if the_colors['green'] > maxGreen: maxGreen = the_colors['green']
        
    # The power of a set of cubes is equal to the numbers of 
    # red, green, and blue cubes multiplied together
    power = maxBlue * maxRed * maxGreen
    return power

#start function
def process_codes(theData):
    power = 0
    sumTotal = 0
    #process all rows
    for row in theData:
        power = process_row(row)
        sumTotal += power
    
    return sumTotal
#end function

def get_the_data():
    #read the puzzle input like this if a list without separation chars
    #theData = open('day22023_test_puzzle_input.txt', 'r')
    theData = open('day22023_puzzle_input.txt', 'r')
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
    
    print('\nWhat is the sum of the power of these sets?', valueX, '\n')

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()