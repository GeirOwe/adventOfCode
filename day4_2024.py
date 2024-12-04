# Day4 - 2024 Advent of code
# source: https://adventofcode.com/2024

from operator import truediv
import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 4, part 1 .... >')
    print()
    return

def find_word_in_grid(grid, word):
    def search_direction(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    occurrences = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == word[0]:
                for dx, dy in directions:
                    if search_direction(i, j, dx, dy):
                        occurrences.append((i, j))

    return occurrences

def process_the_data(theData):
    noOfReports = 0
    grid = []
    for row in theData:
        a_list = [row[i] for i in range(len(row))]
        grid.append(a_list)

    # Example usage:
    #grid = [
    #    ['X', 'M', 'A', 'S'],
    #    ['M', 'X', 'M', 'A'],
    #    ['A', 'A', 'X', 'M'],
    #    ['S', 'A', 'M', 'X']
    #]
    word = "XMAS"
    print(find_word_in_grid(grid, word))

    return noOfReports

def get_the_data():
    #read the test puzzle input 
    theData = open('day4_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day4_2024_puzzle_input.txt', 'r')
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