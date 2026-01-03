import re

def extract_first_last_digits(string):
    # Use regular expression to find all digits in the string
    digits = re.findall(r'\d', string)
    
    if digits:
        # Return the first and last digits
        return int(digits[0]), int(digits[-1])
    else:
        # Return None if no digits are found
        return None, None

# Example list of strings
string_list = ["abc123def456", "xyz789", "abc1xyz2"]

# Extract first and last digits from each string
for string in string_list:
    first_digit, last_digit = extract_first_last_digits(string)
    print(f"String: {string}, First Digit: {first_digit}, Last Digit: {last_digit}")
