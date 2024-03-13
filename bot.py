# bot logic
import pyautogui
from game import Game

class Bot:
    def __init__(self, game):
        self.game = game
        self.turn = "O"

    