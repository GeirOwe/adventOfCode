# 2024 Advent of code
# source: https://adventofcode.com/2024

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 12, part 1 .... >')
    print()
    return  

# calculates the area and perimeter of connected regions of plants in a grid. 
def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    # It uses depth-first search (DFS) to explore each region and determine its 
    # size and boundary length.
    def dfs(r, c, plant_type):
        stack = [(r, c)]
        area = 0
        perimeter = 0
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            area += 1
            borders = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == plant_type:
                    if not visited[nx][ny]:
                        stack.append((nx, ny))
                else:
                    borders += 1
            perimeter += borders
        return area, perimeter

    # The results are stored in a dictionary with plant types as keys.
    regions = {}
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = grid[r][c]
                area, perimeter = dfs(r, c, plant_type)
                if plant_type not in regions:
                    regions[plant_type] = []
                regions[plant_type].append((area, perimeter))

    return regions

def process_the_data(theData):
    # build the grid from the input data
    grid = []

    for row in theData:
        # split the row into a list of chars
        row_list = []
        for char in row:
            row_list.append(char)
        
        # add the row_list to the grid
        grid.append(row_list)

    # find info about regions, their area and perimeter
    # The results are stored in a dictionary with plant types as keys.
    regions_info = find_regions(grid)

    #calc price area * perimeter
    tot_price = 0
    for plant_type, info in regions_info.items():
        for i, (area, perimeter) in enumerate(info):
            tot_price += area * perimeter

    return tot_price

def get_the_data():
    #read the test puzzle input 
    #theData = open('day12_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day12_2024_puzzle_input.txt', 'r')
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
    
    print('What is the total price of fencing all regions on your map? -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()