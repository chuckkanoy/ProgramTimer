from os import system, name
from time import sleep
import threading
import sys

# clear the output window
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

# save progress to file
def close_up():
    print("Done for today, but tomorrow will be a new!")

# time a program and submit it to a permanent log for later access
def main():
    project = input("Hello! What project are you working on today?")
    # if project doesn't exist in database, prompt the creation of a new one or go back
    # if project does exist, access it's file and 
    print("Have fun working on " + project)
    x = threading.Thread(target=clear, daemon=True)
    x.start()

    while True:
        if input() == 'q':
            close_up()
            sys.exit()

if __name__ == "__main__":
    main()