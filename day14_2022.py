# Day14 2022 for Advent of Code
# source: https://adventofcode.com/

import os
import sys
import resource

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 14 part 1 .... >')
    print()
    return

#define the grid -> find lowest/higest x and y
def grid_borders(theData):
    minX, minY = 100000, 100000
    maxX, maxY = 0, 0, 
    for row in theData:
        splitX = row.split()
        j = 0
        while j < len(splitX):
            s = splitX[j].split(',')
            x = int(s[0])
            y = int(s[1])
            if x < minX: minX = x
            if x > maxX: maxX = x
            if y < minY: minY = y
            if y > maxY: maxY = y
            j += 2
    #set as a constant in rebus
    minY = 0
    return minX, minY, maxX, maxY

def define_grid(minX, minY, maxX, maxY):
    grid = []
    #loop thru rows and add to matrix
    i = 0
    while i <= maxY:
        list = []
        j = 0
        while j <= ((maxX-minX)):   #add 1 extra for the abyss column
            if j==0: list.append('~')
            list.append('.')
            j += 1
        grid.append(list)
        i += 1
    return grid

def draw_path(grid, path):
    prevX, prevY = 0, 0
    for coord in path:
        x = coord[0] + 1    #no rocks in the abyss -> column zero
        y = coord[1]
        #first coord?
        if prevX == 0: 
            grid[y][x] = '#'
            prevX = x
            prevY = y
        else:
            #same column as previous?
            if x == prevX:
                #repeat for all y
                j = 0
                no_of_rows = abs(y-prevY)
                #number of steps
                while j < no_of_rows:
                    if y > prevY:
                        # go down one step
                        grid[prevY+1][x] = '#'
                        prevY += 1
                    else: 
                        #go up
                        grid[prevY-1][x] = '#'
                        prevY -= 1
                    j += 1
            else:
                #same row - repeat for all y
                j = 0
                no_of_cols = abs(x-prevX)
                #number of steps
                while j < no_of_cols:
                    if x > prevX:
                        # go right
                        grid[y][prevX + 1] = '#'
                        prevX += 1
                    else: 
                        #go left
                        grid[y][prevX - 1] = '#'
                        prevX -= 1
                    j += 1
                                     
    return grid 

def pour_sand(grid, sand, units_of_sand, more_sand):
    empty = ['.']
    abyss = ['~']
    last_row = False
    # sand is produced one unit at a time, and the next unit of sand is 
    # not produced until the previous unit of sand comes to rest
    # The sand is pouring into the cave from point 500,0.
    x = sand[0]
    y = sand[1] + 1
    #next row, unless last row
    if y < len(grid): last_row = False
    else: 
        last_row = True
        y = sand[1]
    #continue to drop?
    if grid[y][x] in empty and last_row == False:
        # continue to drop
        sand[1] = y
        units_of_sand, more_sand = pour_sand(grid, sand, units_of_sand, more_sand)
    else:
        # instead move diagonally one step down and to the left
        # If that tile is blocked, the unit of sand attempts to instead move 
        # diagonally one step down and to the right.
        x = sand[0] - 1
        if grid[y][x] in empty or grid[y][x] in abyss:
            if grid[y][x] in empty:
                #continue here
                sand[0] = x
                sand[1] = y
                units_of_sand, more_sand = pour_sand(grid, sand, units_of_sand, more_sand)
            else: 
                more_sand = False
        else:
            x = sand[0] + 1
            if grid[y][x] in empty or grid[y][x] in abyss:
                if grid[y][x] in empty:
                    #continue here
                    sand[0] = x
                    sand[1] = y
                    units_of_sand, more_sand = pour_sand(grid, sand, units_of_sand, more_sand)
                else: 
                    #the abyss - stop
                    more_sand = False
            else:
                #check if current pos = empty
                x = sand[0]
                y = sand[1]
                if grid[y][x] in empty:
                    #come to rest
                    units_of_sand += 1
                    grid[y][x] = 'o'
                else:
                    #the abyss - stop
                    more_sand = False

    return units_of_sand, more_sand

def add_rocks(grid, theData, minX, minY):
    for row in theData:
        splitX = row.split()
        j = 0
        #get all points for the path
        path = []
        while j < len(splitX):
            coord = []
            s = splitX[j].split(',')
            x = int(s[0]) - minX
            y = int(s[1]) - minY
            coord.append(x)
            coord.append(y)
            #add coordinates to path
            path.append(coord)
            j += 2
        # draw path in grid
        grid = draw_path(grid, path)
    return grid

def sand_start(minX):
    sand = []
    x = (500 - minX) + 1    #pluss one for the abyss, column zero
    sand.append(x)
    sand.append(0) 
    return sand, x

#start function
def process_data(theData):
    #define the grid -> find lowest/higest x and y
    #remember: x = col, y = row. So grid[y][x]
    minX, minY, maxX, maxY = grid_borders(theData)
    # add air
    grid = define_grid(minX, minY, maxX, maxY)
    # add the rocks
    grid = add_rocks(grid, theData, minX, minY)
    # add sand at 500, 0
    sand, x = sand_start(minX)
    grid[0][x] = '+'
    # start pouring the sand. sand is produced one unit at a time, 
    # and the next unit of sand is not produced until the previous 
    # unit of sand comes to rest
    units_of_sand = 0
    more_sand = True
    while more_sand:
        # add sand at 500, 0
        sand, x = sand_start(minX)
        units_of_sand, more_sand = pour_sand(grid, sand, units_of_sand, more_sand)
    return units_of_sand
#end function

def get_the_data():
    #read the test puzzle input 
    theData = open('day142022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day142022_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        element = element.strip()
        data_list.append(element)
    return data_list

#start function
def start_the_challenge():
    #change recursion limit and resource usage
    #sys.setrecursionlimit(30000)
    #resource.setrlimit(10000)
    
    #get the data and read the into  list
    theData = get_the_data()

    #process the codes and return the answer
    valueX = process_data(theData) 
    
    print('forventet resultat er ...  24 ...') 
    print('How many units of sand come to rest -> ', valueX, '\n')

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()