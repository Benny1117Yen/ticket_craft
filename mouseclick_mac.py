import time
import pyautogui


time.sleep(1)
print('1s delay')
time.sleep(1)
print('1s delay')
time.sleep(1)
print('1s delay')
while True:
    pyautogui.press('esc')
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.press('esc')
    time.sleep(0.02)
    pyautogui.press('esc')
    time.sleep(0.02)
    pyautogui.press('esc')
    time.sleep(0.02)