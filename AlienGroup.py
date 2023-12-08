from Alien import Alien
from GameCanvas import GameCanvas
from Vector2 import Vector2


class AlienGroup():
    def __init__(self, canvas : GameCanvas, aliensLevel : int, aliensStartPositions : list[Vector2], startState : int = 0) -> None:
        self._aliens = [Alien(canvas, aliensLevel, pos, self) for pos in aliensStartPositions]
        
        # State 0 : =>
        # State 1 : \/
        # State 2 : <=
        # State 3 : \/
        self.CurrentState = startState
        self.NextStateRequests = []
        
        pass
    
    def Update(self, deltaTime : float):
        for alien in self._aliens:
            alien.Update(deltaTime)
            
        self.AfterUpdate()
    
    def RequestDirectionChange(self, requestedState : int):
        self.NextStateRequests.append(requestedState)
        
    def AfterUpdate(self):
        if (len(self.NextStateRequests) == 0):
            return
        
        self.NextStateRequests.sort()
        
        mostRequestedState = -1
        mostRequestedStateCount = 0
        currentRequest = self.NextStateRequests[0]
        currentRequestCount = 0
        
        for request in self.NextStateRequests:
            if (request == currentRequest):
                currentRequestCount += 1
            else:
                if (currentRequestCount > mostRequestedStateCount):
                    mostRequestedStateCount = currentRequestCount
                    mostRequestedState = currentRequest
                    
                currentRequest = request
                currentRequestCount = 0
        
        if (currentRequestCount > mostRequestedStateCount):
            mostRequestedStateCount = currentRequestCount
            mostRequestedState = currentRequest
            
        self.ChangeState(mostRequestedState)
        self.NextStateRequests.clear()
                 
    def ChangeState(self, newState : int):
        self.CurrentState = newState
        
        for alien in self._aliens:
            alien.OnGroupStateChanged()
        
        