import time
import pyautogui
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# def click(x, y):
#     pyautogui.click(x = x, y = y)

x = time.time()
click(400, 1000)
print((time.time()-x)*1000, 'ms')