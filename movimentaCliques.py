import pyautogui

pyautogui.click(1808,18,duration=2)

pyautogui.moveTo(809,949, duration=2)

# Click personalizado
pyautogui.click(809,949, duration=1, interval=0.1, button='left', clicks=1000)
