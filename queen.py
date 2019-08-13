import piece
import pygame

queen = "C:/Users/thier/PycharmProjects/chess/images/Queen.png"
queen = pygame.image.load(queen)
# We let the Knight class pass the image to its super class where it is loaded
class Queen(piece.Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour, type)
        self.type = queen
        self.colour = colour

    def generate_moves(self, x, y):
        # Rook
        moves = []
        moves2 = []
        # 150, 150
        i = 0
        j = 0
        # Rook part
        while i < 8:
            moves.append((x, 50 + 100 * i))
            moves.append((50 + 100 * i, y))
            i += 1
        # Bischop part
        while j < 8:
            moves.append((x + 100 * j, y - 100 * j))
            moves.append((x - 100 * j, y + 100 * j))
            moves.append((x - 100 * j, y - 100 * j))
            moves.append((x + 100 * j, y + 100 * j))
            j += 1
        # Check if the move are within the boards boundaries.
        for i in moves:
            # int between, with steps 100.
            if i[0] >= 50 and i[1] >= 50 and i[0] <= 750 and i[1] <= 750:
                moves2.append(i)
            else:
                continue
        return moves2