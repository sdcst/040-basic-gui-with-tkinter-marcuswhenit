import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title ("tk")
window.geometry("500x40")

box1 = tk.Entry(window,text="Entry widgets can be typed in", width=20, relief=SUNKEN, borderwidth=3)
box2 = tk.Entry(window,text="Entry widgets can be typed in", width=20, relief=SUNKEN, borderwidth=3)
box3 = tk.Entry(window,text="Entry widgets can be typed in", width=30, relief=SUNKEN, borderwidth=3)
lable1 = tk.Label(window, text="+", borderwidth=3,)
lable2 = tk.Label(window, text="=", borderwidth=3,)
box1.grid(row = 1, column = 1,)
lable1.grid(row = 1, column = 2)
box2.grid(row = 1, column = 3)
lable2.grid(row = 1, column = 4)
box3.grid(row = 1, column = 5,)



window.mainloop()