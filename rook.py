import piece
import pygame

rook = "C:/Users/thier/PycharmProjects/chess/images/Rook.png"
rook = pygame.image.load(rook)
# We let the Knight class pass the image to its super class where it is loaded
class Rook(piece.Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour, type)
        self.type = rook
        self.colour = colour

    def generate_moves(self, x, y):
        # Rook
        moves = []
        # 150, 150
        i = 0
        while i < 8:
            moves.append((x, 50 + 100 * i))
            moves.append((50 + 100 * i, y))
            i += 1
        return moves