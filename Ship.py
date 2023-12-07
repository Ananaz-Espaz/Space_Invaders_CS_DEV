from GameObject import GameObject
from GameCanvas import GameCanvas
from Input import Input
from Vector2 import Vector2

class Ship (GameObject) :
    def __init__(self, canvas : GameCanvas, level : int, initialPosition : Vector2, leftInput : Input, rightInput : Input):
        GameObject.__init__(self, canvas)
        
        self.level = level
        
        self.position = initialPosition
        
        self.xsize = 40
        self.ysize = 40
        self.speed = 10
        
        self._rightInput = rightInput
        self._leftInput = leftInput
        
        self._tag = "ship"
        
        self.Draw()
    
    #mvt function
    def go_right(self, event):
        if self.x + self.xsize <= self.game_zone.w :
            self.x = self.x + self.speed
            self.Draw()

    def go_left(self, event) :
        if self.x >= 0 :
            self.x = self.x - self.speed
            self.Draw()

    def Update(self, deltaTime : float):
        GameObject.Update(self, deltaTime)
        input = Vector2(self._rightInput.FloatValue() - self._leftInput.FloatValue())
        self.position += input * self.speed * deltaTime
        
        
    def Draw(self):
        GameObject.Draw(self)
        
        self._canvas.delete(self._tag)
        #create ship
        self._canvas.create_rectangle(
            self.position.X, 
            self.position.Y, 
            self.position.Y + self.xsize, 
            self.position.Y + self.ysize, 
            fill='white', 
            tag=self._tag)