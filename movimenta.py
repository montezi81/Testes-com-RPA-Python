import pyautogui
import time


# pyautogui.moveTo(1806,53,duration=2)

# print('O sistema funcionou !')

pyautogui.moveTo(1806,16,duration=2)

pyautogui.click()

pyautogui.moveTo(797,481,duration=2)

# Clicou no objeto por 200 x

for i in range (200):
    pyautogui.click()



