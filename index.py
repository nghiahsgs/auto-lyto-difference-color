import pyautogui
import time
from utils import *

for i_try in range(50):
    pyautogui.screenshot('screenshot.png')

    col_start = 737  # coord_x
    row_start = 392  # coord_y
    col_end = 1178
    row_end = 980
    width = col_end-col_start
    height = row_end-row_start

    crop_img('screenshot.png', row_start, col_start, width, height)

    row, col = find_cood_difference_color_in_image('screenshot.png')

    coord_click_y = row_start+row+5
    coord_click_x = col_start+col

    pyautogui.click(coord_click_x, coord_click_y)
    time.sleep(0.15)