# 2024 Advent of code
# source: https://adventofcode.com/2024

from operator import truediv
import os
from collections import Counter

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 8, part 2 .... >')
    print()
    return

#This function scans the map to find all antennas and groups them by their frequency.
def find_antennas(map_data):
    antennas = {}
    for y, row in enumerate(map_data):
        for x, char in enumerate(row):
            if char.isalnum():  # Check if character is a letter or digit
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

# This function calculates potential antinode positions by checking pairs of antennas 
# with the same frequency. It checks both vertical and horizontal alignments and calculates 
# positions based on the given conditions.
def calculate_antinodes(antennas, map_data):
    antinodes = set()
    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Calculate the vector from one antenna to the other
                dx = x2 - x1
                dy = y2 - y1

                # Calculate potential antinodes
                antinode_1 = (x1 - dx, y1 - dy)
                antinode_2 = (x2 + dx, y2 + dy)

                # Validate and add antinodes within map boundaries
                for ax, ay in [antinode_1, antinode_2]:
                    if 0 <= ax < len(map_data[0]) and 0 <= ay < len(map_data):
                        antinodes.add((ax, ay))

    return antinodes

def process_the_data(theData):
    steps = 0
    # move the input data to the map
    map_data = theData
    #find antennas
    antennas = find_antennas(map_data)
    #calc antinodes
    antinodes = calculate_antinodes(antennas, map_data)
    steps = len(antinodes)

    return steps

def get_the_data():
    #read the test puzzle input 
    theData = open('day8_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day8_2024_puzzle_input.txt', 'r')
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
    
    print('How many unique locations contain an antinode -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()