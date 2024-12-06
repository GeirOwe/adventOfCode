# 2024 Advent of code
# source: https://adventofcode.com/2024

import os

def clear_console():
    os.system('clear')
    print('< .... AoC 2024 Day 5, part 1 .... >')
    print()
    return

#prepare the input as pairs ina dict
def parse_input(rules_input, updates_input):
    # Parse the ordering rules
    rules = []
    for line in rules_input:
        page1, page2 = map(int, line.split('|'))
        rules.append((page1, page2))

    # Parse the updates
    updates = []
    for line in updates_input:
        pages = list(map(int, line.split(',')))
        updates.append(pages)

    return rules, updates

#build a graph of the rules
def build_graph(rules):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for page1, page2 in rules:
        graph[page1].append(page2)
    
    return graph

def is_order_correct(update, graph):
    position = {page: idx for idx, page in enumerate(update)}
    
    for page in update:
        for neighbor in graph[page]:
            if neighbor in position and position[neighbor] < position[page]:
                return False
    return True

def check_updates(rules_input, updates_input):
    rules, updates = parse_input(rules_input, updates_input)
    graph = build_graph(rules)
    
    results = []
    for update in updates:
        if is_order_correct(update, graph):
            results.append(update)
    
    return results

#fetch the page ordering rules from the input file
def read_rules(theData):
    rules_input = []
    for row in theData:
        row = row.strip()
        if '|' in row: rules_input.append(row)

    return rules_input

#fetch the page updates from the input file
def read_updates(theData):
    updates_input = []   
    for row in theData:
        row = row.strip()
        if ',' in row: updates_input.append(row)
    return updates_input

#find the middle number in the list
def find_middle(the_list):
    n = len(the_list)
    result = the_list[n // 2]
    return result

def process_the_data(theData):
    totResult = 0
    # separate the page ordering rules and the page updates from the input file
    rules_input = read_rules(theData)
    updates_input = read_updates(theData)

    # check for page updates in the right order
    results = check_updates(rules_input, updates_input)

    #finr the middle numbr of each updated page
    for row in results:
        numb = find_middle(row)
        totResult += numb

    return totResult

def get_the_data():
    #read the test puzzle input 
    #theData = open('day5_2024_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day5_2024_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return the answer -> correct answer is: 12
    valueX = process_the_data(theData) 
    
    print('What do you get if you add up all of the results -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()