# Day4 - 2018 Advent of code
# source: https://adventofcode.com/2018
from datetime import datetime, timedelta
from collections import defaultdict

def parse_record(record):
    timestamp, action = record.split("] ")
    timestamp = datetime.strptime(timestamp[1:], "%Y-%m-%d %H:%M")
    return timestamp, action

def process_records(records):
    records.sort()
    
    guards_sleep = defaultdict(list)
    current_guard = None
    asleep_time = None
    
    for record in records:
        timestamp, action = parse_record(record)
        
        if "Guard" in action:
            current_guard = int(action.split()[1][1:])
        elif "falls asleep" in action:
            asleep_time = timestamp.minute
        elif "wakes up" in action:
            awake_time = timestamp.minute
            guards_sleep[current_guard].extend(range(asleep_time, awake_time))
    
    return guards_sleep

def get_the_data():
    #read the test puzzle input 
    #theFile = open('day42018_test_puzzle_input.txt', 'r')
    theFile = open('day42018_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theFile:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)
    
  
    # Defining a dict 
    #d = defaultdict(list) 
    #for i in range(5): 
    #    d[i].append(i) 
    #print("Dictionary with values as list:") 
    #print(d)
    #for i in range(5): 
    #    d[i].append(i+1)
    #print(d)

    return data_list

def strategy_1(guards_sleep):
    most_asleep_guard = max(guards_sleep, key=lambda guard: len(guards_sleep[guard]))
    most_asleep_minute = max(set(guards_sleep[most_asleep_guard]), key=guards_sleep[most_asleep_guard].count)
    
    return most_asleep_guard * most_asleep_minute

if __name__ == "__main__":
    # Your puzzle input (replace this with the actual input)
    puzzle_input = get_the_data()
    guards_sleep = process_records(puzzle_input)
    result = strategy_1(guards_sleep)
    print("The result for Strategy 1 is:", result)
