import cv2
import numpy as np

class Piece:
    def __init__(self, x, y, w, h, cell, symbol):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cell = cell
        self.symbol = symbol
        
