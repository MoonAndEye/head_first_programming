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

app = Tk()
app.title('Head first Mix')
app.geometry('250x100+200+100')

def track_start():
    track.play(loops = -1)
    
def track_stop():
    track.stop()

def shutdown():
    #if askokcancel(title = 'Are you sure?', message = 'Do you really want to quit?'):
    track.stop()
    app.destroy()

def track_toggle():
    if track_playing.get() == 1:
        track.play(loops = -1)
    else:
        track.stop()

def change_volume(v):
    track.set_volume(volume.get())

track_playing = IntVar()

sound_file = "50459_M_RED_Nephlimizer.wav"

track = mixer.Sound(sound_file)
"""
start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)

stop_button = Button(app, command = track_stop, text = "Stop")
stop_button.pack(side = RIGHT)
"""

volume = DoubleVar()
volume_scale = Scale(app,
                     variable = volume,
                     from_    = 0.0,
                     to       = 1.0,
                     resolution = 0.1,
                     command   = change_volume,
                     label     = 'volume',
                     orient    = HORIZONTAL)
                     
volume_scale.pack(side = RIGHT)

track_button = Checkbutton(app, variable = track_playing,
                 command = track_toggle,
                 text = 'ON/OFF').pack()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()