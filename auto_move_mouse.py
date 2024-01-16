# Auto Move Mouse
# Window size W35 x H8
# Window position L1580 x T950
# Blank let system position window

import os
import pyautogui as pg
import time

def count():
    for c in range(0, 721):
        print("Move!!")
        pg.moveTo(1700, 525, duration = 0.2)
        pg.moveTo(1695, 520, duration = 0.2)
        pg.moveTo(1700, 525, duration = 0.2)
        pg.click(1700, 525)
        os.system("cls")
        print("Keep Screen On :", c, end="")
        print(" min.")
        time.sleep(60)       
    print("Stop!!")
    
print("""Move My Mouse Every 1 Minute
Program will be started in 15 sec.""")
time.sleep(15)
print("Start!!")
count()
print("Total 12 Hours, Please Turn Your Device Off.")

#End