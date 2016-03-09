# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 22:16:43 2016

@author: Moon
"""

from tkinter import *
import pygame.mixer
from tkinter.messagebox import askokcancel


mixer = pygame.mixer
mixer.init()

def track_start():
    track.play(loops = -1)
    
def track_stop():
    track.stop()

def shutdown():
    #if askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
    track.stop()
    app.destroy()

app = Tk()
app.title('Head first Mix')
app.geometry('250x100+200+100')


sound_file = "50459_M_RED_Nephlimizer.wav"

track = mixer.Sound(sound_file)

start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)

stop_button = Button(app, command = track_stop, text = "Stop")
stop_button.pack(side = RIGHT)

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()