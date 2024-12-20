# 2024 Advent of code
# source: https://adventofcode.com/2024

from operator import truediv
import os
from collections import Counter

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 9, part 1 .... >')
    print()
    return  

def expand_disk(map):
    #read two and two numbers
    # first number is a file, the second is free space
    new_disk = ''
    i  = 0
    file_id = 0
    while i < len(map):
        xFile = int(map[i])
        #check if last number in map
        if i == (len(map) - 1): 
            xFree = 0
        else:
            xFree = int(map[i+1])
        #add file info to disk
        j = 0
        while j < xFile:
            new_disk = new_disk + str(file_id)
            j += 1
        #add free space info to disk
        j = 0
        while j < xFree:
            new_disk = new_disk + '.'
            j += 1
        
        i += 2
        file_id += 1

    # Each file on disk also has an ID number based on the order of 
    # the files as they appear before they are rearranged, starting with ID 0

    return new_disk

#move file blocks one at a time from the end of the disk to the leftmost free space
def move_blocks(disk):
    pos = 0
    new_disk = list(disk)
    reverse_pos = len(disk) - 1  # Start from the last index

    while pos < reverse_pos:
        # Find the rightmost digit
        while reverse_pos >= 0 and not new_disk[reverse_pos].isdigit():
            reverse_pos -= 1

        # If no more digits, break
        if reverse_pos < 0:
            break

        # Find the leftmost dot
        while pos < len(new_disk) and new_disk[pos] != '.':
            pos += 1

        # If no more dots, break
        if pos >= len(new_disk):
            break

        # Swap the digit with the dot
        new_disk[pos], new_disk[reverse_pos] = new_disk[reverse_pos], '.'
        
        # Move position pointers
        pos += 1
        reverse_pos -= 1

    return ''.join(new_disk)

def calc_checksum(disk):
    checksum = 0
    #To calculate the checksum, add up the result of multiplying each of these blocks' 
    # position with the file ID number it contains. The leftmost block is in position 0.
    id = 0
    for item in disk:
        if item.isdigit():
            checksum = checksum + (id * int(item))
            id += 1

    return checksum

def process_the_data(theData):
    steps = 42
    #expand disk map into a new disk
    for row in theData:
        row.strip()
        new_disk = expand_disk(row)
    
    #move file blocks one at a time from the end of the disk to the leftmost free space
    new_disk = move_blocks(new_disk)

    checksum = calc_checksum(new_disk)
    steps = checksum

    return steps

def get_the_data():
    #read the test puzzle input 
    #theData = open('day9_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day9_2024_puzzle_input.txt', 'r')
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
    
    print('What is the resulting filesystem checksum -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()