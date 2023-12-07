#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Nov 10 08:34:49 2023

@author: anais.guerents

Programme principale, Space invaders Game

"""

from tkinter import Tk, Button, Label, StringVar, Canvas
from random import randint

#class window
class window ( Tk ) :
    #init
    def __init__ ( self, winWidth : int, winHeight : int) :
        Tk.__init__ ( self )
        self.create_widgets ()

        self.winWidth = winWidth
        self.winHeight = winHeight

    #start the game
    def start ( self ):

        play_game = True
        self.button_start.destroy()
        
        self.button_quit.anchor ('sw')
        
        # name label display
        self.name_label.grid ( row = 1, column = 1, padx = 1, pady = 1 )
        
        # button quit display
        self.button_quit.grid ( row = 1, column = 9, padx = 1, pady = 1 )
        
        # score label display
        var_score = 0
        self.score_label.grid ( row = 1, column = 2, padx = 1, pady = 1 )
        
        # time label display
        var_time = 0
        self.time_label.grid ( row = 1, column = 4 , padx = 1, pady = 1 )
        
        # life label display
        var_life = 0
        self.life_label.grid ( row = 1, column = 6, padx = 1, pady = 1 )
        
        #canvas creation
        game_zone = canvas ( self, self.winWidth - 5, self.winHeight - 70, "black" )
        game_zone.grid( row = 2, column = 1, columnspan= 10)

        #spaceship
        spaceship = ship ( 0 , game_zone.w//2 , game_zone.h - 100 , game_zone )
        
        #create alien list : one list with N alien level 1, one list with M alien level 2... -> compile list in an global list (for appear's probalility )
        list_level_alien = [ 10, 1 ]
        list_alien = []
        for j in range (5) :
            list_alien += [ alien ( 0, (40+10)*i+350, j*(40+10)+100, game_zone ) for i in range ( list_level_alien [0] ) ]
        
        list_proba_red_alien = [ 0 for i in range (10) ] + [1] #à déplacer dans la boucle de jeu + ne semble pas marcher
        for i in range ( len ( list_proba_red_alien ) ):
            if list_proba_red_alien [ i ] == 1 :
                list_alien += [ alien (1, 10, 1040, game_zone) ]
        
        #game_loop
                
        def game_loop () :
            #ennemy's mouvement
            #for ennemy_i in list_alien :
             #   if alien.ennemy_i.xposition == 0 or alien.ennemy.xposition == 1040 : # il faudrait récupérer le tag de l'alien parce que là ça ne marche pas
              #      for ennemy_j in list_alien :
               #         alien.ennemy_j.yposition += alien.speed
                #if alien.ennemy.yposition == spaceship.xposition : 
                 #   play_game = False
                  #  game_zone = game_zone.destroy ()
                   # self.label_lose = Label ( game_zone, text = "Game Over")
                    #self.label_1.grid ( row = 2, column = 1, padx = 3, pady = 8 )
                #alien.ennemy_i.xposition += alien.ennemy_i.speed
            
            
            #shoot
            shoot_list = []
            if "<Space>" :
                shoot_list += [ shoot ( game_zone, spaceship ) ]
                
        while play_game == True :
            game_loop()
            
    #quit the game
    def quit (self) :
        play_game = False
        self = self.destroy ()
    
    #widgets
    def create_widgets ( self ):
        
        self.grid()

        #text label creation
        self.name_label = Label ( self, text = "Space Invaders" )
        self.name_label.grid ( row = 2, column = 1, padx = 3, pady = 8 )
        self.name_label.anchor ( 'n' )

        #button creation
        self.button_start = Button (self, text = 'Start', command = self.start )
        self.button_start.grid ( row = 3, column = 1, padx = 3, pady = 8 )
        self.button_start.anchor ('n')

        self.button_quit = Button ( self, text = 'Quit', command = self.quit )
        self.button_quit.grid ( row = 4, column = 1, padx = 3, pady = 8 )
        self.button_quit.anchor ('n')

        #score label creation
        var_score = StringVar (value = "Score : ") #definir une fonction de score + sauvegarde du score en fin de partie
        self.score_label = Label ( self, textvariable = var_score)
        
        #time label creation
        var_time = StringVar ( value = "Time : " )#à faire autrement : definir une fonction de temps
        self.time_label = Label ( self, textvariable = var_time )
        
        #live label creation
        var_life = StringVar ( value = "Life.s : " )# à mettre dans les events de touche du vaisseau
        self.life_label = Label ( self, textvariable = var_life )

    
        

#class canvas
class canvas ( Canvas ):
    def __init__ (self, in_window, w, h, bg_canvas) :
        Canvas.__init__(self, in_window, width = w, height = h, bg = bg_canvas )
        self.w = w
        self.h = h
    #potentiellement adapter la taille ??



#class alien
class alien () :
    i = 0
    #init
    def __init__ ( self , level : int, x : int, y : int, game_zone : canvas): 
        self.level = level
        self.x = x # x position 
        self.y = y # y position
        self.game_zone = game_zone

        self.tag = f"alien{alien.i}"
        alien.i += 1

        
        #alien's stats
        if self.level == 0 :
            self.damage = 1
            self.life = 1
            self.color = 'lightblue'
            self.xsize = 40
            self.ysize = 40
            self.speed = 6
        elif self.level == 1 :
            self.dammage = 1
            self.life = 1
            self.color = 'red'
            self.xsize = 60
            self.ysize = 40
            self.speed = 6
        else:
            self.dammage = 0
            self.life = 1
            self.color = 'white'
            self.xsize = 40
            self.ysize = 40
            self.speed = 6


        self.Update()
    
    #mouvement
    def go_front ( self ):
        if self.y + self.ysize == self.game_zone.h :   
            self.destroy()
        else :
            self.y = self.y + self.speed
        self.Update()

    def go_right ( self ):
        if self.x + self.xsize == self.game_zone.w :
            self.go_left ( self )
        else :
            self.x = self.x + self.speed
        self.Update()

    def go_left ( self ):
        if self.x == 0 :
            self.go_right ( self )
        else :
            self.x = self.x - self.speed
        self.Update()

    def Update ( self ) :
        self.game_zone.delete ( self.tag )
        #alien create
        self.game_zone.create_rectangle ( self.x , self.y, self.x+self.xsize , self.y+self.ysize, fill=self.color, tag = self.tag )



#class ship ( user spaceship )
class ship () :
    def __init__ ( self , level, x, y, game_zone : canvas ): 
        self.level = level
        self.x = x # x position 
        self.y = y # y position
        self.xsize = 40
        self.ysize = 40
        self.speed = 10
        self.game_zone = game_zone
        
        self.Update()
        
        #mvt
        self.game_zone.master.bind ( '<Right>', self.go_right )
        self.game_zone.master.bind ( '<Left>' , self.go_left )
    
    #mvt function
    def go_right ( self, event ) :
        if self.x + self.xsize <= self.game_zone.w :
            self.x = self.x + self.speed
            self.Update()

    def go_left ( self, event ) :
        if self.x >= 0 :
            self.x = self.x - self.speed
            self.Update()

    def Update ( self ) :
        self.game_zone.delete ( "ship" )
        #create ship
        self.game_zone.create_rectangle ( self.x , self.y, self.x+self.xsize , self.y+self.ysize, fill='white', tag="ship" )

#class shoot
class shoot () :
    def __init__ ( self, game_zone : canvas, spaceship : ship ) : 
        self.x = spaceship.x # x position 
        self.y = spaceship.y # y position
        self.xsize = 6
        self.ysize = 10
        self.speed = 10
        self.game_zone = game_zone
    def go_front ( self ):
        if self.y == 0 :   
            self.destroy()
        else :
            self.y = self.y + self.speed
        self.Update()

#class bloc (obstacle)

class bloc () : 
    def __init__ ( x, y, self, game_zone :canvas ) :
        self.x = x
        self.y = y
        self.ysize = 40
        self.xsize = 80
        self.game_zone = game_zone
        self.life = 5
        
        self.Update()
        
#windows dimensions
width = 1080
height = 720

#display
main_wind = window (width, height)
main_wind.title ('Space Invaders')
main_wind.geometry (f'{width}x{height}+0+0')
main_wind.config ( bg = "black" )

main_wind.mainloop()
