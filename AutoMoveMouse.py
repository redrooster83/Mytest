import pyautogui
import time

end_time = time.time() + 30 * 60 # 30 minutes * 60 seconds/minute
while time.time() < end_time:
    pyautogui.moveTo(x=100, y=100, duration=0.5) # move mouse to x, y coordinates
    pyautogui.moveTo(x=200, y=200, duration=0.5) # move mouse to x, y coordinates
    pyautogui.moveTo(x=300, y=300, duration=0.5) # move mouse to x, y coordinates
    time.sleep(5) # delay for 5 seconds

