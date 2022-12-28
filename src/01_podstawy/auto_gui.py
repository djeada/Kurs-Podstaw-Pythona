import pyautogui
import time

# pyautogui.displayMousePosition()

"""
pyautogui.click(-110, 48)
pyautogui.click(-1344, 1326)
"""

pyautogui.typewrite(["win"])
pyautogui.typewrite("paint")
time.sleep(1)
pyautogui.typewrite(["enter"])
time.sleep(1)
pyautogui.click(-1100, 500)
pyautogui.dragRel(300, 0, 2)
pyautogui.dragRel(0, 300, 2)
