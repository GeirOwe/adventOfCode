# Day8 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/8
import os


def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 8, part 1 .... >')
    print()
    return

def process_the_data(theData):
    
    #find answer
    answer = -1
    
    return answer

def get_the_data():
    #read the test puzzle input 
    theData = open('day82022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day82022_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        data_list.append(element)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: ...
    valueX = process_the_data(theData) 
    
    print('what crate ends up on top of each stack -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()

