# Dayx - 2024 Advent of code
# source: https://adventofcode.com/2024

from operator import truediv
import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 2, part 1 .... >')
    print()
    return

def allIncreasing(nums):
    def is_increasing(arr):
        return all(arr[i] < arr[i+1] for i in range(len(arr) - 1))
    
    # Check if the original list is increasing
    if is_increasing(nums):
        return True
    
    # Try removing one number at a time
    for i in range(len(nums)):
        temp = nums[:i] + nums[i+1:]
        if is_increasing(temp):
            return True
    
    return False

def allDecreasing(nums):
    def is_decreasing(arr):
        return all(arr[i] > arr[i+1] for i in range(len(arr) - 1))
    
    # Check if the original list is decreasing
    if is_decreasing(nums):
        return True
    
    # Try removing one number at a time
    for i in range(len(nums)):
        temp = nums[:i] + nums[i+1:]
        if is_decreasing(temp):
            return True
    
    return False

def adjacentOk(row):
    def is_safe(levels):
        return all(1 <= abs(int(a) - int(b)) <= 3 for a, b in zip(levels, levels[1:]))

    # Check if the original row is safe
    if is_safe(row):
        return True

    # Try removing one element at a time
    return any(is_safe(row[:i] + row[i+1:]) for i in range(len(row)))

def process_the_data(theData):
    noOfReports = 0
    #check if the report is safe
    for row in theData:
        #change row into a list of integers
        row_list = row.split(' ')
        int_list = [int(x) for x in row_list]
        # check the list according to the criteria
        increase = allIncreasing(int_list)
        decrease = allDecreasing(int_list)
        adjacent = adjacentOk(int_list)

        #it both conditions are true, the report is safe    
        if (increase or decrease) and adjacent: noOfReports += 1
    return noOfReports

def get_the_data():
    #read the test puzzle input 
    theData = open('day2_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day2_2024_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('How many reports are safe -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()