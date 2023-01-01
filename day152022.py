# Day15 2022 for Advent of Code
# source: https://adventofcode.com/

import os
import numpy as np

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 15 part 1 .... >')
    print()
    return

#define a Sensor object
class Sensor():
    def __init__(self, sx, sy, bx, by):
        self.sx = sx
        self.sy = sy
        self.bx = bx
        self.by = by
        return
    def get_sx(self):
        return self.sx
    def get_sy(self):
        return self.sy
    def get_bx(self):
        return self.bx
    def get_by(self):
        return self.by

#end sensor object

def make_sensors(sensors, beacons, offset):
    sensor_list = []
    i = 0
    while i < len(sensors):
        sx = sensors[i][0] + offset
        sy = sensors[i][1]
        bx = beacons[i][0] + offset
        by = beacons[i][1]
        #create a sensor object
        sensor = Sensor(sx, sy, bx, by)
        #add sensor object to a list
        sensor_list.append(sensor)
        i += 1
    return sensor_list

#define the grid -> find lowest/higest x and y
def grid_borders(theData):
    minX, minY = 10000000, 10000000
    maxX, maxY = 0, 0
    sensors = []
    beacons = []
    for row in theData:
        s = row.split()
        #sensor x in s[2] .. sensor y in s[3]
        sx = s[2].split('=')
        sx = int(sx[1].strip(','))
        sy = s[3].split('=')
        sy = int(sy[1].strip(':'))
        #add coord to sensor list
        xy = []
        xy.append(sx)
        xy.append(sy)
        sensors.append(xy)
        #beacon x in s[8] .. sensor y in s[9]
        bx = s[8].split('=')
        bx = int(bx[1].strip(','))
        by = s[9].split('=')
        by = int(by[1].strip())
        #add coord to beacon list
        xy = []
        xy.append(bx)
        xy.append(by)
        beacons.append(xy)
        #check sensor x,y
        x = sx
        y = sy
        if x < minX: minX = x
        if x > maxX: maxX = x
        if y < minY: minY = y
        if y > maxY: maxY = y
        #check beacon x, y
        x = bx
        y = by
        if x < minX: minX = x
        if x > maxX: maxX = x
        if y < minY: minY = y
        if y > maxY: maxY = y
    #set as a constant in rebus
    minY = 0
    #offset is how far below zero x is
    if minX < 0: offset = 0 - minX
    else: offset = 0

    return minX, minY, maxX, maxY, offset, sensors, beacons

def init_grid(minX, minY, maxX, maxY):
    grid = []
    row = []
    x, y = 0, 0
    while y < maxY:
        while x < maxX:
            row.append('.')
            x += 1
        grid.append(row)
        x = 0
        y += 1
    #make grid into a numpy array. easier to work with cells
    grid = np.array(grid)
    return grid

def add_whitespace(grid, sx, sy, bx, by):
    empty = ['.', '#']
    diff = abs(sx-bx) + abs(sy-by)
    currY = sy
    currX = sx
    #mark current row

    #mark all rows above
    j = diff
    while j > 0:
        #move one row up
        currY -= 1
        #add whitespace to the row
        j -= 1
    #mark all rows below
    j = diff
    while j > 0:
        #move one row down        
        currY += 1
        #add whitespace to the row
        j -= 1
        
    return grid

def add_signals_to_grid(grid, sensor_list):
    for sensor in sensor_list:
        # get sensor object signals
        sx = sensor.get_sx()
        sy = sensor.get_sy()
        bx = sensor.get_bx()
        by = sensor.get_by()
        #y = row, x = col
        grid[sy][sx] = 'S'
        grid[by][bx] = 'B'
        grid = add_whitespace(grid, sx, sy, bx, by)

    return grid

#start function
def process_data(theData):
    valueX = -1
    #define the grid -> find lowest/higest x and y
    #remember: x = col, y = row. So grid[y][x]
    minX, minY, maxX, maxY, offset, sensors, beacons = grid_borders(theData)
    #initialize grid
    grid = init_grid(minX+offset, minY, maxX+offset, maxY)
    #add all sensor to a sensor object, add object to list
    sensor_list = make_sensors(sensors, beacons, offset)
    # add sensors and beacons to grid
    grid = add_signals_to_grid(grid, sensor_list)


    return valueX
#end function

def get_the_data():
    #read the test puzzle input 
    theData = open('day152022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day152022_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        element = element.strip()
        data_list.append(element)
    return data_list

#start function
def start_the_challenge():
    #get the data and read the into  list
    theData = get_the_data()

    #process the codes and return the answer
    valueX = process_data(theData) 
    
    print('how many positions cannot contain a beacon -> ', valueX, '\n')

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()