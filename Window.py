from tkinter import Tk, Button, Label, StringVar, Canvas
from Alien import Alien
from GameCanvas import GameCanvas
from Input import Input
from Ship import Ship
from Vector2 import Vector2

#class window
class Window ( Tk ) :
    #init
    def __init__ ( self, winWidth : int, winHeight : int) :
        Tk.__init__ ( self )
        self.create_widgets()
        self.CreateInputs()

        self.winWidth = winWidth
        self.winHeight = winHeight
        
    #widgets
    def create_widgets(self):
        self.grid()

        #text label creation
        self.name_label = Label(self, text = "Space Invaders")
        self.name_label.grid(row = 2, column = 1, padx = 3, pady = 8)
        self.name_label.anchor('n')

        #button creation
        self.button_start = Button(self, text = 'Start', command = self.start)
        self.button_start.grid(row = 3, column = 1, padx = 3, pady = 8)
        self.button_start.anchor('n')

        self.button_quit = Button(self, text = 'Quit', command = self.quit)
        self.button_quit.grid(row = 4, column = 1, padx = 3, pady = 8)
        self.button_quit.anchor('n')

        #score label creation
        var_score = StringVar(value = "Score : ") #definir une fonction de score + sauvegarde du score en fin de partie
        self.score_label = Label(self, textvariable = var_score)
        
        #time label creation
        var_time = StringVar(value = "Time : ") #à faire autrement : definir une fonction de temps
        self.time_label = Label(self, textvariable = var_time)
        
        #live label creation
        var_life = StringVar(value = "Life.s : ") # à mettre dans les events de touche du vaisseau
        self.life_label = Label(self, textvariable = var_life)
        
    def CreateInputs(self):
        self.RightInput = Input("<Right>", "<KeyRelease-Right>", self)
        self.LeftInput = Input("<Left>", "<KeyRelease-Left>", self)
        self.UpInput = Input("<Up>", "<KeyRelease-Up>", self)
        self.RightInput = Input("<Down>", "<KeyRelease-Down>", self)
        self.SpaceInput = Input("<space>", "<KeyRelease-space>", self)

    #start the game
    def start(self):

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
        game_zone = GameCanvas ( self, self.winWidth - 5, self.winHeight - 70, "black" )
        game_zone.grid( row = 2, column = 1, columnspan= 10)

        #spaceship
        spaceship = Ship(game_zone, 0, Vector2(game_zone.w//2 , game_zone.h - 100), self.LeftInput, self.RightInput)
        
        #create alien list : one list with N alien level 1, one list with M alien level 2... -> compile list in an global list (for appear's probalility )
        list_level_alien = [ 10, 1 ]
        list_alien = []
        for j in range (5) :
            list_alien += [Alien(0, Vector2((40 + 10) * i + 350, j * (40 + 10) + 100), game_zone) for i in range(list_level_alien[0])]
        
        list_proba_red_alien = [0 for i in range (10)] + [1] #à déplacer dans la boucle de jeu + ne semble pas marcher
        
        for i in range(len(list_proba_red_alien)):
            if list_proba_red_alien[i] == 1 :
                list_alien += [Alien(1, Vector2(10, 1040), game_zone)]
        
        # while play_game == True :
        #     self.game_loop()
            
        #game_loop
                
    def game_loop () :
        pass
        # ennemy's mouvement
        # for ennemy_i in list_alien :
        #       if alien.ennemy_i.xposition == 0 or alien.ennemy.xposition == 1040 : # il faudrait récupérer le tag de l'alien parce que là ça ne marche pas
        #          for ennemy_j in list_alien :
        #             alien.ennemy_j.yposition += alien.speed
        #     if alien.ennemy.yposition == spaceship.xposition : 
        #           play_game = False
        #          game_zone = game_zone.destroy ()
        #         self.label_lose = Label ( game_zone, text = "Game Over")
        #         self.label_1.grid ( row = 2, column = 1, padx = 3, pady = 8 )
        #     alien.ennemy_i.xposition += alien.ennemy_i.speed
        
        
        #shoot
        # shoot_list = []
        # if "<Space>" :
        #     shoot_list += [ shoot ( game_zone, spaceship ) ]
                
    #quit the game
    def quit (self) :
        play_game = False
        self = self.destroy ()
    
   
    