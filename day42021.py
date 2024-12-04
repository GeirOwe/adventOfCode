# Day4 - 2021 Advent of code
# source: https://adventofcode.com/2021/day/4

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2021 Day 4, part 1 .... >')
    print()
    return

def draw_number(numbers_drawn, pos):
    numberX = int(numbers_drawn[pos])
    return numberX

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

def check_for_bingo(numbers_drawn, theBoards, numOfBoards):
    board = 0
    boardWBingo = 0
    bingo = False
    #array (x, y, z) -> board, rows, columns -> : means all elements
    #print(theBoards[0, 4, :], " -> expect 5th row, in 1st board, all numbers -> 1 12 20 15 19")
    if len(numbers_drawn) > 4:
        while board < numOfBoards and bingo != True:
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
            
            if bingo:
                boardWBingo = board
                board += numOfBoards
            else:
                board += 1

    return bingo, boardWBingo

def sum_the_row(row, numbers_drawn):
    #array (x, y, z) -> board, rows, columns -> : means all elements
    #print(theBoards[0, 4, :], " -> expect 5th row, in 1st board, all numbers -> 1 12 20 15 19")
    pos = 0
    rowSum = 0
    while pos < 5:
        if row[pos] in numbers_drawn:
            rowSum = rowSum + 0
        else:
            rowSum = rowSum + int(row[pos])
        pos += 1
    return rowSum

def sum_unmarked(numbers_drawn, theBoards, board):
    sumX = 0
    #array (x, y, z) -> board, rows, columns -> : means all elements
    #print(theBoards[0, 4, :], " -> expect 5th row, in 1st board, all numbers -> 1 12 20 15 19")
    rowX = 0
    while rowX < 5:
        row = theBoards[board, rowX, :]
        rowSum = sum_the_row(row, numbers_drawn)
        rowX += 1
        sumX = sumX + rowSum
    return sumX

def process_the_data(theNumbers, the_boards, numOfBoards):
    bingo = False
    valueX = 42
    sumX = 0
    noDrawn = 0
    numbers_drawn = []

    while bingo != True or (noDrawn == len(theNumbers)):
        #draw a new number -> number X
        numberX = draw_number(theNumbers, noDrawn)
        noDrawn += 1
        numbers_drawn.append(numberX)
        
        #check for bingo -> bingo = True
        bingo, boardWBingo = check_for_bingo(numbers_drawn, the_boards, numOfBoards)

    if bingo:
        #find sum of all unmarked numbers -> sumX
        sumX = sum_unmarked(numbers_drawn, the_boards, boardWBingo)
        print("Bingo on board number: ", boardWBingo+1)
        #calculate result
        valueX = numberX * sumX

    return valueX

def split_the_data(theData):
    numbers_drawn = ""
    the_boards = []
    numOfBoards = int((len(theData) - 1) / 5)    
    i = 0
    for row in theData:
        if i == 0:
            #first row contains the number to draw for the bingo
            numbers_drawn = row.split(",")
        else:
            #remaining rows contains 5x5 sized boards
            rowList = row.split(" ")
            pos = 0 #the position in rowList
            z = 1 #to track that all 5 numberss have been moved into rowList
            while z <= 5:
                if rowList[pos] == "": #some numbers have several blanks between the numbers
                    pos += 1
                else:
                    #add numbers on the borad to along list - it will be reshaped into a 5x5 board in numpy array
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