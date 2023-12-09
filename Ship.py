from GameObject import GameObject
from GameCanvas import GameCanvas
from GameObjectManager import GameObjectManager
from Input import Input
from Layer import Layer
from Projectile import Projectile
from Vector2 import Vector2

class Ship (GameObject) :
    def __init__(self, canvas : GameCanvas, level : int, initialPosition : Vector2, leftInput : Input, rightInput : Input, spaceInput : Input):
        super().__init__(canvas, initialPosition, Vector2(40, 40), "Ship", Layer.Ship)
        
        self.level = level
        
        self.speed = 200
        
        self._rightInput = rightInput
        self._leftInput = leftInput
        self._spaceInput = spaceInput
        
        self._projectiles = []
        
        self._fireRate = 4
        self._fireTimer = 0
        
        self.Draw()

    def Update(self, deltaTime : float):
        super().Update(deltaTime)
        input = Vector2(self._rightInput.FloatValue() - self._leftInput.FloatValue(), 0)
        
        self.position += input * (self.speed * deltaTime)
        
        self.UpdateProjectiles(deltaTime)
        
        if (self._spaceInput.BoolValue()):
            if (self._fireTimer > (1 / self._fireRate)):
                self._projectiles.append(Projectile(self._canvas, self.position, Vector2(0, -1), True))
                self._fireTimer = 0
            
        self._fireTimer += deltaTime
        
        self.Draw()

    def UpdateProjectiles(self, deltaTime : float):
        projectilesToDelete = []
        for proj in self._projectiles:
            proj.Update(deltaTime)
            if (proj.UpdateCollisions(GameObjectManager.GameObjects)):
                projectilesToDelete.append(proj)
                
        for proj in projectilesToDelete:
            self._projectiles.remove(proj)
        
        
    def Draw(self):
        super().Draw()
        #create ship
        self._canvas.create_rectangle(
            self.position.X, 
            self.position.Y, 
            self.position.X + self.size.X, 
            self.position.Y + self.size.Y, 
            fill='white', 
            tag=self._tag)