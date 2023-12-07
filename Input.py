from tkinter import Misc as TkMisc

class Input():

    def __init__(self, keyDown : str, keyRelease : str, zone : TkMisc):
        zone.bind(keyDown, self._OnKeyDown)
        zone.bind(keyRelease, self._OnKeyReleased)

        self._keyState = False
        
    def State(self) -> bool :
        return self._keyState

    def _OnKeyDown(self):
        self._keyState = True

    def _OnKeyReleased(self):
        self._keyState = False