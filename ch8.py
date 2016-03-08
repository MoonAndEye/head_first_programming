# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:08:35 2016

@author: Moon
"""

from tkinter import *

app = Tk()
app.title("Head-Ex Deliveries")
Label(app, text = "Depot:").pack()
depot = Entry(app)
depot.pack()

Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

app.mainloop()
