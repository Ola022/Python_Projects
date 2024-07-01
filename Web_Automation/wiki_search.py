import wikipedia
import tkinter as tk

""" [ pip install wikipedia ]"""


def on_press():
    query = get_q.get()
    #text.
    text.insert(tk.INSERT, wikipedia.summary(query))


root = tk.Tk()
#root.geometry('320x100')
root.title("WIKI Search APP")
# Question Dialog
question = tk.Label(root, text="Question")
question.pack()
# Search Entry
get_q = tk.Entry(root,  bd=5)
get_q.pack()
# submit
submit = tk.Button(root, text="Search", command=on_press)
submit.pack()

text = tk.Text(root)
text.pack()


root.mainloop()