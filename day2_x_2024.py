# 2024 Advent of code
# source: https://adventofcode.com/2024

from operator import truediv
import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 2, part 2 .... >')
    print()
    return

def is_safe_report(numbers):
    def is_valid_sequence(nums):
        # checks if a sequence is valid according to the given rules:
        # It's either all increasing or all decreasing.
        # Adjacent numbers differ by at least 1 and at most 3.
        if len(nums) < 2:
            return True
        diff = nums[1] - nums[0]
        # zip(nums, nums[1:]): This creates pairs of adjacent numbers in the list.
        # calculates the absolute difference between adjacent numbers.                
        return all(1 <= abs(b - a) <= 3 and (b - a) * diff > 0 for a, b in zip(nums, nums[1:]))

    # Check if the original sequence is valid
    if is_valid_sequence(numbers):
        return True

    # Try removing one number at a time: numbers[:i] + numbers[i+1:]:
    # This creates a new list by concatenating two slices of the original list:
    # numbers[:i]: All elements from the start up to (but not including) index i.
    # numbers[i+1:]: All elements from index i+1 to the end.
    # Effectively, this removes the element at index i from the list.
    return any(is_valid_sequence(numbers[:i] + numbers[i+1:]) for i in range(len(numbers)))

def process_the_data(theData):
    noOfReports = 0
    #check if the report is safe
    for row in theData:
        row_list = row.split(' ')
        #change row into a list of integers
        int_list = [int(x) for x in row_list]

        #check if the report is safe
        safe = is_safe_report(int_list)
        if safe: noOfReports += 1

    return noOfReports

def get_the_data():
    #read the test puzzle input 
    #theData = open('day2_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day2_2024_puzzle_input.txt', 'r')
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