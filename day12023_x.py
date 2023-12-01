import re

def extract_real_digits(line):
    # Define a mapping of spelled-out digits to their corresponding numeric values
    digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    pattern = re.compile('|'.join(map(re.escape, digit_mapping.keys())))
    replace_function = lambda match: digit_mapping[match.group(0)]
    result_string = pattern.sub(replace_function, line)

    # Extract the first and last characters (digits) from the modified line
    first_digit = result_string[0]
    last_digit = result_string[-1]

    return first_digit, last_digit




def get_the_data():
    #read the test puzzle input like this if separated by comma
    theData = open('day12023_2_test_puzzle_input.txt', 'r')
    #theData = open('day12023_puzzle_input.txt', 'r')
    #move data into a list - read a line and remove lineshift
    data_list = []
    for element in theData:
        elementTrimmed = element.strip()
        data_list.append(elementTrimmed)

    return data_list

# Example usage with the provided calibration document
lines = get_the_data()

for line in lines:
    first_digit, last_digit = extract_real_digits(line)
    print(f"Original: {line}, First Digit: {first_digit}, Last Digit: {last_digit}")

