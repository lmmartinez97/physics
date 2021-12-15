
from pygame.draw import *
from math import *
import numpy as np

class PointMass:
    def __init__(self, mass = 1.0, color = (0, 0, 0)):
        self.mass = mass
        self.radius = int(sqrt(25*self.mass))
        self.color = color

    def show(self, surface, center):
        ellipse(surface, self.color, center, self.radius)