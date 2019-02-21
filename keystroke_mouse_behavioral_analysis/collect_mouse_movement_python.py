import pyautogui
import time

starttime=time.time()
while True:
    print(pyautogui.position())
    time.sleep(3)
    if int(time.time() - starttime) % 20 == 1: # at 21 sec
        print('end')
        break
