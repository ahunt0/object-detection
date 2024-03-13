# scanning & game logic
import cv2
from piece import Piece
import numpy as np

class Game:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.pieces = []
        self.game_state = "Game not started"
        self.turn = "O"

    def get_game_state(self):
        # Count the number of X and O pieces
        x_count = sum(piece.symbol == "X" for piece in self.pieces)
        o_count = sum(piece.symbol == "O" for piece in self.pieces)

        # Check for game start
        if x_count + o_count == 0:
            self.game_state = "Game not started"
        elif o_count > x_count:
            self.game_state = "Game in progress"
        else:
            self.game_state = "Game in progress"
        
        return self.game_state

    def scan_board(self, board, needle):
        """
        Scan the board for pieces and update the game state.

        :param board: The board image to scan.
        """
        # Clear the pieces list
        self.pieces.clear()

        result = cv2.matchTemplate(board, needle, cv2.TM_CCOEFF_NORMED)

        threshold = 0.7  # If you're not getting matches try lowering this value
        yloc, xloc = np.where(result >= threshold)

        # Find the locations of the best matches
        rectangles = []

        # Create rectangles around the best matches
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(needle.shape[1]), int(needle.shape[0])])
            rectangles.append([int(x), int(y), int(needle.shape[1]), int(needle.shape[0])])

        # Group the rectangles to avoid duplicates
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

        # Calculate the grid cell size
        cell_w = self.dimensions["width"] // 3
        cell_h = self.dimensions["height"] // 3

        # Draw grid lines
        for i in range(3):
            for j in range(3):
                cv2.rectangle(board, (i * cell_w, j * cell_h), ((i + 1) * cell_w, (j + 1) * cell_h), (0, 255, 0), 2)

        for(x, y, w, h) in rectangles:
            # Calculate the cell position
            cell = (x // cell_w, y // cell_h)

            # If the cell is already occupied, overwrite the piece
            for piece in self.pieces:
                if piece.cell == cell:
                    self.pieces.remove(piece)
                    break

            # Add the piece to the pieces list
            found_piece = Piece(x, y, w, h, cell, needle)
            self.pieces.append(found_piece)
            print(f"Found {Piece.image_type(found_piece, needle)} at {cell}")

        # label the board
        for piece in self.pieces:
            cv2.rectangle(board, (piece.x, piece.y), (piece.x + piece.w, piece.y + piece.h), (0, 0, 255), 2)
            

        
    

