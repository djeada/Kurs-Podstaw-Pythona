import pyautogui
import time
pyautogui.typewrite(['win'])
pyautogui.typewrite('paint')
pyautogui.typewrite(['enter'])
time.sleep(1)
pyautogui.doubleClick(-1100,550)
pyautogui.dragRel(300,0, 2)
pyautogui.dragRel(0,300, 2)

pyautogui.displayMousePosition()
doubleClick()
moveTo(x,y,seconds)
moveRel(x,y,seconds)
dragTo(x,y,seconds)
pyautogui.click(-1800,100)
pyautogui.typewrite('Hello')
pyautogui.typewrite(['enter'])
hotkey('ctr','c')





