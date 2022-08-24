import cv2 as cv
import numpy as np
import os
from time import time
import pyautogui
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\micro\AppData\Local\Tesseract-OCR\tesseract.exe'

times_recorded = []
current_time_recorded = None
last_time_recorded = None

lap_times = []

try:
    while(True):
        last_time_recorded = current_time_recorded

        # get an updated image of the game
        screenshot = pyautogui.screenshot(region=(3230,230,150,30))
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        text = pytesseract.image_to_string(screenshot, config="--psm 7")
        
        try:
            assert ":" in text and "." in text
            current_time_recorded = int(text.replace(",",".").split(":")[0])*60+float(text.replace(",",".").split(":")[1])
        except:
            current_time_recorded = None
        
        if current_time_recorded is not None and last_time_recorded is not None:
            if (not lap_times or current_time_recorded != lap_times[-1]) and current_time_recorded == last_time_recorded:
                lap_times.append(last_time_recorded)
                print(f"DEBUG: Found lap time {last_time_recorded}.")
        
        if current_time_recorded is not None:
            times_recorded.append(current_time_recorded)

except KeyboardInterrupt:
    for number, time in enumerate(lap_times, start=1):
        print(f"Lap {number}, Time: {time}")
    print(f"Best Time: {min(lap_times)} at lap {lap_times.index(min(lap_times))}")
    print(f"Worst Time: {max(lap_times)} at lap {lap_times.index(max(lap_times))}")
    print(f"Average Time: {sum(lap_times)/len(lap_times)}")

print('Done.')