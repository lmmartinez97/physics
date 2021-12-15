import pygame.display
import sys
from errorSpec import *

def translate2D(position):
    try:
        if len(position) < 2:
            size_flag = -1
            raise PositionLengthError(size_flag)
        elif len(position) > 2:
            size_flag = 1
            raise PositionLengthError(size_flag)
    except PositionLengthError as e:
        print(e.message)
        sys.exit(1)
    w, h = pygame.display.get_window_size()
    x_ = int(position[0] + w/2)
    y_ = int(-position[1] + h/2)
    return (x_, y_)
