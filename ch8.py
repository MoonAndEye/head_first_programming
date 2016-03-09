# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:08:35 2016

@author: Moon
"""

from tkinter import *

def save_data():
    fileD = open("delieveries.txt", "a")
    fileD.write("Depot:\n")
    fileD.write("%s\n" % depot.get())
    fileD.write("Description:\n")
    fileD.write("%s\n" % description.get())
    fileD.write("Address:\n")
    fileD.write("%s\n" % address.get("1.0", END))
    fileD.close
    depot.set(None)
    description.delete(0, END)
    address.delete("1.0", END)
    
    
app = Tk()
app.title("Head-Ex Deliveries")
Label(app, text = "Depot:").pack()
#depot = Entry(app)
#depot.pack()

depot = StringVar()
depot.set(None)


Radiobutton(app, text = "Cambridge, MA", value = "Cambridge, MA", variable = depot).pack()
Radiobutton(app, text = "Cambridge, UK", value = "Cambridge, UK", variable = depot).pack()
Radiobutton(app, text = "Seattle, WA", value = "Seattle, WA", variable = depot).pack()


Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()

Label(app, text = "Address:").pack()
address = Text(app)
address.pack()

Button(app, text = "Save", command = save_data).pack()

app.mainloop()
