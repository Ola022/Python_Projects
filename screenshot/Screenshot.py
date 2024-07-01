"""
Use PyAutoGUI package
Install use  [ pip install pyautogui  ]
Install PILLOW  [ pip install pillow ]
"""
import pyautogui
import time


def screenshot():
    time.sleep(4)
    time_sc = time.time()
    name = "C:/Users/Ola/Documents/programming/Real-Projects/Screenshot_image/{}.png".format(time_sc)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()
    print(time_sc)


screenshot()
