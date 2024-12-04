# Day6 - 2023 Advent of code

import os
import re

def clear_console():
    os.system('clear')
    print('< .... AoC 2023 Day 7, part 1 .... >')
    print()
    return

def pairing(row):
    hand, bid = row.split()
    return hand, bid 

def check_hand(hand):
    fives = 0
    fours = 0
    threes = 0
    twos = 0
    single = 0
    house = 0
    tress = 0
    twopair = 0
    pair = 0
    hand_dict = {
            'fives' : 0,
            'fours' : 0,
            'house' : 0,
            'tress' : 0,
            'twopair' : 0,
            'pair' : 0,
            'single' : 0
    }
    #hand is list -> ['A', 'J', 'QQQ']
    for combinations in hand:
        if len(combinations) == 5: type = 7
        if len(combinations) == 4: type = 6
        if len(combinations) == 3: threes += 1
        if len(combinations) == 2: twos += 1
        if len(combinations) == 1: single += 1
    if threes == 1 and twos == 1: 
        house = 1
        type = 5
    else:
        if threes == 1: 
            type = 4
        else:
            if twos == 2:
                type = 3
            else:
                if twos == 1:
                    type = 2
                else:
                    type = 1

    return type

def process_the_data(theData):
    #set initial position for the dataset
    valueX = 42
    hand_l = []
    bid_l = []
    rank = []
    #split into hand and bid
    for row in theData:
        hand, bid = pairing(row) 
        hand_l.append(hand)
        bid_l.append(bid)
    #play
    noOfHands = len(theData)
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    i = 0
    while i < noOfHands:
        #type = [list(g) for k, g in groupby(hands_l[i])]
        #matches any single character (.) and then its repetitions (\1*) if any.
        matcher= re.compile(r'(.)\1*')
        thisHand = ''.join(sorted(hand_l[i]))
        hand = [match.group() for match in matcher.finditer(thisHand)]
        type = check_hand(hand)
        rank_item = []
        rank_item.append(i) #hand
        rank_item.append(type) #type
        rank.append(rank_item)
        #next hand
        i += 1
    
    #sort on type
    rank.sort(key = lambda x: x[1], reverse = True)
    #ok so we have a sorted list.
    # next is to rank those with the same type
    # So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger 
    # because its first card is stronger. Similarly, 77888 and 77788 are 
    # both a full house, but 77888 is stronger because its third card is stronger
    return valueX

def get_the_data():
    #read the test puzzle input 
    theData = open('day72023_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    #theData = open('day72023_puzzle_input.txt', 'r')
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
    
    print('What are the total winnings? -> ', valueX,'\n') 
    return

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()