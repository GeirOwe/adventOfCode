# Day11 - 2022 Advent of code
# source: https://adventofcode.com/2022/day/11

import os
import numpy as np

def clear_console():
    os.system('clear')
    print('< .... AoC 2022 Day 11, part 1 .... >')
    print()
    return

#define a Monkey object
class Monkey():
    def __init__(self, id):
        self.id = id
        self.inspected_items = 0
        self.items = []
        self.throw_to = []
        return

    #get monkey id
    def get_id(self):
        return self.id
    #empty list of items
    def empty_list(self):
        self.items = []
    #worry level for item
    def add_item(self, worry_level):
        self.items.append(worry_level)
    def get_items(self):
        return self.items
    #operation -> e.g. old + 6 .. old * old
    def set_operation(self, ops):
        self.operation = ops
    def get_operation(self):
        return self.operation
    #test division -> Test: divisible by 5
    def set_test(self, divide):
        self.test = divide
    def get_test(self):
        return self.test
    #throw to monkey
    def set_throw_to(self, monkey):
        self.throw_to.append(monkey)
    def get_throw_to(self):
        return self.throw_to
    #count inspections
    def add_inspected(self):
        self.inspected_items += 1
    def get_inspected(self):
        return self.inspected_items

#end class definition

#fidn the two monkeys who inspected the most
def two_most_active(monkeys):
    valueX = 0
    inspected = []
    #check if the monkey has one of the two highest numbers
    for monkey in monkeys:
        inspected.append(monkey.get_inspected())

    #multiply the two highest numbers
    inspected.sort(reverse=True)
    valueX = inspected[0] * inspected[1]
    return valueX

#calc new worry level based on Operations. e.g. old + 7
def calc_new_wl(old_wl, ops):
    splitX = ops.split()
    if splitX[0].lower() == 'old': x = old_wl
    if splitX[2].lower() == 'old': y = old_wl
    else: y = int(splitX[2])
    #operation er pluss eller gange
    new_wl = 0
    if splitX[1] == '+': new_wl = x + y
    else: new_wl = x * y
    return new_wl

def do_round(monkeys):
    for monkey in monkeys:
        #inspect all itema
        items = monkey.get_items()
        for item in items:
            #inspect worry level of item -> i.e. the value
            old_wl = item
            # calc new worry level based on operation
            new_wl = calc_new_wl(old_wl, monkey.get_operation())
            # your worry level to be divided by three and rounded 
            # down to the nearest integer
            new_wl = new_wl // 3
            #check who to throw to
            throw_to = monkey.get_throw_to()
            if new_wl % monkey.get_test() == 0:
                #throw to monkey [0] -> monkey id
                id = throw_to[0]
            else:
                #throw to monkey [i] -> monkey id
                id = throw_to[1]
            
            # count that one insection has been done
            monkey.add_inspected()
            #throw to the the item's worry level to next monkey
            monkeys[id].add_item(new_wl)
        
        #empty the list after all hev been processed
        monkey.empty_list()

    return monkeys

def process_the_data(theData):
    monkeys = []
    for row in theData:
        #dont process empty rows
        if row != '':
            #create a list of monkeys (monkey objects)
            splitX = row.split()
            if splitX[0] == "Monkey":
                #create a Monkey object based on the monkey number
                id = int(splitX[1].strip(':'))
                monkey = Monkey(id)
                #add monkey object to list of monkeys 
                monkeys.append(monkey)
            if splitX[0] == "Starting":
                #add worry level for all items
                j = 2
                while j < len(splitX):
                    #add worry level for item
                    wl = int(splitX[j].strip(','))
                    monkey.add_item(wl)
                    j += 1
            if splitX[0] == "Operation:":
                #set operation instructions
                ops = splitX[3] + ' ' + splitX[4] + ' ' + splitX[5]
                monkey.set_operation(ops)
            if splitX[0] == "Test:":
                #set test instructions
                test = int(splitX[3])
                monkey.set_test(test)
            if splitX[0] == "If":
                #check if instructions, which monkey to throw to
                if splitX[1] == 'true': throw = int(splitX[5])
                else: throw = int(splitX[5])
                monkey.set_throw_to(throw)
                 
    return monkeys

def get_the_data():
    #read the test puzzle input 
    #theData = open('day112022_test_puzzle_input.txt', 'r')
    #read the puzzle input 
    theData = open('day112022_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        element = element.strip()
        data_list.append(element)
    return data_list

def start_the_engine():
    #get the data and read them into a list
    theData = get_the_data()
    
    #process the data and return a list of monkey objects from the input file
    monkeys = process_the_data(theData)

    #process 20 rounds
    j = 0
    while j < 20:
        monkeys = do_round(monkeys)
        j += 1

    # the two most active monkeys inspected items 101 and 105 times. 
    # The level of monkey business in this situation can be found by multiplying 
    # these together: 10605
    valueX = two_most_active(monkeys)
    print('The level of monkey business -> ', valueX,'\n') 
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()

