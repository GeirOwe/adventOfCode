# Day10 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/10
import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 10, part 1 .... >')
    print()
    return

#During the 20th cycle, register X has the value 21, so the signal strength is 20 * 21 = 420.
def new_row(cycle, crt_row, the_crt):
    the_crt.append(crt_row)
    crt_row = []
    cycle = 0
    return cycle, crt_row, the_crt

def draw_pixel(crt_row, register):
    #If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, 
    # the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.)
    pos = len(crt_row)
    if pos == register-1 or pos == register or pos == register+1: crt_row.append('#')
    else: crt_row.append('.')
    return crt_row

def process_signal(instruction, register, cycle, crt_row, the_crt):
    #he CPU has a single register, X, which starts with the value 1. It supports only two instructions:
    # addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
    # noop takes one cycle to complete. It has no other effect.
    key_cycles = [40]
    splitX = instruction.split()
    #the sprite is 3 pixels wide, and the X register sets the horizontal position of the middle of that sprite. 
    if len(splitX) == 1: 
        # noop
        # At the start of the first cycle, the noop instruction begins execution. During the first cycle, X is 1. 
        # After the first cycle, the noop instruction finishes execution, doing nothing
        cycle += 1 
        crt_row = draw_pixel(crt_row, register)    
        # new row?
        if cycle in key_cycles: cycle, crt_row, the_crt = new_row(cycle, crt_row, the_crt)
    else:
        #process the instruction in two cycles
        value = int(splitX[1])
        j = 0
        while j <= 2:
            #During cycle  2: CRT draws pixel in position 1
            #Current CRT row: ##
            #End of cycle  2: finish executing addx 15 (Register X is now 16)
            #Sprite position: ...............###.......................
            if j == 2:  # cycle is finished
                register += value
            else:
                cycle += 1
                #If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, 
                # the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.)
                crt_row = draw_pixel(crt_row, register)
                if cycle in key_cycles: cycle, crt_row, the_crt = new_row(cycle, crt_row, the_crt)
            j += 1

    return register, cycle, crt_row, the_crt

def process_the_data(theData):
    #find answer
    register = 1
    cycle = 0
    crt_row = []
    the_crt = []
    for row in theData:
        # process the signal
        register, cycle, crt_row, the_crt = process_signal(row, register, cycle, crt_row, the_crt)

    return the_crt

def get_the_data():
    #read the test puzzle input 
    #theData = open('day102022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day102022_puzzle_input.txt', 'r')
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
    the_crt = process_the_data(theData)

    print('What eight capital letters appear on your CRT -> ', '\n') 
    for row in the_crt:
        print(' '.join(row))
    
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()

