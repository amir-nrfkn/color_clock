from tkinter import *
import time
import random


root = Tk()
root.title('clock')
# root.iconbitmap("")
root.geometry("300x400")


def r(): return random.randint(0, 255)


# c = '#%02X%02X%02X' % (r(), r(), r())
# my_canvas = Canvas(root, width=300, height=300)
# my_canvas.pack(pady=0)
# circle = my_canvas.create_oval(100, 150, 150, 0, fill="black")
# circle

C = Canvas(root, height=300, width=300)
C.pack()

coord = 50, 50, 250, 250
arc = C.create_arc(coord, start=0, fill="red")


def clock():
    hh = time.strftime("%H")
    mm = time.strftime("%M")
    ss = time.strftime("%S")

    c_time = '#%02X%02X%02X' % (r(), r(), r())
    c_background = '#%02X%02X%02X' % (r(), r(), r())
    c_clock = '#%02X%02X%02X' % (r(), r(), r())

    my_label.config(text=hh + ":" + mm + ":" + ss, fg=c_time, bg=c_background)
    # my_canvas.config(bg=c_clock)
    my_label.after(999, clock)


def update():
    my_label.config(text="New Text")


my_label = Label(root, text="", font=("Helvetica", 48))
my_label.pack(pady=20)

# my_label.after(1000, update)

clock()

root.mainloop()
