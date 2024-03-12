import cv2
import numpy as np
import mss
from time import sleep
import keyboard
import pyautogui
import random

sct = mss.mss()

mon = sct.monitors[1]
dimensions = {
    "top": mon['top'] + 330,
    "left": mon['left'] + 700,
    "width": 530,
    "height": 530
}

o_img = cv2.imread('./images/o_needle.png', cv2.IMREAD_UNCHANGED)
x_img = cv2.imread('./images/x_needle.png', cv2.IMREAD_UNCHANGED)
blank_img = cv2.imread('./images/blank_needle.png', cv2.IMREAD_UNCHANGED)

def image_type(img):
    if img is x_img:
        return "X"
    elif img is o_img:
        return "O"
    else:
        return "Blank"
    
class Piece:
    def __init__(self, img, x, y, position):
        self.img = image_type(img)
        self.x = x
        self.y = y
        self.position = position

pieces = []

def game_state(board):
    # Count the number of X and O pieces
    x_count = sum(piece.img == "X" for piece in board)
    o_count = sum(piece.img == "O" for piece in board)

    # Check for game start
    if x_count + o_count == 0:
        return "Game not started", None
    elif o_count > x_count:
        return "Game in progress", "X"
    else:
        return "Game in progress", "O"
    

def find(board, needle):
    result = cv2.matchTemplate(board, needle, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) # min = worst match, max = best match
    
    threshold = 0.7 # If you're not getting matches try lowering this value
    
    # Find the locations of the best matches
    yloc, xloc = np.where(result >= threshold)

    rectangles = []

    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(needle.shape[1]), int(needle.shape[0])])
        rectangles.append([int(x), int(y), int(needle.shape[1]), int(needle.shape[0])])

    # Group rectangles to avoid duplicates
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    print(f"{image_type(needle)} count: {len(rectangles)}")

    # Calculate the grid cell size
    grid_width = board.shape[1] // 3
    grid_height = board.shape[0] // 3

    # Draw grid lines for debugging
    for i in range(3):
        for j in range(3):
            cv2.rectangle(board, (i * grid_width, j * grid_height), ((i + 1) * grid_width, (j + 1) * grid_height), (0, 255, 0), 2)
    
    for (x, y, w, h) in rectangles:
        # Calculate the center of the rectangle
        center_x = x + w // 2
        center_y = y + h // 2

        # Draw the center of the rectangle
        cv2.circle(board, (center_x, center_y), 5, (0, 0, 255), -1)

        # Calculate the grid cell coordinates
        grid_x = center_x // grid_width
        grid_y = center_y // grid_height

        # Convert the grid cell coordinates to a number from 1 to 9
        position = grid_y * 3 + grid_x + 1

        # if position is already taken overwrite it
        for piece in pieces:
            if piece.position == position:
                pieces.remove(piece)
                break

        pieces.append(Piece(needle, x, y, position)) # Add the piece to the list of pieces

        # Label the rectangles
        if needle is x_img:
            cv2.putText(board, 'X', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif needle is o_img:
            cv2.putText(board, 'O', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.putText(board, f"{position}", (grid_x * grid_width + 5, grid_y * grid_height + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Draw a rectangle around the rectangles
        cv2.rectangle(board, (x, y), (x + w, y + h), (0, 255, 0), 2)

class Bot:
    def __init__(self):
        self.board = []
        self.turn = game_state(self.board)[1]
        self.game_state = game_state(self.board)[0]

    def update_board(self):
        self.board = pieces
        self.game_state, self.turn = game_state(self.board)

    def check_winning_move(self, piece):
        # Check rows, columns, and diagonals for winning move
        lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for line in lines:
            if all(p.position in line for p in self.board if p.img == piece):
                return True
        return False

    def find_empty_cells(self):
        return [piece.position for piece in self.board if piece.img == "Blank"]

    def click_position(self, position):
        # Calculate the coordinates of the center of the cell based on the position
        cell_width = dimensions['width'] // 3
        cell_height = dimensions['height'] // 3
        row = (position - 1) // 3
        col = (position - 1) % 3
        x = dimensions['left'] + cell_width * col + cell_width // 2
        y = dimensions['top'] + cell_height * row + cell_height // 2
        # Click on the calculated position
        pyautogui.click(x, y)

    def make_move(self):
        if self.game_state == "Game not started":
            return
        elif self.game_state == "Game in progress":
            if self.turn == "O":
                print("Player's turn")
            else:
                print("Bot's turn")

                # Get available empty positions
                empty_positions = self.find_empty_cells()

                # Try to find a winning move for the bot
                for pos in empty_positions:
                    test_board = self.board.copy()
                    test_board.append(Piece(o_img, 0, 0, pos))
                    if self.check_winning_move("O"):
                        print("Making winning move at position:", pos)
                        self.click_position(pos)
                        return

                # Try to block player's winning move
                for pos in empty_positions:
                    test_board = self.board.copy()
                    test_board.append(Piece(x_img, 0, 0, pos))
                    if self.check_winning_move("X"):
                        print("Blocking player's winning move at position:", pos)
                        self.click_position(pos)
                        return

                # If no immediate winning or blocking move, choose a winning move based on prior moves
                for pos in empty_positions:
                    test_board = self.board.copy()
                    test_board.append(Piece(o_img, 0, 0, pos))
                    if self.check_winning_move("O"):
                        print("Making winning move at position:", pos)
                        self.click_position(pos)
                        return

                # If no winning move is found, choose the first available empty position
                if empty_positions:
                    pos = empty_positions[0]
                    print("Making move at position:", pos)
                    self.click_position(pos)


bot = Bot()

while True:
    board_img = np.array(sct.grab(dimensions))
    find(board_img, blank_img)
    find(board_img, x_img)
    find(board_img, o_img)
    cv2.imshow('Board', board_img)
    cv2.waitKey(1)
    sleep(.10)
    print(f"Game state: {game_state(pieces)[0]}")
    print(f"Turn: {game_state(pieces)[1]}")
    bot.update_board()
    bot.make_move()
    if keyboard.is_pressed('q'):
        break
