# Day15 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/15

import os
import heapq
import sys

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 15, part 1 .... >')
    print()
    return

#find best route and calculate risk
def calc_risk(grid):
    ##on loan from: https://github.com/Bruception/advent-of-code-2021/blob/main/day15/part1.py
    rows, cols = len(grid), len(grid[0])

    deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    #risk in lower right corner of i, j contains the risk -> sum least effort route
    risk = {(i, j): sys.maxsize for i in range(rows) for j in range(cols)}
    #create a Heap queue
    queue = [(0, (0, 0))]

    while (queue):
        #This function is used to remove and return the smallest element from heap. 
        #The order is adjusted, so as heap structure is maintained.
        current_risk, position = heapq.heappop(queue)
        
        for di, dj in deltas:
            ni, nj = di + position[0], dj + position[1]
            neighbor_position = (ni, nj)
            if (neighbor_position in risk):
                new_risk = current_risk + grid[ni][nj]
                if (new_risk < risk[neighbor_position]):
                    risk[neighbor_position] = new_risk
                    # This function is used to insert the element mentioned in its arguments into heap. 
                    # The order is adjusted, so as heap structure is maintained.
                    heapq.heappush(queue, (new_risk, neighbor_position))

    valueX = risk[(rows - 1, cols - 1)]
    return valueX

def process_the_data(the_data):
    valueX = calc_risk(the_data)
    return valueX

def get_the_data():
    #read the test puzzle input 
    #theData = [list(map(int, row)) for row in open(f'{sys.path[0]}/day15_test_puzzle_input.txt', 'r').read().split('\n')]
    #read the puzzle input 
    theData = [list(map(int, row)) for row in open(f'{sys.path[0]}/day15_puzzle_input.txt', 'r').read().split('\n')]
    
    return theData

def start_the_engine():
    #get the data and read them into a list
    the_data = get_the_data()

    #process the data and return the answer
    valueX = process_the_data(the_data)
    
    print('\nthe lowest total risk of any path -> ', valueX,'\n')
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()