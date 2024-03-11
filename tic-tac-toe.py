import cv2
import numpy as np

board_img = cv2.imread('board.png', cv2.IMREAD_UNCHANGED)
board2_img = cv2.imread('board2.png', cv2.IMREAD_UNCHANGED)
o_img = cv2.imread('o_needle.png', cv2.IMREAD_UNCHANGED)
x_img = cv2.imread('x_needle.png', cv2.IMREAD_UNCHANGED)
blank_img = cv2.imread('blank_needle.png', cv2.IMREAD_UNCHANGED)

def find_xo(img, needle, name):
    result = cv2.matchTemplate(img, needle, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(f"{name}: {int(max_val * 100)}%, {max_loc}")
    w = needle.shape[1]
    h = needle.shape[0]
    cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
    cv2.putText(img, f'\"{name}\" {int(max_val * 100)}%', (max_loc[0] - 5, max_loc[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.waitKey()
    cv2.destroyAllWindows()

find_xo(board2_img, o_img, 'O')
find_xo(board2_img, x_img, 'X')
find_xo(board2_img, blank_img, 'Blank')

cv2.imshow('Board2', board2_img)
cv2.waitKey()
cv2.destroyAllWindows()