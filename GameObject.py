import GameCanvas

class GameObject:
    
    def __init__(self, canvas : GameCanvas) -> None:
        self._canvas = canvas
        pass
    
    def Update(self, deltaTime : float):
        pass
    
    def Draw(self):
        pass