import pyautogui
import time


screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
time.sleep(5)
pyautogui.moveTo(100, 250)
time.sleep(5)
pyautogui.moveTo(100, 350)
time.sleep(5)
pyautogui.moveTo(200, 250)

# TO BE CONTINUED....
