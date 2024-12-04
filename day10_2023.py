# Day8 - 2023 Advent of code

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 10, part 1 .... >')
    print()
    return

def create_matrix(theData):
    matrix = []
    for row in theData:
        x = list(row)
        matrix.append(x)
    return matrix

def find_start(theData):
    # S indicated the start position
    r = 0
    c = 0
    for row in theData:
        #check the column of S if in row
        if 'S' in row: 
            colNo = row.index('S')
            rowNo = r
            break
        # next row
        r += 1

    return rowNo, colNo

def move_on(matrix, r, c, steps):
    #set initial position for the dataset
    #print('F: row + 1 eller col + 1')
    #print('7: row + 1 eller col - 1')
    #print('J: row - 1 eller col - 1')
    #print('L: row - 1 eller col + 1')
    #print('|: row + 1 eller row - 1')
    #print('-: col + 1 eller col - 1')
    #print('. ground move other way')
    cell = matrix[r][c]
    #F?
    if cell == 'F':
        #mark that cell has been visited
        if cell != 'S': matrix[r][c] = '*'
        if matrix[r][c+1] != '.' and matrix[r][c+1] != '*':
            #check that we are not going back to the 'S'
            if matrix[r][c+1] == 'S' and steps < 2:
                #move down
                r += 1
            else:            
                #move right
                c += 1
        else:
            #move down
            r += 1 
     
    #7?
    if cell == '7':
        #mark that cell has been visited
        matrix[r][c] = '*'
        if matrix[r+1][c] != '.' and matrix[r+1][c] != '*':
            #check that we are not going back to the 'S'
            if matrix[r+1][c] == 'S' and steps < 2:
                #move left
                c -= 1 
            else:
                #move down
                r += 1
        else:
            #move left
            c -= 1 

    #J?
    if cell == 'J':
        #mark that cell has been visited
        matrix[r][c] = '*'
        if matrix[r-1][c] != '.' and matrix[r-1][c] != '*':
            #check that we are not going back to the 'S'
            if matrix[r-1][c] == 'S' and steps < 2:
                #move left
                c -= 1 
            else:             
                #move up
                r -= 1
        else:
            #move left
            c -= 1 

    #L?
    if cell == 'L':
        #mark that cell has been visited
        matrix[r][c] = '*' 
        if matrix[r-1][c] != '.' and matrix[r-1][c] != '*':
        #check that we are not going back to the 'S'
            if matrix[r-1][c] == 'S' and steps < 2:
                #move right
                c += 1
            else: 
                #move up
                r -= 1
        else:
            #move right
            c += 1 
   
    #|?
    if cell == '|':
        #mark that cell has been visited
        matrix[r][c] = '*'
        if matrix[r-1][c] != '.' and matrix[r-1][c] != '*':
            #check that we are not going back to the 'S'
            if matrix[r-1][c] == 'S' and steps < 2:
                #move down
                r += 1
            else: 
                #move up
                r -= 1
        else:
            #move down
            r += 1 

    #-?
    if cell == '-':
        #mark that cell has been visited
        matrix[r][c] = '*'
        if matrix[r][c+1] != '.' and matrix[r][c+1] != '*':
        #check that we are not going back to the 'S'
            if matrix[r][c+1] == 'S' and steps < 2:
                #move left
                c -= 1 
            else: 
                #move right
                c += 1
        else:
            #move left
            c -= 1 
    
    steps += 1
    
    return r, c, steps

def test_this_variant(matrix, r, c, steps_list, startRow, startCol):
    steps = 1
    cont2Move = True
    while cont2Move:
        r, c, steps = move_on(matrix, r, c, steps)

        #back at start?
        if r == startRow and c == startCol: cont2Move = False

    steps_list.append(steps // 2)
    return steps_list

def process_the_data(theData):
    #find start; row and col
    startRow, startCol = find_start(theData)
    r = startRow
    c = startCol
    # move theData into a list of lists
    matrix = create_matrix(theData)
    startMatrix = create_matrix(theData)

    steps_list = []
    #test all 4 directions from start pos
    maxCols = len(matrix[0])
    maxRows = len(theData)
    #right
    if c < maxCols: 
        c += 1
        if matrix[r][c] != '.':
            steps_list = test_this_variant(matrix, r, c, steps_list, startRow, startCol)
        c = startCol
        matrix = startMatrix
    #left
    if c > 0: 
        c -= 1
        if matrix[r][c] != '.':
            steps_list = test_this_variant(matrix, r, c, steps_list, startRow, startCol)
        c = startCol
        matrix = startMatrix
    #down
    if r < maxRows: 
        r += 1
        if matrix[r][c] != '.':
            steps_list = test_this_variant(matrix, r, c, steps_list, startRow, startCol)
        r = startRow
        matrix = startMatrix
    #up
    if r > 0: 
        r -= 1
        if matrix[r][c] != '.':
            steps_list = test_this_variant(matrix, r, c, steps_list, startRow, startCol)
        r = startRow
        matrix = startMatrix

    #find highest value in steps list
    steps_list = sorted(steps_list)
    return steps_list[-1]

def get_the_data():
    #read the test puzzle input 
    #theData = open('day102023_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day102023_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 1856459736
    valueX = process_the_data(theData) 
    
    print('What is the sum of these extrapolated values? -> ', valueX,'\n') 
    return

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()