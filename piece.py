import cv2

class Piece:
    def __init__(self, x, y, w, h, cell, symbol):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.cell = cell
        self.o_needle = cv2.imread('./images/o_needle.png', cv2.IMREAD_UNCHANGED)
        self.x_needle = cv2.imread('./images/x_needle.png', cv2.IMREAD_UNCHANGED)
        self.blank_needle = cv2.imread('./images/blank_needle.png', cv2.IMREAD_UNCHANGED)
        self.symbol = self.image_type(symbol)


    def image_type(self, symbol):
        if symbol is self.x_needle:
            return "X"
        elif symbol is self.o_needle:
            return "O"
        else:
            return "Blank"
        
