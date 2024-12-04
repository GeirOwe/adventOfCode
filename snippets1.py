'''code snippets - typically testing some code from Twitter and the net'''

import os

def clear_console():
    '''clear the console and start the programme'''
    os.system('clear')
    print('< .... Code snippets, part 1 .... >')
    print()

def list_comprehension():
    '''test out list comprehension'''
    # traditional variant - no list comprehension
    numbers = []
    for idx in range(10):
        #calculate and add the result as an item in the numbers list
        numbers.append(1 + idx ** 2)
    result_x = numbers
    # adding to a list with list comprehension
    numbers = [1 + idx ** 2 for idx in range(10)]
    result_y = numbers

    print('result without list comprehension: ', result_x)
    print('result   with  list comprehension: ', result_y, '\n')
    #print(max(result_x))

def grok_ai_api():
    # curl https://api.x.ai/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer xai-84gEtVWzKw2UHNhKKJLwtz4HWcUg3DEWO9OkNdREdTbBDm0hFAl7mObTWVectVHYIjweMteNndCU0QyE" -d '{
    # "messages": [
        # {
        #  "role": "system",
        #  "content": "You are a test assistant."
        # },
        # {
        #  "role": "user",
        #   "content": "Testing. Just say hi and hello world and nothing else."
        # }
        # ],
        #  "model": "grok-beta",
        #  "stream": false,
        #  "temperature": 0
        # }'
    return

def dict_stuff():
    # for more details on dict
    # https://www.perplexity.ai/search/how-do-i-process-a-dictionary-6tEUK4ZIQWSH9fgCBRgTcg
    my_dict = {"a": 1, "b": 2, "c": 3}
    for key in my_dict:
        print(key)
    return

def start_the_engine():
    '''the main function - where program logic starts'''
    print('Lift off!','\n')
    # test out list comprehension'''
    #list_comprehension()
    dict_stuff()
    print()
#end function

#let's start
if __name__ == '__main__':
    clear_console()
    start_the_engine()
