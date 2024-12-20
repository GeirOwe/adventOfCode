# Dayx - 2023 Advent of code
# source: https://adventofcode.com/2023

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 1, part 1 .... >')
    print()
    return

def process_the_data(points):
    #set initial position for the dataset
    totalScore = 42
    
    fib_seq_list = []
    #generate fibonacci sequence
    fib = lambda n: n if n<= 1 else fib(n-1) + fib(n-2)
    fib_seq = (fib(i) for i in range(points))
    for x in fib_seq: 
        fib_seq_list.append(x)
    #return fib_seq_list

    return totalScore

def get_the_data():
    #read the test puzzle input 
    theData = 11
    
    return theData

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