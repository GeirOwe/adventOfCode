# Day8 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/6

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 8, part 1 .... >')
    print()
    return

class Sensor():
    def __init__(self, segments):
        self.segments = segments

    def get_segments(self):
        return self.segments
#end class definition


def check_the_data(signal_output, the_unique_no_of_systems):
    valueX = 0
    #how many times do digits in the_unique_no_of_systems appear in signal_output
    for element in signal_output:
        signalsList = element.split(" ")
        for signal in signalsList:
            if len(signal) in the_unique_no_of_systems: valueX += 1

    return valueX

def get_the_data():
    #read the test puzzle input 
    #theData = open('day82021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day82021_puzzle_input.txt', 'r')
    
    #move data into a list
    signal_output = []
    for element in theData:
        splitX = element.split((' | '))
        signal_pattern = splitX[0].strip()      #ten unique signal patterns
        output_value = splitX[1].strip()        #the four digit output value
        signal_output.append(output_value)

    return signal_output

def list_of_sensors():
    #create the sensors
    i = 0
    noOfSensors = 9
    list_of_sensors = []
    #sensors and so of segments
    sensor = Sensor(6)
    list_of_sensors.append(sensor)
    sensor = Sensor(2)
    list_of_sensors.append(sensor)
    sensor = Sensor(5)
    list_of_sensors.append(sensor)
    sensor = Sensor(5)
    list_of_sensors.append(sensor)
    sensor = Sensor(4)
    list_of_sensors.append(sensor)
    sensor = Sensor(5)
    list_of_sensors.append(sensor)
    sensor = Sensor(6)
    list_of_sensors.append(sensor)
    sensor = Sensor(3)
    list_of_sensors.append(sensor)
    sensor = Sensor(7)
    list_of_sensors.append(sensor)
    sensor = Sensor(6)
    list_of_sensors.append(sensor)
    return list_of_sensors

def start_the_engine():
    #get the data and read them into a list
    signal_output = get_the_data()
    #create the list of sensor objects
    sensors_list = list_of_sensors()
    no1 = sensors_list[1].get_segments()
    no2 = sensors_list[4].get_segments()
    no3 = sensors_list[7].get_segments()
    no4 = sensors_list[8].get_segments()
    the_unique_no_of_systems = [no1, no2, no3, no4]

    #check
    valueX = check_the_data(signal_output, the_unique_no_of_systems)
    print("how many times do digits 1, 4, 7, or 8 appear: ", valueX, "\n")
    
    print("number of sensors: ", len(sensors_list))
    i = 0
    while i < len(sensors_list):
        sensor = sensors_list[i]
        print(i, "- no of segments in sensor: ", sensor.get_segments())
        i += 1
    
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()