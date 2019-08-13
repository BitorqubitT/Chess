import piece
import pygame

pawn = "C:/Users/thier/PycharmProjects/chess/images/Pawns.png"
pawn = pygame.image.load(pawn)
# We let the Knight class pass the image to its super class where it is loaded
class Pawn(piece.Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour, type)
        self.type = pawn
        self.colour = colour

    def generate_moves(self, x, y):
        # Pawn
        # Should switch the pieces. Black on top, WHITE on the bottom.
        print(x,y, "startposition")
        moves = []
        if self.colour is "BLACK":
            moves.append((x, y - 100))
        elif self.colour is "WHITE":
            moves.append((x, y + 100))
        return moves

