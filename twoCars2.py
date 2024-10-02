from ppadb.client import Client
import cv2
import numpy as np
from PIL import Image
import mss
import time
import pyautogui
import win32api, win32con

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]
font = cv2.FONT_HERSHEY_COMPLEX

print(f'connected to device {device}')

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# def click(x, y):
#     pyautogui.click(x = x, y = y)

with mss.mss() as sct:
    monitor = {"top": 650, "left": 230, "width": 620, "height": 150}
    red, blue = 1, 2
    while "Screen capturing":
        last_time = time.time()
        img = np.array(sct.grab(monitor))

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0, 19, 0])
        upper_red = np.array([180, 255, 255])

        mask = cv2.inRange(hsv, lower_red, upper_red)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            if 100 < area < 1000:
                cv2.drawContours(img, [approx], 0, (180, 105, 255), 2)
                
                n = approx.ravel()
                x, y = n[0], n[1]
                cv2.putText(img, str(x)+' '+str(y), (x, y), font, 0.75, (255, 255, 255))

                shape = 2 < len(approx) < 9
                lane = 0
                if 100 < x < 300: lane = 1
                elif 300 < x < 450: lane = 2
                elif 450 < x : lane = 3
                print(f'{"sqaure" if shape else "circle"} in lane {lane}')
                curr = time.time()
                clk = False
                if lane < 2:
                    if shape:
                        if lane == red: 
                            click(400, 1000)
                            print('clicked')
                            if red: red = 0
                            else: red = 1
                            clk = True
                    else:
                        if lane != red: 
                            click(400, 1000)
                            print('clicked')
                            if red: red = 0
                            else: red = 1
                            clk = True

                            
                else:
                    if shape:
                        if lane == blue: 
                            click(700, 1000)
                            print('clicked')
                            if blue == 2: blue = 3
                            else: blue = 2
                            clk = True

                    else:
                        if lane != blue: 
                            click(700, 1000)
                            print('clicked')
                            if blue == 2: blue = 3
                            else: blue = 2
                            clk = True
                if clk:
                    print(f'clicked in {(time.time()-curr)*1000} ms in lane {lane}')


        cv2.imshow("output", img)
        #print(f"fps: {1 / (time.time() - last_time)}")
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
        #time.sleep(0.25)