# Day5 - 2023 Advent of code
# source: https://adventofcode.com/2023/day/5

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 5, part 1 .... >')
    print()
    return

#add data to all the maps
def add_data(theData, map, i):
    #next row
    i += 1
    #add all data for seed to soil
    while len(theData[i]) > 0:
        dest, source, length = theData[i].split()
        j = 0
        d = int(dest)
        s = int(source)
        l = int(length)
        while j < l:    
            map.append(str((s+j)) + ' ' + str((d+j)))
            j += 1
        #next row un less last row
        i += 1
        if i >= len(theData): break

    #map = sorted(map)
    return map, i

#parse the maps and find destination value
def parse(seed, map):
    value = seed
    for r, v in enumerate(map):
        #r = row
        #v = value
        source, dest = v.split()
        if source == seed: 
            value = dest
            break
    return value

def process_the_data(theData):
    #set initial position for the dataset
    valueX = 0
    s2s = [] #seed 2 soil
    s2f = [] #soil 2 fert
    f2w = [] #fertilizer-to-water
    w2l = [] #water-to-light
    l2t = [] #light-to-temperature
    t2h = [] #temperature-to-humidity
    h2l = [] #humidity 2 location
    seeds = ''
    i = 0
    while i < len(theData):
        #first row is the seeds to be planted
        if theData[i].startswith('seeds:'): text, seeds = theData[i].split(':')
        #the rest are the maps
        if theData[i].startswith('seed-to-soil'): s2s, i = add_data(theData, s2s, i) 
        if theData[i].startswith('soil-to-fertilizer'): s2f, i = add_data(theData, s2f, i) 
        if theData[i].startswith('fertilizer-to-water'): f2w, i = add_data(theData, f2w, i) 
        if theData[i].startswith('water-to-light'): w2l, i = add_data(theData, w2l, i) 
        if theData[i].startswith('light-to-temperature'): l2t, i = add_data(theData, l2t, i) 
        if theData[i].startswith('temperature-to-humidity'): t2h, i = add_data(theData, t2h, i) 
        if theData[i].startswith('humidity-to-location'): h2l, i = add_data(theData, h2l, i) 
            
        #next row
        i += 1
    
    #process all the maps    
    seeds_list = []
    seeds_list = list(seeds.split())
    location_list = []
    # find location for each seed
    for seed in seeds_list:
        #seed to soil
        value = parse(seed, s2s)
        value = parse(value, s2f)
        value = parse(value, f2w)
        value = parse(value, w2l)
        value = parse(value, l2t)
        value = parse(value, t2h)
        location = parse(value, h2l)
        location_list.append(location)
    #
    location_list = sorted(location_list)
    valueX = location_list[0]
    return valueX

def get_the_data():
    #read the test puzzle input 
    #theData = open('day52023_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day52023_puzzle_input.txt', 'r')
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
    
    print('What is the lowest location number -> ', valueX,'\n') 
    return

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()