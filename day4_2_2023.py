# Day4 2023 for Advent of Code
# source: https://adventofcode.com/

import os
import numpy as np

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 4 part 2 .... >')
    print()
    return

def process_card(row):
    xx = row.split('|')
    #my numbers
    my_numbers = sorted(xx[1].split())
    #winning numbers
    xx2 = xx[0].split(':')
    winning_numbers = sorted(xx2[1].split())
    return winning_numbers, my_numbers

#start function
def process_data(theData):
    card = 1
    total_cards = []
    for row in theData:
        winning_numbers, my_numbers = process_card(row)
        # returns common elements in the two lists
        common_elements = list(set(winning_numbers).intersection(my_numbers))
        #you win copies of the scratchcards below the winning card equal to the number of matches

        # how many in total
        total_cards.append(card)
        k = 0
        while k < total_cards.count(card):
            j = 0
            while j < len(common_elements):
                j += 1
                total_cards.append(card+j)    #Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
            k += 1
        #next row / card
        card += 1
        total_cards = sorted(total_cards)

    return len(total_cards)
#end function

def get_the_data():
    #read the test puzzle input 
    #theData = open('day42023_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day42023_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        element = element.strip()
        data_list.append(element)
    return data_list

#start function
def start_the_challenge():
    #get the data and read the into  list
    theData = get_the_data()

    #process the codes and return the answer
    valueX = process_data(theData) 
    
    print('how many total scratchcards do you end up with -> ', valueX, '\n')

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()