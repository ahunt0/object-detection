# bot logic
import pyautogui
from game import Game

class Bot:
    def __init__(self, game):
        self.game = game

    def click_position(self, position):
        # Calculate the coordinates of the center of the cell based on the position
        cell_width = self.game.dimensions['width'] // 3
        cell_height = self.game.dimensions['height'] // 3
        row = (position - 1) // 3
        col = (position - 1) % 3
        x = self.game.dimensions['left'] + cell_width * col + cell_width // 2
        y = self.game.dimensions['top'] + cell_height * row + cell_height // 2
        # Click on the calculated position
        pyautogui.click(x, y)

    def evaluate_board(self, pieces, turn):
        # check if there is an x piece in the center
        print("Pieces: ", len(pieces))
        if len(pieces) == 0:
            return
        
        # Define positions
        for piece in pieces:
            if piece.cell == (0, 0):
                top_left = piece
                # print(f"Top left piece: {top_left.symbol}")
            elif piece.cell == (0, 1):
                top_center = piece
                # print(f"Top center piece: {top_center.symbol}")
            elif piece.cell == (0, 2):
                top_right = piece
                # print(f"Top right piece: {top_right.symbol}")
            elif piece.cell == (1, 0):
                middle_left = piece
                # print(f"Middle left piece: {middle_left.symbol}")
            elif piece.cell == (1, 1):
                center = piece
                # print(f"Center piece: {center.symbol}")
            elif piece.cell == (1, 2):
                middle_right = piece
                # print(f"Middle right piece: {middle_right.symbol}")
            elif piece.cell == (2, 0):
                bottom_left = piece
                # print(f"Bottom left piece: {bottom_left.symbol}")
            elif piece.cell == (2, 1):
                bottom_center = piece
                # print(f"Bottom center piece: {bottom_center.symbol}")
            elif piece.cell == (2, 2):
                bottom_right = piece
                # print(f"Bottom right piece: {bottom_right.symbol}")

        print(f"Turn: {turn}")
        print("Running bot logic...")
        
        if turn == "X":
            
            # Check if X has two pieces in a row
            if top_left.symbol == "X" and top_center.symbol == "X" and top_right.symbol == "Blank":
                self.click_position(3)
                return
            elif top_left.symbol == "X" and top_right.symbol == "X" and top_center.symbol == "Blank":
                self.click_position(2)
                return
            elif top_center.symbol == "X" and top_right.symbol == "X" and top_left.symbol == "Blank":
                self.click_position(1)
                return
            elif middle_left.symbol == "X" and center.symbol == "X" and middle_right.symbol == "Blank":
                self.click_position(6)
                return
            elif middle_left.symbol == "X" and middle_right.symbol == "X" and center.symbol == "Blank":
                self.click_position(5)
                return
            elif middle_right.symbol == "X" and center.symbol == "X" and middle_left.symbol == "Blank":
                self.click_position(4)
                return
            elif bottom_left.symbol == "X" and bottom_center.symbol == "X" and bottom_right.symbol == "Blank":
                self.click_position(9)
                return
            elif bottom_left.symbol == "X" and bottom_right.symbol == "X" and bottom_center.symbol == "Blank":
                self.click_position(8)
                return
            elif bottom_center.symbol == "X" and bottom_right.symbol == "X" and bottom_left.symbol == "Blank":
                self.click_position(7)
                return
            elif top_left.symbol == "X" and middle_left.symbol == "X" and bottom_left.symbol == "Blank":
                self.click_position(7)
                return
            elif top_left.symbol == "X" and bottom_left.symbol == "X" and middle_left.symbol == "Blank":
                self.click_position(4)
                return
            elif middle_left.symbol == "X" and bottom_left.symbol == "X" and top_left.symbol == "Blank":
                self.click_position(1)
                return
            elif top_center.symbol == "X" and center.symbol == "X" and bottom_center.symbol == "Blank":
                self.click_position(8)
                return
            elif top_center.symbol == "X" and bottom_center.symbol == "X" and center.symbol == "Blank":
                self.click_position(5)
                return
            elif center.symbol == "X" and bottom_center.symbol == "X" and top_center.symbol == "Blank":
                self.click_position(2)
                return
            elif top_right.symbol == "X" and middle_right.symbol == "X" and bottom_right.symbol == "Blank":
                self.click_position(9)
                return
            elif top_right.symbol == "X" and bottom_right.symbol == "X" and middle_right.symbol == "Blank":
                self.click_position(6)
                return
            elif middle_right.symbol == "X" and bottom_right.symbol == "X" and top_right.symbol == "Blank":
                self.click_position(3)
                return
            elif top_left.symbol == "X" and center.symbol == "X" and bottom_right.symbol == "Blank":
                self.click_position(9)
                return
            elif top_left.symbol == "X" and bottom_right.symbol == "X" and center.symbol == "Blank":
                self.click_position(5)
                return
            elif center.symbol == "X" and bottom_right.symbol == "X" and top_left.symbol == "Blank":
                self.click_position(1)
                return
            elif top_right.symbol == "X" and center.symbol == "X" and bottom_left.symbol == "Blank":
                self.click_position(7)
                return
            elif top_right.symbol == "X" and bottom_left.symbol == "X" and center.symbol == "Blank":
                self.click_position(5)
                return
            elif center.symbol == "X" and bottom_left.symbol == "X" and top_right.symbol == "Blank":
                self.click_position(3)
                return
            
            # Check if O has two pieces in a row
            if top_left.symbol == "O" and top_center.symbol == "O" and top_right.symbol == "Blank":
                self.click_position(3)
                return
            elif top_left.symbol == "O" and top_right.symbol == "O" and top_center.symbol == "Blank":
                self.click_position(2)
                return
            elif top_center.symbol == "O" and top_right.symbol == "O" and top_left.symbol == "Blank":
                self.click_position(1)
                return
            elif middle_left.symbol == "O" and center.symbol == "O" and middle_right.symbol == "Blank":
                self.click_position(6)
                return
            elif middle_left.symbol == "O" and middle_right.symbol == "O" and center.symbol == "Blank":
                self.click_position(5)
                return
            elif middle_right.symbol == "O" and center.symbol == "O" and middle_left.symbol == "Blank":
                self.click_position(4)
                return
            elif bottom_left.symbol == "O" and bottom_center.symbol == "O" and bottom_right.symbol == "Blank":
                self.click_position(9)
                return
            elif bottom_left.symbol == "O" and bottom_right.symbol == "O" and bottom_center.symbol == "Blank":
                self.click_position(8)
                return
            elif bottom_center.symbol == "O" and bottom_right.symbol == "O" and bottom_left.symbol == "Blank":
                self.click_position(7)
                return
            elif top_left.symbol == "O" and middle_left.symbol == "O" and bottom_left.symbol == "Blank":
                self.click_position(7)
                return
            elif top_left.symbol == "O" and bottom_left.symbol == "O" and middle_left.symbol == "Blank":
                self.click_position(4)
                return
            elif middle_left.symbol == "O" and bottom_left.symbol == "O" and top_left.symbol == "Blank":
                self.click_position(1)
                return
            elif top_center.symbol == "O" and center.symbol == "O" and bottom_center.symbol == "Blank":
                self.click_position(8)
                return
            elif top_center.symbol == "O" and bottom_center.symbol == "O" and center.symbol == "Blank":
                self.click_position(5)
                return
            elif center.symbol == "O" and bottom_center.symbol == "O" and top_center.symbol == "Blank":
                self.click_position(2)
                return
            elif top_right.symbol == "O" and middle_right.symbol == "O" and bottom_right.symbol == "Blank":
                self.click_position(9)
                return
            elif top_right.symbol == "O" and bottom_right.symbol == "O" and middle_right.symbol == "Blank":
                self.click_position(6)
                return
            elif middle_right.symbol == "O" and bottom_right.symbol == "O" and top_right.symbol == "Blank":
                self.click_position(3)
                return
            elif top_left.symbol == "O" and center.symbol == "O" and bottom_right.symbol == "Blank":
                self.click_position(9)
                return
            elif top_left.symbol == "O" and bottom_right.symbol == "O" and center.symbol == "Blank":
                self.click_position(5)
                return
            elif center.symbol == "O" and bottom_right.symbol == "O" and top_left.symbol == "Blank":
                self.click_position(1)
                return
            elif top_right.symbol == "O" and center.symbol == "O" and bottom_left.symbol == "Blank":
                self.click_position(7)
                return
            elif top_right.symbol == "O" and bottom_left.symbol == "O" and center.symbol == "Blank":
                self.click_position(5)
                return
            elif center.symbol == "O" and bottom_left.symbol == "O" and top_right.symbol == "Blank":
                self.click_position(3)
                return

            # Check if the center is empty
            if center.symbol == "Blank":
                self.click_position(5)
                return

            # Check if the corners are empty
            if top_left.symbol == "Blank":
                self.click_position(1)
                return
            elif top_right.symbol == "Blank":
                self.click_position(3)
                return
            elif bottom_left.symbol == "Blank":
                self.click_position(7)
                return
            elif bottom_right.symbol == "Blank":
                self.click_position(9)
                return

            # Check if the sides are empty
            if top_center.symbol == "Blank":
                self.click_position(2)
                return
            elif middle_left.symbol == "Blank":
                self.click_position(4)
                return
            elif middle_right.symbol == "Blank":
                self.click_position(6)
                return
            elif bottom_center.symbol == "Blank":
                self.click_position(8)
                return

            # If no winning move is found, click on the first available empty cell
            for piece in pieces:
                if piece.symbol == "Blank":
                    self.click_position(piece.cell[0] * 3 + piece.cell[1] + 1)
                    break

        
        

        
        
    
            

    