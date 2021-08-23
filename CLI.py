from os import system, name
import os
from time import sleep
import threading
import sys
import numpy
from tkinter import *
from src.util import *
import base64

from data.animationArrs import *

# global variables
stop_timer = False
currentSecs = 0

# display animation running in the background
def clear(animation):
    i = 0
    endStr = '                          \r'
    while(True):
        for frame in animation:
            print(frame, end=endStr)
            sleep(.5)
            system('cls')

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

def writeTable(projects):
    maxWidth = 0

    for project in projects:
        maxWidth = numpy.maximum(maxWidth, len(project))
    for name in projects.keys():
        maxWidth = numpy.maximum(maxWidth, len(name))
    headers = ['Title','Time(H:M:S)']
    for header in headers:
        maxWidth = numpy.maximum(maxWidth, len(header))
    
    maxWidth = maxWidth + 4
    
    table = ""
    try:
        projects.pop('')
    except:
        '''No blank project'''
    table += "+"
    for j in range(2):
        table += ("-" * maxWidth) + "+"
    table += "\n"
    line = "|"  
    for header in headers:
        length = maxWidth - len(header)
        line += header + (" " * length) + "|"
    line += "\n"
    table += line

    for project in projects.keys():
        table += "+"
        for j in range(2):
            table += ("-" * maxWidth) + "+"
        table += "\n"

        line = "|"  
        length = maxWidth - len(project)
        line += project + (" " * length) + "|"
        length = maxWidth - len(projects[project])
        line += projects[project] + (" " * length) + "|"

        line += "\n"
        table += line
    table += "+"
    for j in range(2):
        table += ("-" * maxWidth) + "+"
    table += "\n"

    print(table)


# time a program and submit it to a permanent log for later access
def main():
    global stop_timer

    data = loadProjects()
    writeTable(data)

    project = input("What project will you be working on today?")

    # if project doesn't exist in database, prompt the creation of a new one or go back
    if project not in data.keys():
        response = ''
        while response.lower() != 'n' and response.lower() != 'y':
            print(response.lower() != 'n' and response.lower() != 'y')
            response = input(project + ' not found, would you like to create it?(Y/N)\n')
        if response.lower() == 'n':
            print('Understandable, have a nice day')
            sys.exit()
        else:
            print('Creating {}...'.format(project))

    # create thread for animation
    x = threading.Thread(target=lambda: clear(multiline), daemon=True)
    x.start()
    # create thread for timer
    y = threading.Thread(target=runTimer, daemon=True)
    y.start()
    while True:
        if input() == 'q':
            stop_timer = True
            y.join()
            getMessage()
            print('Worked for: ' + secondsToString(currentSecs))

            f = open("records.txt", "w")

            # write the new data to the file
            previousTime = 0
            try:
                previousTime = stringToSeconds(data[project])
            except:
                print('No previous data')
            data[project] = secondsToString(currentSecs + previousTime)
            saveProjects(data)
            sys.exit()

if __name__ == "__main__":
    main()