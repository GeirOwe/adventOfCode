# Word Cloud
# by ChatGPT

import os
import matplotlib.pyplot as plt

#clear the console and start the programme
def clear_console():
    os.system('clear')
    print('< .... generating a fibonacci sequence .... >')
    print('  --------------------------------------------')
    print('(c) code by ChatGPT\n')

#start function
def process_data(points):
    fib_seq_list = []
    #generate fibonacci sequence
    fib = lambda n: n if n<= 1 else fib(n-1) + fib(n-2)
    fib_seq = (fib(i) for i in range(points))
    for x in fib_seq: 
        fib_seq_list.append(x)
    return fib_seq_list

def plot_data(fibonacci_sequence, points):
    # Lag x-aksen for plottet
    x = list(range(points))

    # Plot Fibonacci-sekvensen
    plt.plot(x, fibonacci_sequence, marker='o', linestyle='-')

    # Sett etiketter for aksene
    plt.xlabel('Posisjon i Fibonacci-sekvensen')
    plt.ylabel('Verdi')

    # Sett tittel for plottet
    plt.title('Fibonacci-sekvensen')

    # Vis plottet
    plt.show()
    return

def get_going():
    #process the data and return the answer
    points = int(input('hvor mange tall i fibonacci rekken: '))
    fib_sequence = process_data(points)

    plot_data(fib_sequence, points)
    return 

#let's start
if __name__ == '__main__':
    clear_console()
    get_going()