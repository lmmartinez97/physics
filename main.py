import pygame.time

from SimulationWindow import GameWindow
import auxiliar
myWindow = GameWindow(width = 1200, height = 800)
game_clock = pygame.time.Clock()


def main():
    myWindow.window_config()
    #Main game loop
    while not (myWindow.exit_window()):
        game_clock.tick(60)
        myWindow.draw_frame()

if __name__ == "__main__":
    main()