# Day10 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/10
import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 10, part 1 .... >')
    print()
    return

#During the 20th cycle, register X has the value 21, so the signal strength is 20 * 21 = 420.
def calc_signal(cycle, register, signal_strength):
    signal_strength = signal_strength + (cycle * register)
    return signal_strength

def process_signal(instruction, register, cycle, signal_strength):
    #he CPU has a single register, X, which starts with the value 1. It supports only two instructions:
    # addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
    # noop takes one cycle to complete. It has no other effect.
    key_cycles = [20, 60, 100, 140, 180, 220]
    splitX = instruction.split()
    if len(splitX) == 1: 
        # noop
        # At the start of the first cycle, the noop instruction begins execution. During the first cycle, X is 1. 
        # After the first cycle, the noop instruction finishes execution, doing nothing
        cycle += 1     
        # consider the signal strength 
        if cycle in key_cycles: signal_strength = calc_signal(cycle, register, signal_strength)
    else:
        #process the instruction in two cycles
        value = int(splitX[1])
        j = 0
        while j <= 2:
            # At the start of the second cycle, the addx 3 instruction begins execution. 
            # During the second cycle, X is still 1. During the third cycle, X is still 1. 
            # After the third cycle, the addx 3 instruction finishes execution, setting X to 4.
            if j == 2:  # cycle is finished
                register += value
            else:
                cycle += 1
                # consider the signal strength 
                if cycle in key_cycles: signal_strength = calc_signal(cycle, register, signal_strength)
            j += 1

    return register, cycle, signal_strength

def process_the_data(theData):
    #find answer
    register = 1
    cycle = 0
    signal_strength = 0
    for row in theData:
        # process the signal
        register, cycle, signal_strength = process_signal(row, register, cycle, signal_strength)

    return signal_strength

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
    valueX = process_the_data(theData) 
    
    print('What is the sum of these six signal strengths -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()

