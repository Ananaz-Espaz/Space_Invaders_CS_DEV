from tkinter import Misc as TkMisc

class Input():

    def __init__(self, keyDown : str, keyRelease : str, zone : TkMisc):
        zone.bind(keyDown, self._OnKeyDown)
        zone.bind(keyRelease, self._OnKeyReleased)

        self._keyState = False
        
    def BoolValue(self) -> bool :
        return self._keyState
    
    def FloatValue(self) -> float :
        if (self._keyState):
            return 1
        return 0

    def _OnKeyDown(self, event):
        self._keyState = True

    def _OnKeyReleased(self, event):
        self._keyState = False