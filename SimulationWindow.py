import sys, os
import pygame
import datetime

from pygame.constants import *
from pygame.color import THECOLORS
from pygame.locals import *

class GameWindow:
    def __init__(self, background_color = (255, 255, 255), width = 1080, height = 720):
        self.background_color = background_color
        self.windowSize = [width, height]

    def window_config(self, caption = 'Test'):
        pygame.init()
        self.screen = pygame.display.set_mode(self.windowSize)
        pygame.display.set_caption(caption)
        self.screen.fill(self.background_color)

    def draw_frame(self):
        pygame.display.update()

    def erase_screen(self):
        self.screen.fill(self.background_color)

    def draw_objects(selfself, objects):
        for object in objects:


    def exit_window(self):
        ret = 0
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if K_ESCAPE:
                    pygame.quit()
                    ret = 1
        return ret