import random
import os
import pickle

PROJECTS_PATH = 'data\\projects.pickle'

def loadProjects():
    if not os.path.exists(PROJECTS_PATH):
        with open(PROJECTS_PATH, 'wb') as f:
            pickle.dump({}, f, pickle.HIGHEST_PROTOCOL)
    with open(PROJECTS_PATH, 'rb') as f:
        projects = pickle.load(f)
    
    return projects

def saveProjects(projects):
    with open(PROJECTS_PATH, 'wb') as f:
        pickle.dump(projects, f, pickle.HIGHEST_PROTOCOL)

# display message based on random
def getMessage():
    messages = ['Another day, another dollar.', 'Great work today! Come back tomorrow (or don\'t, I\'m just a program)', 'Proud of you :)']
    print(messages[random.randint(0, len(messages) - 1)])

# convert seconds into string for writing to file
def secondsToString(seconds):
    hours = int(seconds / (60*60))
    min = int((seconds - (hours * 60 * 60)) / 60)
    seconds = int((seconds - ((min * 60) + (hours * 60 * 60))))
    return (str(hours).zfill(2) + ":" + str(min).zfill(2) + ":" + str(seconds).zfill(2))

# convert string to seconds
def stringToSeconds(string):
    secHolder = string.split(":")
    seconds = int(secHolder[0]) * 60 * 60 + int(secHolder[1]) * 60 + int(secHolder[2])
    return seconds