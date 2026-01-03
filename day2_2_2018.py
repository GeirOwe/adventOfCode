# Day1 - 2018 Advent of code
# source: https://adventofcode.com/2018

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2018 Day 2, part 2 .... >')
    print()
    return

#loop thru data and look for 
#two words where only one char is different 
#ChatGPT version
def process_the_data_chatgpt(theData):
    for i in range(len(theData)):
        for j in range(i+1, len(theData)):
            differing_positions = [pos for pos, (a, b) in enumerate(zip(theData[i], theData[j])) if a!= b]
            if len(differing_positions) == 1:
                common_letters = [theData[i][pos] for pos in range(len(theData[i])) if pos not in differing_positions]
                return ''.join(common_letters)
   
    return "found none"   

#my own version with googling support
def process_the_data(theData):
    for id in theData:
        for idX in theData:
            diff_char = sum(char1 != char2 for char1, char2 in zip(idX, id))
            if diff_char == 1:
                answer = id + ' -> ', idX
                return answer

    return "found none"

def get_the_data():
    #read the test puzzle input 
    #theFile = open('day2_2_2018_test_puzzle_input.txt', 'r')
    theFile = open('day22018_puzzle_input.txt', 'r')

    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theFile:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)

    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer
    valueX = process_the_data(theData) 
    
    print('What letters are common between the two correct box IDs?  ->\n ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()