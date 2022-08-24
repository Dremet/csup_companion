import cv2 as cv
import numpy as np
import os
from time import time
from cscom.windowcapture import WindowCapture

# adapted based on:
# https://github.com/learncodebygaming/opencv_tutorials/blob/master/004_window_capture/main.py


# initialize the WindowCapture class
wincap = WindowCapture('circuit-superstars')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    cv.imshow('Computer Vision', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')