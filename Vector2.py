import math

class Vector2 :
    
    def __init__(self) -> None:
        self.__init__(0, 0)
        pass
    
    def __init__(self, x : float, y : float) -> None:
        self.X = x
        self.Y = y
        pass
    
    def SqrMagnitude(self) -> float:
        return self.X**2 + self.Y**2
    
    def Magnitude(self) -> float:
        return math.sqrt(self.SqrMagnitude())
    
    def Normalized(self) -> 'Vector2':
        return self / self.Magnitude()
        
    def __repr__(self) -> str:
        return f"({self.X}, {self.Y})"
    
    # Operators
    def __add__(self, other):
        return Vector2(self.X + other.X, self.Y + other.Y)
    
    def __sub__(self, other):
        return Vector2(self.X - other.X, self.Y - other.Y)
    
    def __mul__(self, mul):
        return Vector2(self.X * mul, self.Y * mul)
    
    def __truediv__(self, div):
        return Vector2(self.X / div, self.Y / div)
    
    def __iadd__(self, other):
        return self.__add__(other)
    
    def __isub__(self, other):
        return self.__sub__(other)
    
    def __imul__(self, mul):
        return self.__mul__(mul)
    
    def __itruediv__(self, div):
        return self.__truediv__(div)
    
    def __neg__(self):
        return Vector2(-self.X, -self.Y)