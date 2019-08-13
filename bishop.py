import piece
import pygame

bishop = "C:/Users/thier/PycharmProjects/chess/images/Bishop.png"
bishop = pygame.image.load(bishop)
# We let the Knight class pass the image to its super class where it is loaded
class Bishop(piece.Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour, type)
        self.type = bishop
        self.colour = colour

    def generate_moves(self, x, y):
        # Bischop
        moves = []
        i = 1
        while i < 8:
            moves.append((x + 100 * i, y - 100 * i))
            moves.append((x - 100 * i, y + 100 * i))
            moves.append((x - 100 * i, y - 100 * i))
            moves.append((x + 100 * i, y + 100 * i))
            i += 1
        moves2 = []
        for i in moves:
            # int between, with steps 100.
            if i[0] >= 50 and i[1] >= 50 and i[0] <= 750 and i[1] <= 750:
                moves2.append(i)
            else:
                continue
        return moves2