import os, sys
import pygame
from pygame.locals import *

class BoardGrid(pytgame.sprite.Sprite):
    def __init__(self, width, height):


class DestinationBlock(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

def image_loader(name, colorKey=None):
    image_path = os.path.join("assets", name)
    try:
        image = pygame.image.load(image_path)
    except pygame.error as message:
        print("Couln't load specified image {0}".format(name))
        raise SystemExit(message)

def main_game_loop():
    while 1:
        pygame.init()
        screen = pygame.display.set_mode((468, 60))


if __name__ == "__main__":
    main_game_loop()