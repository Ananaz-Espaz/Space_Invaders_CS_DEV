from GameObject import GameObject
from GameCanvas import GameCanvas
from Vector2 import Vector2

class Block (GameObject) : 
    def __init__ (self, canvas : GameCanvas, position : Vector2) :
        GameObject.__init__(self, canvas)
        
        self.position = position
        self.ysize = 40
        self.xsize = 80
        self.life = 5
        
        self.Update()