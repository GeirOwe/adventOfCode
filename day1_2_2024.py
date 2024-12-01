# Dayx - 2024 Advent of code
# source: https://adventofcode.com/2024

import os
from collections import Counter

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day X, part 2 .... >')
    print()
    return

# a more pythonic way by Perplexity.ai
def calc_similarity_more_pythonic(first_list, second_list):
    # Count occurrences in the second list
    second_list_counts = Counter(second_list)
    
    # Calculate similarity using a list comprehension and sum
    return sum(num * second_list_counts[num] for num in first_list)
# This improved version has several advantages: # It uses Counter from the collections module 
# to efficiently count occurrences in second_list. This is done once, outside the loop, reducing 
# time complexity. It replaces the while loop with a list comprehension, which is more Pythonic 
# and often faster. It uses sum() to add up all the similarity scores, which is more concise and 
# efficient than manually incrementing a total.

def calc_similarity(first_list, second_list):
    totalSim = 0
    item = 0
    #Calculate a total similarity score by adding up each number in the left list 
    #after multiplying it by the number of times that number appears in the right list
    while item < len(first_list):
        #Example: The first number in the test left list is 3. It appears in the 
        # right list three times, so the similarity score increases by 3 * 3 = 9.
        noOfTimes = second_list.count(first_list[item])
        similarity = first_list[item] * noOfTimes

        totalSim += similarity
        item += 1

    return totalSim

def process_the_data(theData):
    #set initial position for the dataset
    first_list = []
    second_list = []
    # loop thru the input data and split into two lists
    for theRow in theData:
        split = theRow.split('  ')
        first = int(split[0].strip())
        first_list.append(first)
        second = int(split[1].strip())
        second_list.append(second)

    #calculate the the total distance between your lists
    totalDistance = calc_similarity(first_list, second_list)
    #calculate the the total distance more efficient and Pythonic
    #totalDistance = calc_similarity_more_pythonic(first_list, second_list)
    
    return totalDistance

def get_the_data():
    #read the test puzzle input 
    #theData = open('day1_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day1_2024_puzzle_input.txt', 'r')
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
    
    print('their similarity score -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()