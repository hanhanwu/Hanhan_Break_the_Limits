# Keystroke Mouse Behavioral Analysis

## Data Collection
Here to try difference languages to collect keystroke and mouse movement data, to compare and to find an optimal solution.
### Python Version
#### Collect Mouse Movement
* [My code - Using PyAutoGUI to record mouse movement][1]
  * [About PyAutoGUI][2]
  * It seems that the x, y collected here are all int, may lose accuracy
  * Most of the features in PyAutoGUI is to control the mouse (such as mouse up, mouse down, drag, etc.), keyboard, this can help write user behavoior simulation
  * But so far, it doesn't support more movement recording, such as mouse click
* [Pynput for mouse monitoring][3]
  * Not sure why, I used IPython and python terminal, none of them could give me any output...
  
### jQuery Version
Although I'm very bad at JS, jQuery is really great to record all these movements with high precision.
* [My code - Single field keystroke & mouse movement][4]
  * The data details are recorded in console, save console results into .txt file should be fine
  * Besides output the data in the console, in the code, it also pushes each keystroke (key up & key down) into a list. There are a few interesting findings:
    * If you press "Enter" to trigger the button, its keyup won't be recorded in the `tmr` list, but will appear in console. So better to use console to record the data you want to collect.
    * If you typed any special character, such as `&` = Shift + 7, if you simply record the event key, it will record "Shift" and "&", while the code for "&" and "7" are the same. So, it's better to record the event code or both, otherwise same key maybe recorded as different when you used Shift
  

[1]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/keystroke_mouse_behavioral_analysis/collect_mouse_movement_python.py
[2]:https://github.com/asweigart/pyautogui
[3]:https://pynput.readthedocs.io/en/latest/mouse.html#monitoring-the-mouse
[4]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/keystroke_mouse_behavioral_analysis/single_field_keystroke_mouse_move_jQuery.html
