from tkinter import Canvas

#class canvas
class GameCanvas(Canvas):
    def __init__ (self, in_window, w, h, bg_canvas) :
        super().__init__(in_window, width = w, height = h, bg = bg_canvas)
        self.w = w
        self.h = h
    #potentiellement adapter la taille ??


