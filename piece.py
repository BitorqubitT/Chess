import pygame

size = width, height = 800, 800
screen = pygame.display.set_mode(size)

class Piece():
    def __init__(self, x, y, type, colour):
        self.x = x
        self.y = y
        self.type = type
        self.size = 100
        self.side = colour

    def display(self):
        # - 50 to center them change this later
        screen.blit(self.type, (self.x - 50, self.y - 50))



