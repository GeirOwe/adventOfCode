# 2024 Advent of code
# source: https://adventofcode.com/2024

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 10, part 1 .... >')
    print()
    return  

def find_hiking_trails(map_grid):
    rows = len(map_grid)
    cols = len(map_grid[0])
    
    # Checks if a given position `(x, y)` is within the bounds of the grid.
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    #`dfs(x, y, current_height)`: A depth-first search function that explores 
    # all possible paths starting from `(x, y)` with the current height. It returns a set of 
    # positions where height 9 can be reached. The DFS function marks each visited cell 
    # temporarily by adding `10` to avoid revisiting during the same path exploration.
	# It explores all four cardinal directions (up, down, left, right) and continues only 
    # if the next cell’s height is exactly one more than the current height.
    def dfs(x, y, current_height):
        if not is_valid(x, y) or map_grid[x][y] != current_height:
            return set()
        
        if current_height == 9:
            return {(x, y)}
        
        # Mark the current position as visited by incrementing it temporarily
        map_grid[x][y] += 10
        
        # Explore all four possible directions
        trails = set()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            trails.update(dfs(nx, ny, current_height + 1))
        
        # Unmark the current position
        map_grid[x][y] -= 10
        
        return trails

    # Find all trailheads and calculate their scores
    # For each position with height `0`, it calculates 
    # how many unique positions with height `9` can be reached using DFS.
	# Stores the results in a dictionary `trailhead_scores` where keys are 
    # trailhead coordinates and values are their scores.
    trailhead_scores = {}
    for i in range(rows):
        for j in range(cols):
            if map_grid[i][j] == 0:
                reachable_nines = dfs(i, j, 0)
                trailhead_scores[(i, j)] = len(reachable_nines)
    
    return trailhead_scores

def process_the_data(theData):
    map_grid = []
    #convert the input data to the grid map
    for row in theData:
        grid_line = list(row)
        #convert from str to int
        i = 0
        for numb in grid_line:
            grid_line[i] = int(numb)
            i += 1
        map_grid.append(grid_line)

    #find trails and their score
    trailhead_scores = find_hiking_trails(map_grid)
    #summarize the trailhead scores
    my_sum = sum(trailhead_scores.values())
    #print(trailhead_scores)

    return my_sum

def get_the_data():
    #read the test puzzle input 
    #theData = open('day10_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day10_2024_puzzle_input.txt', 'r')
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
    
    print('What is the sum of the scores of all trailheads on your topographic map? -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()