import piece
import pygame

knight = "C:/Users/thier/PycharmProjects/chess/images/Knight.png"
knight = pygame.image.load(knight)
# We let the Knight class pass the image to its super class where it is loaded
class Knight(piece.Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour, type)
        self.type = knight
        self.colour = colour

    def generate_moves(self, x, y):
        # Knight
        moves = []
        moves.append((x + 200, y - 100))
        moves.append((x + 100, y - 200))
        moves.append((x - 100, y - 200))
        moves.append((x - 200, y - 100))
        moves.append((x + 200, y + 100))
        moves.append((x + 100, y + 200))
        moves.append((x - 100, y + 200))
        moves.append((x - 200, y + 100))
        return moves

