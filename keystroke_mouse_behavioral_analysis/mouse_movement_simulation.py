import pyautogui
import time


# Mouse - Move to
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150, duration=1)   # the duration here can define mouse move speed
time.sleep(2)
pyautogui.moveTo(100, 250, duration=1)
time.sleep(2)
pyautogui.moveTo(100, 350, duration=2)
time.sleep(2)
pyautogui.moveTo(200, 250, duration=1)


# Mouse - Drag to (if there's dragable web element, it will be dragged)
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.dragTo(100, 150, duration=1)   # the duration here can define mouse move speed
time.sleep(2)
pyautogui.dragTo(100, 250, duration=1)
time.sleep(2)
pyautogui.dragTo(100, 350, duration=2)
time.sleep(2)
pyautogui.dragTo(200, 250, duration=1)

pyautogui.rightClick(x=200, y=250)  # mouse click


# With mouse down, mouse up, you can simulate the 
pyautogui.mouseDown(x=200, y=250, button='right')  # mouse down
pyautogui.mouseUp(x=200, y=250, button='right')  # mouse up


pyautogui.scroll(-700, x=200, y=250)  # dind't see any effect
