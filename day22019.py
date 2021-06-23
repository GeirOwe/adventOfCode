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

    #set iniial position
    currentPos = 0
    cont = True
    while cont:
        opCode = int(codeList[currentPos]) #find the opCode
        if opCode == 99:    #99 -> quit
            cont = False
        else:
            pos1 = int(codeList[currentPos+1])
            pos2 = int(codeList[currentPos+2])
            pos3 = int(codeList[currentPos+3])
            result = calc_result(int(codeList[pos1]), int(codeList[pos2]), opCode) #process the two numbers in pos1 and pos2
            codeList[pos3] = result #store the processed result in third position
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
    #get the data
    codeList = get_the_data()

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