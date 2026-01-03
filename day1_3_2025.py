#  Day1 - 2025 Advent of code
# source: https://adventofcode.com/2025

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2025 Day 1, part 1 .... >')
    print()
    return

def process_the_data(theData):
    dial = 50
    pword = 0
    for element in theData:
        # Extract the substring starting from the second character (index 1) which contains the numbers
        number_str = element[1:]
        # Convert the extracted string to an integer (use full number, not just % 100)
        number = int(number_str)
        # Store previous dial value
        previous_dial = dial
        
        # Count how many times we pass through zero during the rotation
        # Use mathematical formula instead of iterating through all positions
        if element[0] == 'L':
            # For left rotation: we visit positions dial-1, dial-2, ..., dial-number
            # We pass through 0 when (dial - i) % 100 == 0, i.e., dial - i = 100*k
            # So i = dial - 100*k, and we need 1 <= i <= number
            # This gives: (dial - number) / 100 <= k <= (dial - 1) / 100
            # Count integer k values in this range
            start_k = (dial - number + 99) // 100  # Ceiling of (dial - number) / 100
            end_k = (dial - 1) // 100  # Floor of (dial - 1) / 100
            if start_k <= end_k:
                pword += (end_k - start_k + 1)
            dial = (dial - number) % 100
        else:
            # For right rotation: we visit positions dial+1, dial+2, ..., dial+number
            # We pass through 0 when (dial + i) % 100 == 0, i.e., dial + i = 100*k
            # So i = 100*k - dial, and we need 1 <= i <= number
            # This gives: (dial + 1) / 100 <= k <= (dial + number) / 100
            # Count integer k values in this range
            start_k = (dial + 1 + 99) // 100  # Ceiling of (dial + 1) / 100
            end_k = (dial + number) // 100  # Floor of (dial + number) / 100
            if start_k <= end_k:
                pword += (end_k - start_k + 1)
            dial = (dial + number) % 100

    # print the content of pword
    #print('the dial is at: ', dial)
    #print('the pasword is: ', pword)

    return pword

def get_the_data():
    #read the puzzle input 
    #theData = open('day1_2025_test_puzzle_input.txt', 'r')
    theData = open('day1_2025_puzzle_input.txt', 'r')
    
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
    
    print('The password is  -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()