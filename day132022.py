# Day13 - 2022 Advent of code
# source: https://github.com/am93/aoc2022/blob/main/day13.py

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 13, part 1 .... >')
    print()
    return

#thru recursion
def check_signal(pack1, pack2):
    if isinstance(pack1, int) and isinstance(pack2, int):
        #both elements are integers
        if pack1 < pack2:
            return -1
        elif pack1 == pack2:
            return 0
        else:
            return 1
    elif isinstance(pack1, list) and isinstance(pack2, list):
        #both elements are list -> recursion of the list
        idx = 0
        while idx < len(pack1) and idx < len(pack2):
            res = check_signal(pack1[idx], pack2[idx])
            if res != 0:
                return res
            idx += 1
        return len(pack1) - len(pack2)
    elif isinstance(pack1, int) and isinstance(pack2, list):
        #mixed elements -> one integer and one list
        return check_signal([pack1], pack2)
    else:
        return check_signal(pack1, [pack2])

#Packet data consists of lists and integers. Each list starts with [, ends with ], 
# and contains zero or more comma-separated values (either integers or other lists). 
# Each packet is always a list and appears on its own line.
def process_the_data(theData):
    valueX = 0

    pair = []
    # What are the indices of the pairs that are already in the right order? 
    # (The first pair has index 1, the second pair has index 2, and so on.) 
    # In the above example,     # the pairs in the right order are 1, 2, 4, and 6; 
    # the sum of these indices is 13.
    ind_list = []
    pair_no = 0
    for row in theData:
        # read the pair
        if row != '':
            # move from trings to thru list
            pair.append(eval(row))
        else:
            # check the pair
            pair_no += 1
            #right_order = process_pair(pair, done)
            if check_signal(pair[-2], pair[-1]) < 0:
                ind_list.append(pair_no)
            #prepare for next pair
            pair = []
    
    #sum of indices in right order
    valueX = sum(ind_list)
    return valueX

def get_the_data():
    #read the test puzzle input 
    theData = open('day132022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day132022_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        element = element.strip()
        data_list.append(element)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return a list of monkey objects from the input file
    valueX = process_the_data(theData)

    print('What is the sum of the indices of those pairs -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()

