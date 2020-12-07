# advent of code by geir owe
# day5
# link to the challenge: https://adventofcode.com/2020/day/5

import math

#find the lower half in the range - divide and round down
def go_lower_half(lRow):
    result = int(lRow / 2)
    return result

#find the upper half half in the range - divide and round up
def go_upper_half(lRow):
    result = math.ceil(lRow / 2)
    return result

# start function
def find_row(bPass):
    pos = 1
    fromRow = 0
    toRow = 127
    for letter in bPass:
        #only the first seven letters are sed to find the row
        if pos <= 7:
            if letter.upper() == 'F':
                #F means to take the lower half of he current range
                toRow = (go_lower_half(toRow - fromRow)) + fromRow
            else:
                #F means to take the upper half of he current range
                fromRow = (go_upper_half(toRow - fromRow)) + fromRow
        pos = pos + 1
    theRow = fromRow
    return theRow
# end find_row function

# start fucntion
def find_seat(bPass):
    pos = 1
    fromSeat = 0
    toSeat = 7
    for letter in bPass:
        #only the first seven letters are sed to find the row
        if pos > 7:
            if letter.upper() == 'L':
                #F means to take the lower half of he current range
                toSeat = (go_lower_half(toSeat - fromSeat)) + fromSeat
            else:
                #F means to take the upper half of he current range
                fromSeat = (go_upper_half(toSeat - fromSeat)) + fromSeat
        pos = pos + 1
    theSeat = fromSeat
    return theSeat
# end find_row function


#read the test puzzle input
#bpass_file = open('day5_test_puzzle_input.txt', 'r')
#read the puzzle input
bpass_file = open('day5_puzzle_input.txt', 'r')

#the challenge:
#As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
maxSeatId = 0

#read the passports from the file
for bPass in bpass_file:
    bPass = bPass.strip()
   
    #find the row
    theRow = find_row(bPass)
    
    #find the seat
    theSeat = find_seat(bPass)

    #calculate the seat id
    seatId = theRow * 8 + theSeat
    if seatId > maxSeatId:
        maxSeatId = seatId
        print(bPass, ' equals row: ', theRow, ' and seat: ', theSeat, ' and seat ID: ', seatId)  

#the challenge:
print('the highest seat ID on a boarding pass? ', maxSeatId)
    