import pygame.time
import Objects
from SimulationWindow import GameWindow
import pygame.color
from auxiliar import translate2D

BLACK = (0x0, 0x0, 0x0)
RED = (0xFF, 0x00, 0x00)
BLUE = (0x00, 0xFF, 0x00)
GREEN = (0x00, 0x00, 0xFF)
WHITE = (0xFF, 0xFF, 0xFF)


myWindow = GameWindow(width = 1200, height = 800)
game_clock = pygame.time.Clock()


def main():
    myWindow.window_config()
    #Main game loop
    while not (myWindow.exit_window()):
        game_clock.tick(60)
        p1 = Objects.PointMass(mass = 250, position = translate2D((0,0)),  color = RED)
        p2 = Objects.PointMass(mass = 250, position = translate2D((100,100)), color = BLACK)
        p3 = Objects.Box(250, 20, 20, (-100, -100), BLUE)
        myWindow.draw_frame(objects = [p1, p2, p3])

if __name__ == "__main__":
    main()