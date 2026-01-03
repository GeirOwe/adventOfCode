#2019 day 2 Advent of Code
# source: https://adventofcode.com/2019/day/2

import os

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... AoC 2019 Day2 .... >')
    print()

def calc_result(num1, num2, opCode):
    if opCode == 1:
        result = num1 + num2
    elif opCode == 2:
        result = num1 * num2
    else:
        result = -1
    return result

#start function
def process_codes(codeList):
    #before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
    codeList[1] = 12
    codeList[2] = 2

    #set initial position
    # The address of the current instruction is called the instruction pointer
    # After an instruction finishes, the instruction pointer increases by the number of values in the instruction; 
    # until you add more instructions to the computer, this is always 4 (1 opcode + 3 parameters)
    currentPos = 0 
    cont = True
    part2ExpectedResult = 19690720
    while cont:
        #Opcodes (like 1, 2, or 99) mark the beginning of an instruction. 
        opCode = int(codeList[currentPos]) #find the opCode
        if opCode == 99:    #99 -> quit
            cont = False
        else:
            # The values used immediately after an opcode, if any, are called the instruction's parameters.
            pos1 = int(codeList[currentPos+1])
            pos2 = int(codeList[currentPos+2])
            pos3 = int(codeList[currentPos+3])
            result = calc_result(int(codeList[pos1]), int(codeList[pos2]), opCode) #process the two numbers in pos1 and pos2
            codeList[pos3] = result #store the processed result in third position

            #part2
            part2_quiz = 100 * pos1 + pos2
            if part2_quiz == part2ExpectedResult:
                print(pos1, pos2)
            
            # After an instruction finishes, the instruction pointer increases by the number of values in the instruction
            currentPos += 4 #move forward to next opCode

    return codeList[0]
#end function

def get_the_data():
    #read the test puzzle input 
    #intcodes_f = open('day22019_test_puzzle_input.txt', 'r')
    #read the puzzle input
    intcodes_f = open('day22019_puzzle_input.txt', 'r')
    #the codes are separated by comma - transfer them to a list
    codeList = intcodes_f.read().split(',')
    return codeList

#start function
def start_the_challenge():
    #get the data and read the into  list
    codeList = get_the_data()

    # Part 2 - With terminology out of the way, we're ready to proceed. To complete the gravity assist, 
    # you need to determine what pair of inputs produces the output 19690720.
    # Once the program has halted, its output is available at address 0, also just like before. Each time 
    # you try a pair of inputs, make sure you first reset the computer's memory to the values in the program 
    # (your puzzle input) - in other words, don't reuse memory from a previous attempt.
    # Find the input noun (pos2) and verb (pos3) that cause the program to produce the output 19690720

    #process the codes and return the answer
    valueAtPosZero = process_codes(codeList) 
    
    print('forventet resultat er ...  6730673 ...') 
    print('What value is left at position 0 after the program halts? - ', valueAtPosZero)

    return 
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_challenge()