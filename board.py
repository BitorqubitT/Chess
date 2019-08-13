import pygame
import itertools


class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    #teken een vierkant dan next
    #rotate de kleuren met NEXT
    # set kleuren ergens
    def drawSquare(self, color, x,y):
        #first x, y are position on the screen. The rest is size of rect.
        pygame.draw.rect(self.screen, (color), (x,y, int(self.width/8), int(self.height/8)))

    def drawBoard(self):
        x = 0
        y = 0
        black = (201, 133, 255)
        white = (160, 255, 255)
        color = itertools.cycle((white, black))
        for x in range(0, self.width, int(self.width/8)):
            for y in range(0, self.height, int(self.height/8)):
                self.drawSquare(next(color), x, y)
            next(color)


