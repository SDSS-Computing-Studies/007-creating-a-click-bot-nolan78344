
import pyautogui as p 
import time

p.mouseInfo()

def clicker():
    time.sleep(2)
    i = 0
    buttonloc = p.locateCenterOnScreen("clickthis.png")
    if buttonloc is not None:    
        print("1This button is at " + str(buttonloc))
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
    dataloc = p.locateCenterOnScreen("data1.png", confidence=0.8, region=(104,260, 100, 150))
    if dataloc is not None:    
        print("2This button is at " + str(dataloc))
    else:
        print("could not find it")
        exit()
    
    while True:
        cantbuydataloc = p.locateCenterOnScreen("cantbuy.png", region=(104,260, 100, 100))
        if cantbuydataloc is None:
            break
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    break
                else:
                    p.click(dataloc)

def buyhr():
    time.sleep(2)
    i = 0
    hrloc = p.locateCenterOnScreen("hr40buy.jpg", confidence=0.8, region=(1313,313, 50, 150))
    if hrloc is not None:    
        print("3This button is at " + str(hrloc))
    else:
        print("could not find it")
        exit()
    
    while True:
        cantbuyhrloc = p.locateCenterOnScreen("cant40buy.jpg", region=(1313,313, 50, 50))
        if cantbuyhrloc is None:
            break
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    break
                else:
                    p.click(hrloc)

def buyupgrades():
    time.sleep(2)
    i = 0
    upgradeloc = p.locateCenterOnScreen("buyupgrades.jpg", confidence=0.8, region=(1658,294, 50, 150))
    if upgradeloc is not None:    
        print("4This button is at " + str(upgradeloc))
    else:
        print("could not find it")
        exit()
    
    while True:
        cantbuyupgradeloc = p.locateCenterOnScreen("cantbuyupgrade.jpg", region=(1658,294, 50, 50))
        if cantbuyupgradeloc is None:
            break
        else:
            i = 0
            while True:
                i = i + 1
                if i >= 5:       
                    break
                else:
                    p.click(upgradeloc)
a = 0
while (a<10):
    a = a + 0
    def clicker():
        def buyresearch():
            def buyhr():
                def buyupgrades():