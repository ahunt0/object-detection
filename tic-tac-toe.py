import cv2
import numpy as np
import pyautogui
import mss
from time import sleep
import keyboard

sct = mss.mss()

dimensions = {
    "top": 330,
    "left": 700,
    "width": 530,
    "height": 530
}

# board_img = np.array(sct.grab({"top": 330, "left": 700, "width": 530, "height": 530}))
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

def find(board, needle):
    result = cv2.matchTemplate(board, needle, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) # min = worst match, max = best match
    
    threshold = 0.8
    
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

        # print(f"    @ {center_x}, {center_y}, position: {position}")

        # Label the rectangles
        if needle is x_img:
            cv2.putText(board, 'X', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        elif needle is o_img:
            cv2.putText(board, 'O', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(board, 'Blank', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Draw a rectangle around the rectangles
        cv2.rectangle(board, (x, y), (x + w, y + h), (0, 255, 0), 2)

while True:
    board_img = np.array(sct.grab(dimensions))
    find(board_img, blank_img)
    find(board_img, x_img)
    find(board_img, o_img)
    cv2.imshow('Board', board_img)
    cv2.waitKey(1)
    sleep(.10)
    if keyboard.is_pressed('q'):
        break

# find(board_img, blank_img)
# find(board_img, x_img)
# find(board_img, o_img)

# for piece in pieces:
#     print(f"Piece: {piece.img}\n    @ {piece.x}, {piece.y}, position: {piece.position}")

# cv2.imshow('Board', board_img)
# cv2.waitKey()
# cv2.destroyAllWindows()