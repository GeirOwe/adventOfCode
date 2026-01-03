# 2023 for Advent of Code
# source: https://adventofcode.com/
import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 15 part 2 .... >')
    print()
    return

def hash_it(row):
    result = 0
    for char in row:
        # The current value starts at 0.
        # The first character ->; its ASCII code value
        # The current value increases with asci code value
        # The current value is multiplied by 17 .
        # The current value becomes the remainder of calue divided by 256.
        result = result + ord(char)
        result = result * 17
        result = result % 256

    return result

def get_label(row):
    #get ops character
    ops = ''
    if '-' in row: 
        label, foc_lenX = row.split('-')

        ops = '-'
    else:
        label, foc_lenX = row.split('=')
        ops = '='
    #use hash algorith to calc cox no
    # make foc length into an int
    box = hash_it(label)
    if foc_lenX == '': foc_lenX = '0'
    foc_len = int(foc_lenX)

    return label, box, ops, foc_len

def update_lenses(label, box, ops, foc_len, box_dict):
    #check what type of operation
    key_val = box_dict[str(box)]
    if ops == '-':
        # If the operation character is a dash (-), go to the relevant box and remove the lens 
        # with the given label if it is present in the box.
        j = 0
        for element in key_val:
            if label in element:
                key_val.pop(j)
                break
            j += 1
    else:
        # If the operation character is an equals sign (=)
        # If there is already a lens in the box with the same label, replace the old lens with the new lens:
        #    remove the old lens and put the new lens in its place, not moving any other lenses in the box.
        # if not already a lens in the box with the same label, add the lens to the box 
        #    immediately behind any lenses already in the box
        j = 0
        for element in key_val:
            if label in element:
                key_val[j] = label + ' ' + str(foc_len)
                break
            j += 1
        else:
            key_val.append(label + ' ' + str(foc_len))
    #update dict
    #box_dict[str(box)] = key_val


    return box_dict

def initialize_box():
    box_dict = {}
    # The book goes on to describe a series of 256 boxes numbered 0 through 255
    #  # box no is key. lenses are a list of lists
    i = 0
    for i in range(256):
        new_pair = [(str(i), [])]
        box_dict.update(new_pair)

    return box_dict

def calc_power(box_dict):
    sumX = 0
    for k, v in box_dict.items():
        #any value her to calculate?
        if len(v) > 0:
            j= 0
            for item in v:
                #print(item)
                j += 1  #value element no
                boxNo = int(k) + 1   # box
                _, foc_len = item.split()
                # power: (box + 1) * (value_element_no + 1) * focal_length
                power = boxNo * j * int(foc_len)
                #summarize power
                sumX += power

    return sumX

#start function
def process_data(theData):
    #we use a dictionary to track this
    # box no is key. lenses are a list of lists
    box_dict = initialize_box()
    for row in theData:
        label, box, ops, foc_len  = get_label(row)
        box_dict = update_lenses(label, box, ops, foc_len, box_dict)
        
    sumX = calc_power(box_dict)

    return sumX
#end function

def get_the_data():
    #read the test puzzle input 
    #theData = open('day15_2023_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day15_2023_puzzle_input.txt', 'r')
    #the codes are separated by comma - transfer them to a list
    data_list = theData.read().split(',')

    return data_list

#start function
def start_the_challenge():
    #get the data and read the into  list
    theData = get_the_data()
    #process the codes and return the answer
    valueX = process_data(theData) 
    
    print('What is the focusing power of the resulting lens configuration -> ', valueX, '\n')
    return 

#end function
#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()
