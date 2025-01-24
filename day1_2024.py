# 2024 Advent of code
# source: https://adventofcode.com/2024

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 1, part 1 .... >')
    print()
    return

def calc_distance(first_list, second_list):
    totalDiff = 0
    item = 0
    #calculate the difference and add to the total distance
    while item < len(first_list):
        diff = first_list[item] - second_list[item]
        if diff < 0: diff = diff * -1
        
        totalDiff += diff
        item += 1

    return totalDiff

#a more pythonic way for  the calc distance routine
def calc_distance_pythonic(first_list, second_list):
    """Calculate distance between two lists using Pythonic approach.

    Args:
        first_list (list): First list of integers
        second_list (list): Second list of integers

    Returns:
        int: Sum of absolute differences between corresponding elements
    """
    return sum(abs(a - b) for a, b in zip(first_list, second_list))
# This improved version has several Pythonic features:
# It uses zip() to pair up corresponding elements from both lists. It employs a generator 
# expression (similar to a list comprehension) to calculate the absolute differences.
# zip creates an iterable where each element is a tuple containing a and b.
# The for loop unpacks each tuple into the two variables.
# This version is more concise, easier to read, and generally more efficient. 

def process_the_data(the_data):
    """Process input data and calculate total distance between two lists.

    Args:
        the_data (list): List of strings containing space-separated numbers

    Returns:
        int: Total distance between sorted lists
    """
    # Set initial position for the dataset
    first_list = []
    second_list = []

    # Loop through the input data and split into two lists
    for row in the_data:
        split = row.split('  ')
        first = int(split[0].strip())
        first_list.append(first)
        second = int(split[1].strip())
        second_list.append(second)

    # Sort both lists with the smallest numbers first
    first_list.sort()
    second_list.sort()

    # Calculate the total distance between lists
    total_distance = calc_distance(first_list, second_list)
    # Alternative: using pythonic way
    # total_distance = calc_distance_pythonic(first_list, second_list)

    return total_distance

def get_the_data():
    #read the test puzzle input 
    theData = open('day1_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day1_2024_puzzle_input.txt', 'r')
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
    
    print('the total distance between your lists  -> ', valueX,'\n') 

    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()