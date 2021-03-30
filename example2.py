#!python3

""" 
pyautogui:
PyAutoGUI lets your Python scripts control the mouse and 
keyboard to automate interactions with other applications. 
The API is designed to be as simple. 
PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.
https://pyautogui.readthedocs.io/en/latest/index.html

Once we install it, we can explore some of the functionality available
in the pyautogui methods.  The documentation shows good information on 
a lot of the commands, but some of the methods that will be most useful
to us:

moveTo(x,y)
click()
click(x,y,clicks,interval,button) optional arguments can be included!
alert()
confirm()
prompt()
locateOnScreen() looks for an image on screen and returns the first instance (left, top, width, height)
locateAllOnScreen() looks for an image on screen and returns a tuple of instances
locateCenterOnScreen() looks for an image and returns the (x,y) of the first instance
    - check out the documentation for more information on the screen image locate methods
getpixel(x,y) returns the color of the pixel at a particular location

note: I find typing in "pyautogui" a lot to be quite time consuming, so will
usually assign a shorter name to the module.

A useful function is the "info" method to help gather information about
your screen

"""

import pyautogui as p 
import time


def clicker():
    time.sleep(2)
    i = 0
    buttonloc = p.locateCenterOnScreen("clickthis.png")
    if buttonloc is not None:    
        print("This button is at " + str(buttonloc))
    else:
        print("could not find it")
        exit()

    i = 0
    while True:
        i = i + 1
        if i >= 15:       
            break
        else:
            p.click(buttonloc)

def buyresearch():
    time.sleep(2)
    i = 0
    dataloc = p.locateCenterOnScreen("data1.png")
    if dataloc is not None:    
        print("This button is at " + str(dataloc))
    else:
        print("could not find it")
        exit()
    
    while True:
        if cantbuyloc == p.locateCenterOnScreen("cantbuy.png"):     
            break
        else:
            p.click(dataloc)

def clicker()
def buyresearch()