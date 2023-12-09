from GameCanvas import GameCanvas
from GameObjectManager import GameObjectManager
from Layer import Layer
from Vector2 import Vector2

class GameObject:
    
    def __init__(self, canvas : GameCanvas, position : Vector2, size : Vector2, tag : str, layer : int) -> None:
        self._canvas = canvas
        
        self._tag = tag
        self._isAlive = True
        self.position = position
        self.size = size
        
        self._layer = layer
        
        GameObjectManager.Register(self)
        pass
    
    def Update(self, deltaTime : float):
        pass
    
    def Draw(self):
        self.Erease()
        
    def Erease(self):
        self._canvas.delete(self._tag)
    
    def Destroy(self):
        
        print("GO dest")
        self._isAlive = False
        self.Erease()
        GameObjectManager.Unregister(self)
    
    def CollidesWith(self, other : 'GameObject') -> bool:
        if (not self._isAlive):
            return False
        
        if (not Layer.DoInteract(self._layer, other._layer)):
            return False
        
        x0y0 = self.position
        x0y1 = self.position + Vector2(0, self.size.Y)
        x1y0 = self.position + Vector2(self.size.X, 0)
        x1y1 = self.position + self.size
        
        x0y0InOther = GameObject.IsInSquare(x0y0, other.position, other.size)
        x0y1InOther = GameObject.IsInSquare(x0y1, other.position, other.size)
        x1y0InOther = GameObject.IsInSquare(x1y0, other.position, other.size)
        x1y1InOther = GameObject.IsInSquare(x1y1, other.position, other.size)
        
        return x0y0InOther or x0y1InOther or x1y0InOther or x1y1InOther
    
    def OnCollisionEnter(self, other : 'GameObject'):
        pass
        
    def IsInSquare(point: Vector2, squareOrigin : Vector2, squareSize : Vector2) -> bool:
        return squareOrigin.X <= point.X <= squareOrigin.X + squareSize.X and squareOrigin.Y <= point.Y <= squareOrigin.Y + squareSize.Y