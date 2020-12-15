# advent of code 
# response to the challenge by geir owe
# day9 - challenge: https://adventofcode.com/2020/day/9

#start function
def get_all_port_data(port_file):
    codeList = []
    #move all instructions in the boot file into a list
    for code in port_file:
        code = int(code.strip())
        codeList.append(code)
    return codeList
#end get_all_port_data function

#start function
def check_the_number(codeList, startPos, endPos, theNumber):
    inList = False
    checkNext = True
    thisPos = startPos
    nextPos = thisPos + 1
    
    #check if the number is the sum of to elements in list
    while checkNext:
        calcResult = codeList[thisPos] + codeList[nextPos]
        #if the number is the sum of the two elements, then we are done
        if calcResult == theNumber:
            inList = True
            checkNext = False
        else:
            #keep this position fixed and loop thru the rest of the list
            nextPos = nextPos + 1
            moveToNextItem = True
            while moveToNextItem:
                calcResult = codeList[thisPos] + codeList[nextPos]
                #if the number is the sum of the two elements, then we are done
                if calcResult == theNumber:
                    inList = True
                    checkNext = False
                    moveToNextItem = False
                else:
                    nextPos = nextPos + 1
                    #when at the end of the list; start from top again by moving to 
                    # next item in list; unless we are the end; then we are done
                    if nextPos > endPos:
                        thisPos = thisPos + 1
                        nextPos = thisPos + 1
                        moveToNextItem = False
                        if thisPos == endPos:
                            checkNext = False

    return inList
#end get_all_port_data function


#start function
def find_the_number(codeList, preambleLength):
    #the part of the codelist to check 
    startPos = 0
    endPos = preambleLength - 1
    thePosToCheck = endPos + 1
    itemsInList = len(codeList)

    theNumber = codeList[thePosToCheck]
    moreItems = True
    
    inList = check_the_number(codeList, startPos, endPos, theNumber)
    while (inList) & (moreItems):
        # move to next number and check if there exist
        # two numbers that sumarize to that number
        startPos = startPos + 1
        endPos = endPos + 1
        thePosToCheck = endPos + 1
        theNumber = codeList[thePosToCheck]
        inList = check_the_number(codeList, startPos, endPos, theNumber)
        
        #check if we are at the end - i.e. the item is not in the list
        if endPos == (itemsInList - 1):
            moreItems = False
            
    return theNumber
#end function

#read the test puzzle input
#port_file = open('day9_test_puzzle_input.txt', 'r')
#thePreamble = 5
#read the puzzle input
port_file = open('day9_puzzle_input.txt', 'r')
thePreamble = 25

#move all codes into a list
codeList = get_all_port_data(port_file)

#the challenge:
# find the first number in the list (after the preamble) which is not 
# the sum of two of the 25 numbers before it. 
# What is the first number that does not have this property?
theNumber = 0
theNumber = find_the_number(codeList, thePreamble)

print('the first number in the list which is not the sum of two of the x numbers before it is: ', theNumber)
