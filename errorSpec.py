

class Error(Exception):
    pass

class PositionLengthError(Error):
    """Raised when position size does not match expected dimensions"""
    def __init__(self, size_flag):
        if size_flag == -1:
            self.message = "Too few positional arguments. Check length of position tuple"
        elif size_flag == 1:
            self.message = "Too many positional arguments. Check length of position tuple"