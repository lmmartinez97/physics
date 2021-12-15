import pygame
from pygame.draw import *
from pygame import Rect
from math import *
import numpy as np

class PointMass:
    def __init__(self, mass = 1.0, position = (0, 0), color = (0, 0, 0)):
        self.mass = mass
        self.radius = sqrt(4*self.mass/pi)
        self.color = color
        self.position = position

    def show(self, surface):
        return circle(surface, self.color, self.position, self.radius)

class Box:
    def __init__(self, mass = 1.0, width = 10, height = 10, position = (0,0), color = (0, 0, 0)):
        self.mass = mass
        self.width = width
        self.height = height
        self.color = color
        self.position = position
        self.top, self.left = (self.position[0] - width/2, self.position[1] - height/2)
        self.rectangle = Rect(self.left, self.top, self.width, self.height)

    def show(self, surface):
        return rect(surface, self.color, self.rectangle)