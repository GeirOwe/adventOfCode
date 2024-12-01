# Day8 - 2023 Advent of code

import os
from pickle import FALSE

def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 8, part 1 .... >')
    print()
    return


def fetch_node(row, row_dict):
    #separate node and instructions -> AAA = (BBB, CCC)
    node, instruct = row.split('=')
    node = node.strip()
    # move instructions into a list
    row_list = []
    instruct = instruct.strip()
    instruct = instruct.strip('(')
    instruct = instruct.strip(')')
    l, r = instruct.split(',')
    l = l.strip()
    r = r.strip()
    row_list.append(l)
    row_list.append(r)
    # and add to a dict
    row_dict[node] = row_list
    return row_dict

def get_nodes(theData):
    #start from row 3
    j = 2
    row_dict =  {}
    while j < len(theData):
        row = theData[j]
        row_dict = fetch_node(row, row_dict)
        j += 1
    return row_dict

def process_the_data(theData):
    #set initial position for the dataset
    noOfSteps = 0
    instruction = theData[0]
    row_dict = get_nodes(theData)
    # loop thru all instructions and look for 'zzz' node
    noOfInstruct = len(instruction)
    i = 0
    #start with the first key as node
    node = list(row_dict.keys())[0]
    notFound = True
    while i < noOfInstruct and notFound:
        #next step and increase number of steps
        step = instruction[i]
        noOfSteps += 1
        # check instr for this node
        this_i = row_dict[node]
        if step == 'L':
            nextNode = this_i[0]
        else:
            nextNode = this_i[1]

        #found?
        if nextNode == 'ZZZ': 
            notFound = False

        # next instruction
        i += 1
        node = nextNode
        # if at the end of instruction and not found; start over
        if i == noOfInstruct and notFound: i = 0

    return noOfSteps

def get_the_data():
    #read the test puzzle input 
    theData = open('day82023_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day82023_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 1856459736
    valueX = process_the_data(theData) 
    
    print('How many steps are required to reach ZZZ? -> ', valueX,'\n') 
    return

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()