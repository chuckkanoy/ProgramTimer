from os import system, name
import os
import time
from time import sleep
import threading
import sys
import datetime
import random
import numpy

# global variables
stop_timer = False
currentSecs = 0

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

# convert seconds into string for writing to file
def secondsToString(seconds):
    hours = int(seconds / (60*60))
    min = int((seconds - (hours * 60 * 60)) / 60)
    seconds = int((seconds - ((min * 60) + (hours * 60 * 60))))
    return (str(hours) + ":" + str(min) + ":" + str(seconds))

# convert string to seconds
def stringToSeconds(string):
    secHolder = string.split(":")
    seconds = int(secHolder[0]) * 60 * 60 + int(secHolder[1]) * 60 + int(secHolder[2])
    return seconds

# run timer in background via threading
def runTimer():
    global currentSecs

    while True:
            sleep(1)
            currentSecs = currentSecs + 1
            if stop_timer:
                break

def convertRecords():
    storage = []
    lineNum = 0
    f = open('records.txt', 'r')

    if os.path.getsize('records.txt') != 0:
        for line in f:
            line = line.replace("\n", "")
            storage.append(line.split(","))
            lineNum+=1
    
    return storage

def writeTable(listArr):
    maxWidth = 0

    for i in range(len(listArr)):
        for j in range(len(listArr[i])):
            maxWidth = numpy.maximum(maxWidth, len(listArr[i][j]))
    
    maxWidth = maxWidth + 4
    
    table = ""
    for i in range(len(listArr)):
        table += "+"
        for j in range(len(listArr[i])):
            table += ("-" * maxWidth) + "+"
        table += "\n"

        line = "|"  
        for j in range(len(listArr[i])):
            length = maxWidth - len(listArr[i][j])
            line += listArr[i][j] + (" " * length) + "|"
        line += "\n"
        table += line
    table += "+"
    for j in range(len(listArr[len(listArr) - 1])):
        table += ("-" * maxWidth) + "+"
    table += "\n"

    print(table)


# time a program and submit it to a permanent log for later access
def main():
    global stop_timer

    # open the file and check for records
    try:
        f = open('records.txt', 'r')
        data = convertRecords()
        writeTable(data)
    except(FileNotFoundError):
        f = open('records.txt', 'x')
        f.write("Title,Time(H:M:S)\n")

    project = input("Hello! What project are you working on today?\n")
    flag = True
    storage = []

    f = open('records.txt', 'r')

    lineCount = 0
    for line in f:
        storage.append(line)
        # check to see if the size of the file is zero
        if os.path.getsize("records.txt") != 0:
            if line.split(',')[0] == project and lineCount != 0:
                flag = False
        else:
            flag = True
        lineCount += 1
    
   # if project doesn't exist in database, prompt the creation of a new one or go back
    if(flag):
        response = input(project + ' not found, would you like to create it?(Y/N)\n')

        if response.lower() == 'n':
            print('Understandable, have a nice day')
            sys.exit()
        storage.append(project + ",0:0:0")

    # create thread for animation
    x = threading.Thread(target=clear, daemon=True)
    x.start()
    # create thread for timer
    y = threading.Thread(target=runTimer)
    y.start()

    while True:
        if input() == 'q':
            stop_timer = True
            y.join()
            getMessage()
            print('Worked for: ' + secondsToString(currentSecs))

            f = open("records.txt", "w")

            # write the new data to the file
            for line in storage:
                # modify old value and write it to file
                if line.split(',')[0] == project:
                    previousTime = stringToSeconds(line.split(',')[1])
                    newTime = secondsToString(currentSecs + previousTime)
                    line = project + "," + newTime + "\n"
                f.write(line)
            f.close()
            sys.exit()

if __name__ == "__main__":
    main()