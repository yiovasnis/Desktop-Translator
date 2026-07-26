import mss
import numpy as np
import cv2


class ScreenCapture:

    def __init__(self):
        self.sct = mss.mss()

    def capture(self):

        monitor = self.sct.monitors[1]

        screenshot = self.sct.grab(monitor)

        img = np.array(screenshot)

        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        return img