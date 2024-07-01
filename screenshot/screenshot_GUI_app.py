"""
Use PyAutoGUI package
Install use  [ pip install pyautogui  ]
Install PILLOW  [ pip install pillow ]
"""
import pyautogui
import time
import tkinter as tk


def screenshot():
    time.sleep(2)
    time_sc = time.time()
    name = "C:/Users/Ola/Documents/programming/Real-Projects/Screenshot_image/{}.png".format(time_sc)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()


root = tk.Tk()
#root.geometry('320x100')
root.title("SCREEN-SHOT APP")
frame = tk.Frame(root)
frame.pack()

# frame.pack(pady=10)  # Add some padding for better layout

# Create button for Screenshot and Quit
button = tk.Button(frame, text="Take Screenshot", command=screenshot)
button.pack(side=tk.LEFT,)
#button.pack(side=tk.LEFT, padx=5)  # Add padding between buttons

close_btn = tk.Button(frame, text="Quit", command=root.quit)
close_btn.pack(side=tk.LEFT)
#close_btn.pack(side=tk.LEFT, padx=5)

root.mainloop()