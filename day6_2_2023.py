# Day6 - 2023 Advent of code

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 6, part 1 .... >')
    print()
    return

def get_list(row):
    x, data = row.split(':')
    listStr = data.split()
    #convert from str to int
    new = ''
    for num in listStr:
        new = new + num
    return int(new)

def process_the_data(theData):
    #set initial position for the dataset
    valueX = 1
    #extract input file into the two lists
    time = get_list(theData[0])
    distance = get_list(theData[1])
    #do the races
    record_beaten = 0
    beat_rec = []
    noOfRaces = 1
    i = 0
    #repeat for all races
    while i < noOfRaces:
        button = 0
        #button can not be held longer than available time
        while button < time:
            speed = button * 1
            remaining_time = time - button
            my_distance = speed * remaining_time
            if my_distance > distance: 
                record_beaten += 1
                #print(button, speed, remaining_time, my_distance)
            button += 1
        
        # number of ways to beat record
        i += 1
        if record_beaten > 0: beat_rec.append(record_beaten)
        record_beaten = 0

    #calculate result
    for num in beat_rec:
        valueX = valueX * num
    return valueX

def get_the_data():
    #read the test puzzle input 
    #theData = open('day62023_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day62023_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 1856459736
    valueX = process_the_data(theData) 
    
    print('What do you get if you multiply these numbers together -> ', valueX,'\n') 
    return

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()