# advent of code 
# response to the challenge by geir owe
# day8 - challenge: https://adventofcode.com/2020/day/8

#start function
def get_all_instructions(boot_file):
    allInstruct = []
    #move all instructions in the boot file into a list
    for instruction in boot_file:
        instruction = instruction.strip()
        allInstruct.append(instruction)
    return allInstruct
#end get_all_instructions function

#start function
def check_if_about_to_loop(newPos, visitedPos, aboutToLoop):
    #check if the position for he instruction has been visited before
    #if so, we are about to loop
    theSet = set(visitedPos) 
    if newPos in theSet: 
        aboutToLoop = True
    else:
        visitedPos.append(newPos)       #store what position we are at; and validate aginst it later
    return visitedPos, aboutToLoop
#end check_if_about_to_loop function

#start function
def jump_around(theInstruction, currentPos, theAccumulator):
    #split at ' ' - the right part cotnains the jump " 
    # the left part contains the instruction
    splitInstr = theInstruction.split(' ')
    theAccContent = splitInstr[0].strip()
    theJump = int(splitInstr[1].strip())
    
    #nop stands for No OPeration - it does nothing. The instruction immediately below it 
    # is executed next
    if (theAccContent == 'nop'):                
        theJump = 1
    
    #check if the accumulator value is to be increased
    #if so, increase the accumulator and move to next line
    if theAccContent == 'acc':
        theAccumulator = theAccumulator + theJump
        theJump = 1                 #move on to next instruction

    #calculate new  position due to the jump
    newPos = currentPos + theJump
    if newPos < 0:                  # if this happen it is a bug in the puzle input
        newPos = 0
    return newPos, theAccumulator
#end jump_around function

#start function
def swap_next_relevant_instr(allInstructions, startingPoint):
    x = startingPoint
    while x < len(allInstructions):
        #keep the value that we swap - will be used if we have to swap back
        beforeSwap = x
        bsValue = allInstructions[x]
        #split at ' ' - the right part cotnains the jump " 
        # the left part contains the instruction
        splitInstr = allInstructions[x].split(' ')
        theAccContent = splitInstr[0].strip()
        theJump = splitInstr[1].strip()
        #check if this instruction is to be swapped - if not move to next instruction
        if theAccContent == 'jmp':
            allInstructions[x] = 'nop ' + theJump
            x = len(allInstructions)
        else:
            if theAccContent == 'nop':
                if (allInstructions[x] != 'nop +0'):        #jmp +0 is invalid
                    allInstructions[x] = 'jmp ' + theJump
                    x = len(allInstructions)
                else:
                    x = x +1
            else:
                x = x + 1      
    return allInstructions, beforeSwap, bsValue
#end function

#read the test puzzle input
#boot_file = open('day8_test_puzzle_input.txt', 'r')
#read the puzzle input
boot_file = open('day8_puzzle_input2.txt', 'r')

#the challenge:
# The moment the program tries to run any instruction a second time, you know it will never terminate.
# Run your copy of the boot code. Immediately before any instruction 
# is executed a second time, what value is in the accumulator?
aboutToLoop = False
atTheEnd = False
theAccumulator = 0
calcPos = []
didISwap = False

#get all instructions from boot file
allInstructions = get_all_instructions(boot_file)

#starting point is where to get back to if we loop
startingPoint = 0
beforeSwap = 0
bsValue = ''

newPos=0
#execute instructions until loop is detected
while (aboutToLoop != True) & (atTheEnd != True):
    #check if we are about to loop
    calcPos, aboutToLoop = check_if_about_to_loop(newPos, calcPos, aboutToLoop)
    if aboutToLoop:
        #reset and try again
        #first - swap back if a swap has been done
        if didISwap:
            allInstructions[beforeSwap] = bsValue
            startingPoint = startingPoint + 1
        
        #then - swap again in the next jmp / nop from where we are and forward
        allInstructions, beforeSwap, bsValue = swap_next_relevant_instr(allInstructions, startingPoint)
        startingPoint = beforeSwap 
        
        #reset the values and run all instructions again
        aboutToLoop = False
        theAccumulator = 0
        calcPos = []
        newPos=0
        didISwap = True
    else:
        #jump to position as specified in instruction and collect accumulator value when relevant
        currentPos = newPos
        #are we at the end of all instructions
        newPos, theAccumulator = jump_around(allInstructions[newPos], currentPos, theAccumulator)
        if newPos == len(allInstructions):
            print()
            print('all instructions executed without a loop.')
            print('... what value is in the accumulator? ', theAccumulator)
            print()
            print('... where we have been: ')
            print(calcPos)
            print()
            atTheEnd = True

