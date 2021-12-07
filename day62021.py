# Day6 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/6

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 6, part 2 .... >')
    print()
    return

class Fish():
    def __init__(self, timer):
        self.timer = timer
    
    #get the timere
    def get_timer(self):
        return self.timer
    
    #set timer
    def set_timer(self, timer):
        self.timer = timer
        return

    #reduce timer
    def reduce_timer(self):
        self.timer -= 1
        return self.timer
#end class definition

def check_for_fish(list_of_fish):
    #list of fish contain fish objects
    i = 0
    new_list_of_fish = []
    while i < len(list_of_fish):
        #reduce timer for the fish
        fish = list_of_fish[i]
        timer = fish.reduce_timer()
        if timer < 0:
            #reduce timer to 6 and create new fish with timer = 8
            fish.set_timer(6)
            fish = Fish(8)
            #add new fish to new list
            new_list_of_fish.append(fish)
        i += 1

    #add all new fishes to the list
    i = 0
    while i < len(new_list_of_fish):
        fish = new_list_of_fish[i]
        list_of_fish.append(fish)
        i += 1

    return list_of_fish

def get_the_data():
    #read the test puzzle input 
    #theData = open('day62021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day62021_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        i = 0
        for char in element:
            if char != ",":
                data_list.append(int(char))
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()

    #create fishes first time based on input
    i = 0
    list_of_fish = []
    while i < len(theData):
        fish = Fish(theData[i])
        list_of_fish.append(fish)
        i += 1
        
    days = 1
    maxDays = 256 #256 in part 2 - extremely long runtime with this implementation
    while days <= maxDays:
    #process the data and return the answer
        list_of_fish = check_for_fish(list_of_fish)
        days += 1

    print("How many lanternfish would there be after", maxDays, " days? ", len(list_of_fish),'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()