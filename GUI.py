from collections import defaultdict
import fileinput
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from time import sleep
from threading import Thread
import sys
import os
import pickle

from src.util import *

numClicks = 0
projectName = ''
projectTime = ''
newProjectTime = ''
ONE_PROJECT_ERROR = 'Please select only one project!'

def fillListBox(listBox, projects):
    listBox.delete(0, END)
    for project in projects:
        if projects[project] != '':
            listBox.insert(END, '{}, {}'.format(project, projects[project]))

def save(listBox, projects):
    global oldProjectTime
    global newProjectTime
    global projectName

    projects[projectName] = newProjectTime

    fillListBox(listBox, projects)
    saveProjects(projects)

def count_time(time, listBox, projects):
    global numClicks
    global projectTime
    global newProjectTime

    actualTime = stringToSeconds(time.get())
    while numClicks % 2 != 0:
        sleep(1)
        if numClicks % 2 != 0:
            actualTime += 1
            time.set(secondsToString(actualTime))
    newProjectTime = secondsToString(actualTime)
    
    save(listBox, projects)

def increase_clicks(msg):
    global numClicks
    if msg != ONE_PROJECT_ERROR:
        numClicks += 1

def begin(listBox, msg, time, projects):
    global oldProjectTime
    global projectName
    global projectTime
    global numClicks

    if len(listBox.curselection()) != 1:
        msg.set(ONE_PROJECT_ERROR)
    else:
        msg.set('Timer time!')
        project = listBox.get(listBox.curselection()[0]).split(', ')
        if numClicks % 2 != 1:
            projectName = project[0]
            projectTime = project[1]
            time.set(projectTime)
        msg.set(projectName)

        x = Thread(target=lambda: count_time(time, listBox, projects), daemon=True)
        x.start()

def raise_frame(frame):
    frame.tkraise()

def insert_project(name, retFrame, listbox, projects):
    names = projects.keys()
    if not name in names:
        projects[name] = secondsToString(0)
        save(listbox, projects)
        raise_frame(retFrame)

def delete_project(listBox, projects, msg):
    try:
        projects.pop(listBox.get(listBox.curselection()[0]).split(', ')[0])
        fillListBox(listBox, projects)
        saveProjects(projects)
    except:
        msg.set('Could not remove element')

def main():
    projects = loadProjects()
    defaultMsg = 'Timer time!'
        
    root = Tk()
    root.geometry('300x200')
    root.title('Timber')
    root.iconbitmap('data\\clock.ico')
    
    selection = Frame(root)
    timing = Frame(root)
    list_mod = Frame(root)
    add_project = Frame(root)

    for frame in (selection, timing, list_mod, add_project):
        frame.grid(row=0, column=0, sticky='news')

    message = StringVar()
    time = StringVar()
    message.set(defaultMsg)
    font = Font(size=12)
    timeFont = Font(size=24)

    listyBoxy = Listbox(selection, font=font)
    listyBoxy.pack(side=LEFT)
    addButton = Button(selection, text="+", command=lambda: [raise_frame(add_project), message.set(defaultMsg)])
    addButton.pack(side=BOTTOM)
    delButton = Button(selection, text='-', command=lambda: [message.set(defaultMsg), delete_project(listyBoxy, projects, message)])
    delButton.pack(side=BOTTOM)
    fillListBox(listyBoxy, projects)

    Label(selection, textvariable=message, font=font).pack(side=TOP)

    frame = Image.open('data\\clock.gif', 'r')
    frame = frame.resize((100,100), Image.ANTIALIAS)
    frame = ImageTk.PhotoImage(frame)
    Button(selection, image=frame, command=lambda: [begin(listyBoxy, message, time, projects), increase_clicks(message.get()), raise_frame(timing), message.set(defaultMsg)]).pack(side=RIGHT)

    projectName = StringVar()
    Label(add_project, text="Project Name:").pack(side=TOP)
    Entry(add_project, textvariable=projectName).pack(side=LEFT)
    Button(add_project, text="+", command=lambda: [insert_project(projectName.get(), selection, listyBoxy, projects), message.set(defaultMsg)]).pack(side=LEFT)

    Label(timing, textvariable=message, font=font).pack(side=TOP)
    Label(timing, textvariable=time, font=timeFont).pack(side=LEFT)
    Button(timing, image=frame, command=lambda: [begin(listyBoxy, message, time, projects), increase_clicks(message.get()), raise_frame(selection), message.set(defaultMsg)]).pack(side=RIGHT)
    
    if projects == []:
        raise_frame(add_project)
    else:
        raise_frame(selection)
    
    root.mainloop()

if __name__ == '__main__':
    main()