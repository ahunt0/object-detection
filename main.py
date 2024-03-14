import mss
from game import Game
from bot import Bot
import cv2
import numpy as np
import time
import keyboard
import subprocess
import sys

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
new_game_needle = cv2.imread('./images/new_game_needle.png', cv2.IMREAD_UNCHANGED)

game = Game(dimensions)
bot = Bot(game)

while True:
    board = np.array(sct.grab(dimensions))
    if keyboard.is_pressed("q"):
        break
    if game.is_game_over(board, new_game_needle):
        print("Game over")
        continue
    game.scan_board(board, o_needle, "O")
    game.scan_board(board, x_needle, "X")
    game.scan_board(board, blank_needle, "Blank")
    game_state = game.get_game_state()
    if game.turn == "X":
        bot.evaluate_board(game.pieces, game.turn)
    print(game_state)
    game.pieces.clear()
    cv2.namedWindow("Board", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Board", cv2.WND_PROP_TOPMOST, 1)
    cv2.imshow("Board", board)
    cv2.waitKey(1)
    time.sleep(.10)
    if game_state == "Game not started":
        continue
    elif game_state == "Game in progress":
        print("Game in progress")
    else:
        print("Game over")
        break