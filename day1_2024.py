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
    x = zip(first_list, second_list)
    return sum(abs(a - b) for a, b in zip(first_list, second_list))
# This improved version has several Pythonic features:
# It uses zip() to pair up corresponding elements from both lists. It employs a generator 
# expression (similar to a list comprehension) to calculate the absolute differences.
# zip creates an iterable where each element is a tuple containing a and b.
# The for loop unpacks each tuple into the two variables.
# This version is more concise, easier to read, and generally more efficient. 

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

    # sort both list with the smallest numbers first and
    first_list.sort()
    second_list.sort()
    # calculate the the total distance between your lists
    totalDistance = calc_distance(first_list, second_list)
    # calculate the the total distance between your lists in a more pythonic way
    #totalDistance = calc_distance_pythonic(first_list, second_list)
    return totalDistance

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

def generate_fibonacci(n):
    """
    Generate Fibonacci numbers up to the nth number.
    """
    # Define a lambda function to calculate Fibonacci numbers
    # The lambda function uses recursion to calculate the nth Fibonacci number
    fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
    
    # Create a generator to generate Fibonacci numbers from 0 to n
    fibonacci_generator = (fib(i) for i in range(n + 1))
    
    print('Fibonacci numbers:')
    # Iterate through the generator and print each Fibonacci number
    for i in fibonacci_generator:
        print(i, end=' ')
    print('\n')

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('the total distance between your lists  -> ', valueX,'\n') 

    # Generate and print Fibonacci numbers up to 10
    generate_fibonacci(10)

    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()