#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 08:36:30 2023

@author: anais.guerents

Tkinter fichier "brouillon" à copier coller sur le programme principale
Tkinter ne fonctionne qu'avec un seul fichier

"""

from tkinter import Tk, Button, Label, StringVar, Frame

#main window
main_wind = Tk()
main_wind.title('Space Invaders')
main_wind.geometry('1600x1200+100+400')

#main menu
main_menu = Frame ( main_wind, relief = 'groove', bg='black', borderwidth=2)

main_menu.pack(padx=2,pady=2)

#main menu button
button_new_game = Button ( main_menu , text = 'New Game', command = main_menu.destroy ).pack(padx=10,pady=10)

button_quit = Button ( main_menu , text = 'Quit' , command = main_wind.destroy).pack(padx=10,pady=10)



#score
score = StringVar()
score = 0 #à supprimer uniquement pour voir où est le score
score_label = Label(main_wind, text=score)
score_label.pack(side='right',padx=5, pady='5')

main_wind.mainloop()