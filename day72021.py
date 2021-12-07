# Day7 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/7

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 7, part 2 .... >')
    print()
    return

class Crab():
    def __init__(self, position):
        self.position = position
    
    #get the timere
    def get_position(self):
        return self.position
    
    #set position
    def set_position(self, position):
        self.position = position
        return

    #reduce timer
    def step(self, step):
        self.position += step
        return self.timer
#end class definition

def calc_fuelCost(toPos, fromPos):
    i = 1
    fuelCost = 0
    #calculate the cost for the steps in this movement
    #the first step costs 1, the second step costs 2, the third step costs 3, and so on
    while fromPos < toPos:
        fuelCost = fuelCost + i
        i += 1
        fromPos += 1 
    return fuelCost

def check_the_crabs(list_of_crab, minPos, maxPos):
    #list of crab contain crab objects
    #Determine the horizontal position that the crabs can align to using the least fuel possible.
    # valueX -> amount of fuel spent to get to position
    valueX = -1
    lowestFuelCost = 999999999999999999
    fuelCost = 0
    bestPos = 0
    #check the cost for all possible positions where we have crabs
    while minPos < maxPos:
        # calculate fuel cost to move all crabs to minPos
        # save position for lowest fuel cost
        thisFuelCost = 0
        i = 0
        while i < len(list_of_crab):
            crab = list_of_crab[i]
            position = int(crab.get_position())
            #calculate cost for this crab to get to minPos
            if position >= minPos: fuelCost = calc_fuelCost(position, minPos)
            else: fuelCost = calc_fuelCost(minPos, position)
            #add this cost to an accumulate cost for this position for all crabs
            thisFuelCost += fuelCost
            #next crab
            i += 1
        #store the position and cost for cheapest possible outcome
        if thisFuelCost < lowestFuelCost:
            lowestFuelCost = thisFuelCost
            bestPos = minPos
        #next position
        minPos +=1

    return bestPos, lowestFuelCost

def get_the_data():
    #read the test puzzle input 
    #theData = open('day72021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day72021_puzzle_input.txt', 'r')
    
    #move data into a list - read a line and remove lineshift
    minPos = 99
    maxPos = 0
    elements = []
    for element in theData:
        elements.append(element)

    #find minimu and max pos in the dataset
    data_list = elements[0].split(",")
    for number in data_list:
        pos = int(number)
        if pos < minPos: minPos = pos
        if pos > maxPos: maxPos = pos 
    return data_list, minPos, maxPos

def start_the_engine():
    #get the data and read them into a list
    theData, minPos, maxPos = get_the_data()

    print("minPos: ", minPos)
    print("maxPos: ", maxPos)
    print("number of crabs: ", len(theData))
    
    #create a crab first time based on input
    i = 0
    list_of_crab = []
    while i < len(theData):
        crab = Crab(theData[i])
        list_of_crab.append(crab)
        i += 1
    
    #Determine the horizontal position that the crabs can align to using 
    # the least fuel possible.
    #process the data and return the answer
    bestPos, lowestFuelCost = check_the_crabs(list_of_crab, minPos, maxPos)
    
    print("the best horizontal position: ", bestPos,'\n') 
    print("the fuel they must spend to align all to that position? ", lowestFuelCost,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()