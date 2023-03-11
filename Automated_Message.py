# Import the modules
import time
import pyautogui

# Code

def SendMessage():
    time.sleep(10)
    text = open('message.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

SendMessage()
