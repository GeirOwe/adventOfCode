# Word Cloud
# by ChatGPT

import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... generating a wordcloud from a txt file .... >')
    print('  --------------------------------------------')
    print('(c) code by ChatGPT\n')

#start function
def process_data(theData):
    #opprett wordcloud
    cloud = WordCloud(width=800, height=400, background_color='white').generate(theData)
    return cloud

def show_wordcloud(cloud):
    plt.figure(figsize=(10, 5))
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    return

def get_the_data():
    with open('some_text.txt', 'r', encoding='utf-8') as file:
        theData = file.read()
    return theData

def start_NexUs():
    #get the data
    theData = get_the_data()
    #process the data and return the answer
    cloud = process_data(theData)

    #vis wordcloud
    show_wordcloud(cloud)

    return 

#let's start
if __name__ == '__main__':
    clear_console()
    start_NexUs()