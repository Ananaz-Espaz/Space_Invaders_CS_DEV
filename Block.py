from GameObject import GameObject
from GameCanvas import GameCanvas
from Layer import Layer
from Vector2 import Vector2

class Block (GameObject) : 
    _nextBlockID = 0
    
    def __init__ (self, canvas : GameCanvas, position : Vector2) :
        self.position = position
        self.life = 5
        
        GameObject.__init__(self, canvas, position, Vector2(40, 80), f"Block#{Block._nextBlockID}", Layer.Block)
        Block._nextBlockID += 1
        
        self.Draw()
        
    def Draw(self):
        GameObject.Draw(self)
        self._canvas.create_rectangle(
            self.position.X, 
            self.position.Y, 
            self.position.X + self.size.X, 
            self.position.Y + self.size.Y, 
            fill="grey", 
            tag=self._tag)