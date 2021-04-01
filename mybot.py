
import pyautogui as p 
import time

p.mouseInfo()

#def clicker():
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

#def buyresearch():
time.sleep(2)
i = 0
dataloc = p.locateCenterOnScreen("data1.png", confidence=0.8)
if dataloc is not None:    
    print("2This button is at " + str(dataloc))
else:
    print("could not find it")
    exit()
    
while True:
    cantbuyloc = p.locateCenterOnScreen("cantbuy.png")
    if cantbuyloc is None:
        break
    else:
        i = 0
        while True:
            i = i + 1
            if i >= 5:       
                break
            else:
                p.click(dataloc)

time.sleep(2)
i = 0
hrloc = p.locateCenterOnScreen("hr40buy.png", confidence=0.8)
if hrloc is not None:    
    print("3This button is at " + str(hrloc))
else:
    print("could not find it")
    exit()
    
while True:
    cantbuyloc = p.locateCenterOnScreen("cantbuy.png")
    if cantbuyloc is None:
        break
    else:
        i = 0
        while True:
            i = i + 1
            if i >= 5:       
                break
            else:
                p.click(dataloc)

#(region=(101,298, 100, 100)
#(region=(108,243, 100, 100)
#(region=(104,260, 100, 150)