from os import system, name
from time import sleep
import threading
import sys
import datetime
import random

# display animation running in the background
def clear():
    i = 0
    while(True):
        i = i + 1
        if(i % 5 == 1):
            print('Working|')
        elif(i % 5 == 2):
            print('Working/')
        elif(i % 5 == 3):
            print('Working-')
        else:
            print('Working\\')
            i = 0
        sleep(.5)
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux
        else:
            _ = system('clear')

# display message based on random
def getMessage():
    messages = ['Another day, another dollar.', 'Great work today! Come back tomorrow (or don\'t, I\'m just a program)', 'Proud of you :)']
    print(messages[random.randint(0, len(messages))])

# time a program and submit it to a permanent log for later access
def main():
    project = input("Hello! What project are you working on today?\n")
    flag = True

    # if project doesn't exist in database, prompt the creation of a new one or go back
    f = open('records.txt', 'r')
    for line in f:
        if line.split()[1] == project:
            flag = False
    f.close()
        
    if(flag):
        response = input(project + 'not found, would you like to create it?(Y/N)\n')

    if response.lower == 'n':
        print('Understandable, have a nice day')
        sys.exit()

    # if project does exist, access it's file and 
    

    # create thread for animation
    x = threading.Thread(target=clear, daemon=True)
    x.start()

    # grab initial time
    start_time = datetime.datetime.now()

    while True:
        if input() == 'q':
            getMessage()
            end_time = datetime.datetime.now()
            finishing_time = end_time - start_time
            print('Worked for: ' + str(finishing_time))
            # f = open("records.txt", "w")
            # for line in f:
            #     if line.split()[1] == project:

            sys.exit()

if __name__ == "__main__":
    main()