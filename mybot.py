
import pyautogui as p 
import time

#p.mouseInfo()

def clicker():
    time.sleep(1)
    i = 0
    buttonloc = p.locateCenterOnScreen("clickthis.png")
    if buttonloc is not None:    
        print("1This button is at " + str(buttonloc))
    else:
        print("clicker1 could not find it")

    i = 0
    while True:
        i = i + 1
        if i >= 76:       
            return
        else:
            p.click(buttonloc)

def buyresearch1():
    i = 0
    dataloc = p.click(x=100, y=232)
    if dataloc is not None:    
        print("2This button is at " + str(dataloc))
    else:
        print("2could not find it")
    while True:
        cantbuydataloc = p.locateCenterOnScreen("cantbuy.png")
        if cantbuydataloc is None:
            return
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    return
                else:
                    p.click(dataloc)

def buyhr1():
    i = 0
    hrloc = p.click(x=1327, y=239)
    if hrloc is not None:    
        print("3This button is at " + str(hrloc))
    else:
        print("3could not find it")
    while True:
        cantbuyhrloc = p.locateCenterOnScreen("cant40buy.jpg")
        if cantbuyhrloc is None:
            return
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    return
                else:
                    p.click(hrloc)

def buyupgrades():
    i = 0
    upgradeloc = p.click(x=1657, y=299)
    if upgradeloc is not None:    
        print("4This button is at " + str(upgradeloc))
    else:
        print("could not find it")
    
    while True:
        cantbuyupgradeloc = p.locateCenterOnScreen("cantbuyupgrade.jpg")
        if cantbuyupgradeloc is None:
            return
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    return
                else:
                    p.click(upgradeloc)

def buyresearch2():
    i = 0
    dataloc = p.click(x=95, y=297)
    if dataloc is not None:    
        print("2This button is at " + str(dataloc))
    else:
        print("could not find it")
    
    while True:
        cantbuydataloc = p.locateCenterOnScreen("cantbuy.png")
        if cantbuydataloc is None:
            return
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    return
                else:
                    p.click(dataloc)

def buyhr2():
    i = 0
    hrloc = p.click(x=1339, y=316)
    if hrloc is not None:    
        print("3This button is at " + str(hrloc))
    else:
        print("could not find it")
    
    while True:
        cantbuyhrloc = p.locateCenterOnScreen("cant40buy.jpg")
        if cantbuyhrloc is None:
            return
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    return
                else:
                    p.click(hrloc)

def buyresearch3():
    i = 0
    dataloc = p.click(x=88, y=369)
    if dataloc is not None:    
        print("2This button is at " + str(dataloc))
    else:
        print("could not find it")
    
    while True:
        cantbuydataloc = p.locateCenterOnScreen("cantbuy.png")
        if cantbuydataloc is None:
            return
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    return
                else:
                    p.click(dataloc)

def buyhr3():
    i = 0
    hrloc = p.click(x=1339, y=380)
    if hrloc is not None:    
        print("3This button is at " + str(hrloc))
    else:
        print("could not find it")
    
    while True:
        cantbuyhrloc = p.locateCenterOnScreen("cant40buy.jpg")
        if cantbuyhrloc is None:
            return
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    return
                else:
                    p.click(hrloc)

def buyresearch4():
    i = 0
    dataloc = p.click(x=96, y=447)
    if dataloc is not None:    
        print("2This button is at " + str(dataloc))
    else:
        print("4could not find it")
    
    while True:
        cantbuydataloc = p.locateCenterOnScreen("cantbuy.png")
        if cantbuydataloc is None:
            return
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    return
                else:
                    p.click(dataloc)


def buyhr4():
    i = 0
    hrloc = p.click(x=1339, y=467)
    if hrloc is not None:    
        print("3This button is at " + str(hrloc))
    else:
        print("could not find it")
    
    while True:
        cantbuyhrloc = p.locateCenterOnScreen("cant40buy.jpg")
        if cantbuyhrloc is None:
            return
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    return
                else:
                    p.click(hrloc)

def clicker2():
    i = 0
    buttonloc = p.locateCenterOnScreen("clickthis.png")
    if buttonloc is not None:    
        print("1This button is at " + str(buttonloc))
    else:
        print("clicker2 could not find it")

    i = 0
    while True:
        i = i + 1
        if i >= 101:       
            return
        else:
            p.click(buttonloc)

while True:
    clicker()
    buyresearch1()
    buyhr1()
    buyupgrades()
    buyresearch2()
    buyhr2()
    buyresearch3()
    buyhr3()
    buyresearch4()
    buyhr4()
    clicker2()