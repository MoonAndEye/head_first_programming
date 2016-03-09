# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 22:16:43 2016

@author: Moon
"""

from tkinter import *
import pygame.mixer

mixer = pygame.mixer
mixer.init()

def track_start():
    track.play(loops = -1)
    
def track_stop():
    track.stop()

app = Tk()
app.title('Head first Mix')
app.geometry('250x100+200+100')

start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)

stop_button = Button(app, command = track_stop, text = "Stop")
stop_button.pack(side = RIGHT)

sound_file = "50459_M_RED_Nephlimizer.wav"

track = mixer.Sound(sound_file)

app.mainloop()