import pyautogui

# with typewrite(), it will type the string automatically
pyautogui.typewrite("""The fox told the little prince, 'The most precious things are never visible.'""", interval=0.01)  # interval 0.01 sec

# The code below only works on Windows, not on Mac
## To see this work, you need terminal, IPython won't show the result
def press_star():
    pyautogui.keyDown('shift')
    pyautogui.keyDown('8')
    pyautogui.keyUp('8')
    pyautogui.keyUp('shift')
    
# To make Shift + 8 works on Mac
def press_star():
    pyautogui.hotkey("shift", "8")
