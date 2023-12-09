from GameObject import GameObject
from GameCanvas import GameCanvas
from Layer import Layer
from Vector2 import Vector2

#class alien
class Alien (GameObject) :
    _nextAlienID = 0
    
    #init
    def __init__(self, canvas : GameCanvas, level : int, initialPosition : Vector2, group):
        
        self.level = level
        
        self._group = group
        
        self.InitStates()
        
        self._downMaxMovement = 50

        size = Vector2(0, 0)
        #alien's stats
        if self.level == 0 :
            self.damage = 1
            self.life = 1
            self.color = 'lightblue'
            size = Vector2(40, 40)
            self.speed = 120
        elif self.level == 1 :
            self.dammage = 1
            self.life = 1
            self.color = 'red'
            size = Vector2(60, 40)
            self.speed = 120
        else:
            self.dammage = 0
            self.life = 1
            self.color = 'white'
            size = Vector2(40, 40)
            self.speed = 120
            
        super().__init__(canvas, initialPosition, size, f"Alien#{Alien._nextAlienID}", Layer.Alien)
        Alien._nextAlienID += 1
        self._heightOnStateEnter = self.position.Y

        self.Draw()
        
    def InitStates(self):
        self._states = {
            0 : self.State0,
            1 : self.State1,
            2 : self.State2,
            3 : self.State3}

    def Update(self, deltaTime : float):
        super().Update(deltaTime)
        
        self.position += self._states[self._group.CurrentState]() * self.speed * deltaTime
        
        self.Draw()
        
    def OnGroupStateChanged(self):
        self._heightOnStateEnter = self.position.Y
        
    def OnCollisionEnter(self, other: GameObject):
        super().OnCollisionEnter(other)
        self.life -= 1
        if (self.life <= 0):
            self.Destroy()
        
    def Destroy(self):
        super().Destroy()
        self._group.OnAlienDestroyed(self)
    # =>
    def State0(self) -> Vector2:
        if (self.position.X >= 1040):
            self._group.RequestDirectionChange(1)
        return Vector2(1, 0)
    
    # \/
    def State1(self) -> Vector2:
        if (abs(self._heightOnStateEnter - self.position.Y) >= self._downMaxMovement):
            self._group.RequestDirectionChange(2)
        return Vector2(0, 1)
    
    # <=
    def State2(self) -> Vector2:
        if (self.position.X <= 0):
            self._group.RequestDirectionChange(3)
        return Vector2(-1, 0)
    
    # \/
    def State3(self) -> Vector2:
        if (abs(self._heightOnStateEnter - self.position.Y) >= self._downMaxMovement):
            self._group.RequestDirectionChange(0)
        return Vector2(0, 1)
        
    def Draw(self):
        super().Draw()
        self._canvas.create_rectangle(
            self.position.X, 
            self.position.Y, 
            self.position.X + self.size.X, 
            self.position.Y + self.size.Y, 
            fill=self.color, 
            tag=self._tag)
        

