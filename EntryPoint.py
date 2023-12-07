#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Nov 10 08:34:49 2023

@author: anais.guerents

Programme principale, Space invaders Game

"""
    
from Window import Window


if __name__ == "__main__":
    print("EntryPoint")
    #windows dimensions
    width = 1080
    height = 720

    #display
    main_wind = Window (width, height)
    main_wind.title ('Space Invaders')
    main_wind.geometry (f'{width}x{height}+0+0')
    main_wind.config ( bg = "black" )

    main_wind.mainloop()



        
