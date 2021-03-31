import pyautogui as p 
import time


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
    
i = 0
while True:
    i = i + 1
    if i >= 15:       
        break
    else:
        p.click(dataloc)

