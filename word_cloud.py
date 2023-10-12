# Word Cloud
# by ChatGPT

import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... generating a wordcloud from a txt file .... >')
    print('  --------------------------------------------')
    print('(c) code by ChatGPT\n')

#start function
def process_data(theData):
    #opprett wordcloud
    cloud = WordCloud(width=800, height=400, background_color='white', max_words=20).generate(theData)
    return cloud

def show_wordcloud(cloud):
    plt.figure(figsize=(10, 5))
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    return

def get_the_data():
    tekst = ''
    with open('some_text.txt', 'r', encoding='utf-8') as file:
        for linje in file:
            tekst += linje.strip()
    return tekst

def get_going():
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
    get_going()