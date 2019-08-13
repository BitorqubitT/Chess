import piece
import pygame

king = "C:/Users/thier/PycharmProjects/chess/images/king.png"
king = pygame.image.load(king)
# We let the Knight class pass the image to its super class where it is loaded
class King(piece.Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour, type)
        self.type = king
        self.colour = colour

    def generate_moves(self, x, y):
        # The fact that I add the old position as a valid position might give problems later on in the game.
        # King
        moves = []
        moves.append((x, y))
        moves.append((x, y + 100))
        moves.append((x, y - 100))
        moves.append((x + 100, y))
        moves.append((x - 100, y))
        moves.append((x + 100, y + 100))
        moves.append((x - 100, y - 100))
        moves.append((x - 100, y + 100))
        moves.append((x + 100, y - 100))
        return moves
