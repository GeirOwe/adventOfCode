# 2024 Advent of code
# source: https://adventofcode.com/2024

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 12, part 2 .... >')
    print()
    return  

# The code now tracks sides using a set called `sides`. Each side is represented by a 
# tuple containing the coordinates of its start point and its orientation 
# (‘H’ for horizontal and ‘V’ for vertical).
#	•	Unique Sides: By storing sides as tuples in a set, we ensure that each unique
#       straight section is only counted once.
#	•	Output: The function returns both the area and the number of distinct sides 
#       for each region.
def find_regions_with_sides(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c, plant_type):
        stack = [(r, c)]
        area = 0
        perimeter = 0
        sides = set()

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
                    # Record the side as a tuple (min(x1, x2), min(y1, y2), direction)
                    # direction is 'H' for horizontal and 'V' for vertical
                    if dx != 0:  # Vertical side
                        sides.add((min(x, nx), y, 'V'))
                    else:  # Horizontal side
                        sides.add((x, min(y, ny), 'H'))

        return area, len(sides)

    regions = {}
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = grid[r][c]
                area, num_sides = dfs(r, c, plant_type)
                if plant_type not in regions:
                    regions[plant_type] = []
                regions[plant_type].append((area, num_sides))

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
    regions_info = find_regions_with_sides(grid)

    #calculate the total price; area * number_of_sides
    tot_price = 0
    for plant_type, info in regions_info.items():
        print(f"Plant {plant_type}:")
        for i, (area, num_sides) in enumerate(info):
            print(f" Region {i+1}: Area={area}, Sides={num_sides}")
            tot_price += area * num_sides

    return tot_price

def get_the_data():
    #read the test puzzle input 
    theData = open('day12_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day12_2024_puzzle_input.txt', 'r')
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