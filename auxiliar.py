from errorSpec import *

def translate2D(*position):
    try:
        if len(position) < 2:
            size_flag = -1
            raise PositionLengthError(size_flag)
        elif len(position) > 2:
            size_flag = 1
            raise PositionLengthError(size_flag)
    except PositionLengthError as e:
        print(e.message)