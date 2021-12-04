# Day4 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/4

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 4, part 2 .... >')
    print()
    return

def check_the_row(row, numbers_drawn):
    bingo = False
    #array (x, y, z) -> board, rows, columns -> : means all elements
    #print(theBoards[0, 4, :], " -> expect 5th row, in 1st board, all numbers -> 1 12 20 15 19")
    hit = 0
    pos = 0
    while pos < 5:
        if row[pos] in numbers_drawn:
            hit += 1
        pos += 1
    
    if hit ==5:
        bingo = True
    
    return bingo

def check_the_col(col, numbers_drawn):
    bingo = False
    #array (x, y, z) -> board, rows, columns -> : means all elements
    #print(theBoards[0, 4, :], " -> expect 5th row, in 1st board, all numbers -> 1 12 20 15 19")
    hit = 0
    pos = 0
    while pos < 5:
        if col[pos] in numbers_drawn:
            hit += 1
        pos += 1
    
    if hit ==5:
        bingo = True

    return bingo

def check_for_bingo(numbers_drawn, theBoards, numOfBoards, boardWBingo):
    board = 0
    bingo = False
    #array (x, y, z) -> board, rows, columns -> : means all elements
    #print(theBoards[0, 4, :], " -> expect 5th row, in 1st board, all numbers -> 1 12 20 15 19")
    if len(numbers_drawn) > 4:
        while board < numOfBoards and bingo != True and (len(boardWBingo) <= numOfBoards):
            if board in boardWBingo:
                bingo = False
            else:
                rowX = 0
                while rowX < 5 and bingo != True:
                    row = theBoards[board, rowX, :]
                    bingo = check_the_row(row, numbers_drawn)
                    rowX += 1
                colX = 0
                while colX < 5 and bingo != True:
                    col = theBoards[board, :, colX]
                    bingo = check_the_col(col, numbers_drawn)
                    colX += 1

            #in part two we are to look for the last board with bingo
            if bingo:
                boardWBingo.append(board)
                if (len(boardWBingo) == numOfBoards):
                    bingo = True
                else:
                    bingo = False
                    board = 0
            else:
                board += 1
    
    return bingo, boardWBingo

def sum_the_row(row, numbers_drawn):
    #summarize the unmarked numbers on the board
    #array (x, y, z) -> board, rows, columns -> : means all elements
    #print(theBoards[0, 4, :], " -> expect 5th row, in 1st board, all numbers -> 1 12 20 15 19")
    pos = 0
    rowSum = 0
    while pos < 5:
        #do not summarize if the number is matching a number drawn
        if row[pos] in numbers_drawn:
            rowSum = rowSum + 0
        else:
            rowSum = rowSum + int(row[pos])
        pos += 1
    return rowSum

def sum_unmarked(numbers_drawn, theBoards, board):
    #find the sum of all numbers of the board that is unmarked; i.e.no bingo hit for number
    sumX = 0
    #array (x, y, z) -> board, rows, columns -> : means all elements
    #print(theBoards[0, 4, :], " -> expect 5th row, in 1st board, all numbers -> 1 12 20 15 19")
    rowX = 0
    while rowX < 5:
        row = theBoards[board, rowX, :]
        rowSum = sum_the_row(row, numbers_drawn) #
        rowX += 1
        sumX = sumX + rowSum
    return sumX

def process_the_data(theNumbers, the_boards, numOfBoards):
    bingo = False
    valueX = 42
    sumX = 0
    noDrawn = 0 # how many bingo balls we have used
    numbers_drawn = []  # the list of all bingo balls numbers used
    boardWBingo = [] #used in part two - we are to find the last board
    noOfBingoBalls = len(theNumbers) #total number of balls available

    while bingo != True and (noDrawn < noOfBingoBalls):
        #draw a new number -> number X
        numberX = int(theNumbers[noDrawn])
        noDrawn += 1
        numbers_drawn.append(numberX) #add to the list og bingo balls used
        
        #check for bingo -> bingo = True
        bingo, boardWBingo = check_for_bingo(numbers_drawn, the_boards, numOfBoards, boardWBingo)

    if bingo:
        boardToCheck = boardWBingo[-1] # last board in list is the one to check
        #find sum of all unmarked numbers -> sumX
        sumX = sum_unmarked(numbers_drawn, the_boards, boardToCheck)
        print("The last board to get bingo: ", boardToCheck)
        print("Last bingo ball fetched: ", numberX)
        #calculate result
        valueX = numberX * sumX

    return valueX

def split_the_data(theData):
    #first row contains the number to draw for the bingo
    #remaining rows contains 5x5 sized boards. add numbers on the board to one long list
    # it will be reshaped into a 5x5 board in the numpy array
    numbers_drawn = ""
    the_boards = []
    numOfBoards = int((len(theData) - 1) / 5)    
    i = 0
    for row in theData:
        if i == 0:
            #first row contains the number to draw for the bingo
            numbers_drawn = row.split(",")
        else:
            #the boards - they are spaces between the numbers
            rowList = row.split(" ")
            pos = 0 #the position in rowList
            z = 1 #to track that all 5 numberss have been moved into rowList
            while z <= 5:
                if rowList[pos] == "": #some numbers have several blanks between the numbers
                    pos += 1
                else:
                    #add numbers on the board to along list - it will be reshaped into a 5x5 board in numpy array
                    the_boards.append(int(rowList[pos]))
                    pos += 1
                    z += 1       
        i += 1
    
    #move them into numpy arrays - to make it easier to process
    #array (x, y, z) -> board, rows, columns -> : means all elements
    #print(theBoards[0, 4, :], " -> expect 5th row, in 1st board, all numbers -> 1 12 20 15 19")
    the_boards = np.array(the_boards, dtype = "int").reshape(numOfBoards, 5, 5)
    numbers_drawn = np.array(numbers_drawn, dtype = "int")
    return numbers_drawn, the_boards, numOfBoards

def get_the_data():
    #read the test puzzle input 
    #theData = open('day42021_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day42021_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        if elementTrimmed != "":
            data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    numbers_drawn, the_boards, numOfBoards = split_the_data(theData)
    
    #process the data and return the answer
    valueX = process_the_data(numbers_drawn, the_boards, numOfBoards) 
    
    print('The score of the winning board -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()