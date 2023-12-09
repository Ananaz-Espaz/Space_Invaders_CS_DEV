from GameCanvas import GameCanvas
from GameObject import GameObject
from Layer import Layer
from Vector2 import Vector2


#class shoot
class Projectile(GameObject) :
    _nextProjectileID = 0
    
    def __init__(self, canvas : GameCanvas, initialPosition : Vector2, direction : Vector2, shipProjectile : bool) : 
        self._direction = direction
        
        self._speed = 300
        
        if (shipProjectile):
            layer = Layer.ShipProjectile
        else :
            layer = Layer.AlienProjectile
        super().__init__(canvas, initialPosition, Vector2(6, 10), f"Projectile#{Projectile._nextProjectileID}", layer)
        Projectile._nextProjectileID += 1
        
        self.Draw()
        
    def Update(self, deltaTime : float):
        if (not self._isAlive):
            return
        super().Update(deltaTime)
        self.position += self._direction * self._speed * deltaTime
        
        self.Draw()
        
    def UpdateCollisions(self, collidableObjects : list[GameObject]) -> bool:
        if (not self._isAlive):
            return False
        
        if (self.position.Y <= 0):
            self.Destroy()
            return True
        
        for object in collidableObjects :
            if (object == self):
                continue
            if (self.CollidesWith(object)):
                object.OnCollisionEnter(self)
                self.Destroy()
                return True
            
        return False
        
    def Draw(self):
        GameObject.Draw(self)
        self._canvas.create_rectangle(
            self.position.X, 
            self.position.Y, 
            self.position.X + self.size.X, 
            self.position.Y + self.size.Y, 
            fill='white', 
            tag=self._tag)