# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 23:36:52 2016

@author: Moon
"""

from tkinter import *

app = Tk()

app.title("Your tkinter application")
app.geometry('450x100+200+100')

b1 = Button(app, text = "click me!", width = 10)
b1.pack()

app.mainloop()

