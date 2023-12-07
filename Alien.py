from GameObject import GameObject
from GameCanvas import GameCanvas
from Vector2 import Vector2

#class alien
class Alien (GameObject) :
    _nextAlienID = 0
    #init
    def __init__(self , level : int, initialPosition : Vector2, canvas : GameCanvas):
        GameObject.__init__(self, canvas)
        
        self.level = level
        
        self.position = initialPosition

        self._tag = f"alien{Alien._nextAlienID}"
        Alien._nextAlienID += 1

        
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

        self.Draw()
    
    #mouvement
    def go_front ( self ):
        if self.y + self.ysize == self.game_zone.h :   
            self.destroy()
        else :
            self.y = self.y + self.speed
        self.Draw()

    def go_right ( self ):
        if self.x + self.xsize == self.game_zone.w :
            self.go_left ( self )
        else :
            self.x = self.x + self.speed
        self.Draw()

    def go_left ( self ):
        if self.x == 0 :
            self.go_right ( self )
        else :
            self.x = self.x - self.speed
        self.Draw()
        

    def Update(self, deltaTime : float):
        GameObject.Update(self, deltaTime)
        
    def Draw(self):
        GameObject.Draw(self)
        
        self._canvas.delete(self._tag)
        self._canvas.create_rectangle(
            self.position.X, 
            self.position.Y, 
            self.position.X + self.xsize, 
            self.position.Y + self.ysize, 
            fill=self.color, 
            tag=self._tag)

