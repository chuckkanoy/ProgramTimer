from os import system, name
import os
import time
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
    print(messages[random.randint(0, len(messages) - 1)])

# time a program and submit it to a permanent log for later access
def main():
    project = input("Hello! What project are you working on today?\n")
    flag = True
    storage = []
    index = 0
    count = 0

    # if project doesn't exist in database, prompt the creation of a new one or go back
    f = open('records.txt', 'r')
    for line in f:
        # check to see if the size of the file is zero
        if os.path.getsize("records.txt") != 0:
            storage.append(line)
            print(line.split(',')[0])
            if line.split(',')[0] == project:
                index = count
                flag = False
            count = count + 1
        else:
            flag = True
    
    # handle when no record is found
    if(flag):
        response = input(project + 'not found, would you like to create it?(Y/N)\n')
        if response.lower == 'n':
            print('Understandable, have a nice day')
            sys.exit()
        storage.append(project + "," + str(time.timedelta(0, 0, 0)))

    # if project does exist, access it's file and 
    
    print(str(datetime.timedelta(0,0,0)))
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
            f = open("records.txt", "w")

            # write the new data to the file
            for line in storage:
                print(line.split(','))
                # modify old value and write it to file
                if line.split(',')[0] == project:
                    line = project + "," + str(finishing_time + time.strptime(int(line.split(',')[1]), "%H:%M:%S").replace("\n","")) + "\n"
                f.write(line)
            f.close()
            sys.exit()

if __name__ == "__main__":
    main()