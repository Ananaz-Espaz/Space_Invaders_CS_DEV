from GameCanvas import GameCanvas
from GameObject import GameObject
from Vector2 import Vector2


#class shoot
class Projectile(GameObject) :
    _nextProjectileID = 0
    
    def __init__(self, canvas : GameCanvas, initialPosition : Vector2, velocity : Vector2) : 
        GameObject.__init__(self, canvas)
        
        self.position = initialPosition
        self.velocity = velocity
        
        self.xsize = 6
        self.ysize = 10
        self.speed = 10
        
        self._tag = f"projectile{Projectile._nextProjectileID}"
        Projectile._nextProjectileID += 1
        
    def go_front ( self ):
        if self.y == 0 :   
            self.destroy()
        else :
            self.y = self.y + self.speed
        self.Update()

    def Update(self, deltaTime : float):
        GameObject.Update(self, deltaTime)
        self.position = self.position + self.velocity * deltaTime
        
    def Draw(self):
        GameObject.Draw(self)
        
        self._canvas.delete(self._tag)
        self._canvas.create_rectangle(
            self.position.X, 
            self.position.Y, 
            self.position.Y + self.xsize, 
            self.position.Y + self.ysize, 
            fill='white', 
            tag=self._tag)