from os import system, name
from time import sleep
import threading
import sys

# global variables
closing = ""

# clear the output window
def clear():
    global closing
    i = 0

    while(True):
        i = i + 1
        if(i % 3 == 0):
            print('Working.')
        elif(i % 3 == 1):
            print('Working..')
        else:
            print('Working...')
        sleep(.5)

        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux
        else:
            _ = system('clear')

# time a program and submit it to a permanent log for later access
def main():
    global closing
    project = input("Hello! What project are you working on today?")
    # if project doesn't exist in database, prompt the creation of a new one or go back
    # if project does exist, access it's file and 
    print("Have fun working on " + project)

    x = threading.Thread(target=clear(), args=(None,))
    x.start()
    print('um')
    while closing != 'quit':
        closing = input('why')
        if closing == 'quit':
            print("Works")
            break
        else:
            print("Works")
    x.join()
    print("Done for today, but tomorrow will be a new!")

if __name__ == "__main__":
    main()