from ppadb.client import Client
import cv2
import numpy as np
from PIL import Image
import mss
import time

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

print(f'connected to device {device}')

with mss.mss() as sct:
    monitor = {"top": 850, "left": 230, "width": 620, "height": 260}

    while "Screen capturing":
        last_time = time.time()
        img = np.array(sct.grab(monitor))

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(
            gray, cv2.HOUGH_GRADIENT,
            1, 20,
            param1=50, param2=30,
            minRadius=1, maxRadius=40)

        if circles is not None:
            circles = np.uint16(circles)

            for pt in circles[0, :]:
                x, y, r = pt[0], pt[1], pt[2]
                cv2.circle(img, (x, y), r, (0, 0, 255), 5)
                ball_y = y

        cv2.imshow("output", img)
        print(f"fps: {1 / (time.time() - last_time)}")
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break   