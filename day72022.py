# Day7 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/7

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 7, part 1 .... >')
    print()
    return

def build_filesys(theData):
    #initialize
    filesys = []
    i = 0 # no of rows in filesys
    level = 0 #where in filesys
    for row in theData:
        if row[0] == '$' and (row[2].lower()) == 'c':
            # a / means go to (or add) root level
            if row[5] == '/':
                if i == 0: 
                    #add root level
                    filesys.append(row[5] + str(level))
                    level += 1
                    i += 1
                else:
                    #go to root level
                    level = 0
            else:
                #go to a (or add ) a dir or move up one level
                if row[5] == '.': 
                    level -= 1
                    if level < 0: level = 0 #cant go beyond root level
                    else:
                        filesys.append('!' + str(level))
                        i += 1 
                else:
                    #last row?
                    if i == len(filesys): 
                        #add new level level
                        level += 1
                        filesys.append(row[5] + str(level))
                        i += 1
                    else: 
                        level += 1
        elif row[0].isdigit():
            # capture the size of the file
            sizeX = row.split()
            size = int(sizeX[0])
            filesys.append(size)
            i += 1

    return filesys

def find_dir_size(level, rowNo, filesys):
    dir_size = 0
    max_size = 100000
    i = 0
    for row in filesys:
        if i > rowNo:
            # The total size of a directory is the sum of the sizes 
            # of the files it contains, directly or indirectly 
            # Check if row is string 
            is_string = isinstance(row, str)
            if is_string: 
                #if this_level: this_level = False
                #else: 
                    if int(row[1:]) <= level: break
            else:
                dir_size += row
                if dir_size > max_size: break
            
        i += 1
    return dir_size

# find all of the directories with a total size of at most 100000
def check_dir(filesys):
    relevant_dir = []
    rowNo = 0
    max_size = 100000
    for row in filesys:
        #look for directories
        # Check if row is string 
        row_is_string = isinstance(row, str)
        if row_is_string:    
            # find size of all files in dir
            level = int(row[1:])
            dir_size = find_dir_size(level, rowNo, filesys)
            if dir_size < max_size: 
                relevant_dir.append(dir_size)
        rowNo += 1

    return relevant_dir

def print_it(filesys):
    for row in filesys:
        # Check if row is string 
        row_is_string = isinstance(row, str)
        if row_is_string:
            print()
            x = int(row[1:])
            i = 0
            while i < x:
                print('.', end =" ")
                i += 1
            print(row, end =" ")
        else:
           print(row, end =" ") 

    return

def process_the_data(theData):
    #build filesys
    filesys = build_filesys(theData)
    #print_it(filesys)
    #print('\n')

    # find all of the directories with a total size of at most 100000
    relevant_dir = check_dir(filesys)

    # then calculate the sum of their total sizes.
    valueX = sum(relevant_dir)

    return valueX

def get_the_data():
    #read the test puzzle input 
    #theData = open('day72022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day72022_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        element = element.strip()
        data_list.append(element)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: ...
    valueX = process_the_data(theData) 
    
    print('What is the sum of the total sizes of those directories -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()

