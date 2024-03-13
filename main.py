import mss
from game import Game
import cv2
import numpy as np
import time
import keyboard

sct = mss.mss()

mon = sct.monitors[1]
dimensions = {
    "top": mon['top'] + 330,
    "left": mon['left'] + 700,
    "width": 530,
    "height": 530
}

o_needle = cv2.imread('./images/o_needle.png', cv2.IMREAD_UNCHANGED)
x_needle = cv2.imread('./images/x_needle.png', cv2.IMREAD_UNCHANGED)
blank_needle = cv2.imread('./images/blank_needle.png', cv2.IMREAD_UNCHANGED)

game = Game(dimensions)

while True:
    board = np.array(sct.grab(dimensions))
    game.scan_board(board, o_needle)
    game.scan_board(board, x_needle)
    game.scan_board(board, blank_needle)
    if keyboard.is_pressed("q"):
        break
    cv2.imshow("Board", board)
    cv2.waitKey(1)
    time.sleep(.10)
    game_state = game.get_game_state()
    print(game_state)
    if game_state == "Game not started":
        continue
    elif game_state == "Game in progress":
        print("Game in progress")
    else:
        print("Game over")
        break