import pygame
import board
import knight
import king
import pawn
import queen
import rook
import bishop
import math

white = (255,255,255)
screen = pygame.display.set_mode((800,800))
board = board.Board(800, 800)
size = width, height = 800, 800

# Check of er friendly moves
# This is no bueno I have to check i[0] and i[1].
def legal_move_checker(colour, legalmoves):
    # Later on I can clean this up. Put black and white into 1 list and check for x,y,colour.
    checkmoves = []
    newmoves = []
    for i in allpieces:
        if i.colour is colour:
            checkmoves.append((i.x, i.y))
    for i in legalmoves:
        if i not in checkmoves:
            newmoves.append(i)
    return newmoves

def check_for_enemy(colour, x, y):
    # We don't have to check for colour since legal_move_checker already does this.
    for i in allpieces:
        if (i.x, i.y) == (x, y):
            return i
    return False

# should also have a function that checks if an enemy pawn is located and remove it from the board.
# find_horse
def findHorse(horse, x, y):
    for h in horse:
        # Check if mouse(x,y) is within the range of origin of image + length(x,y) we convert the mouse position to int.
        # Changed this since the pieces are now centered.
        if int(x) in range(h.x - 50, h.x + 50) and int(y) in range(h.y - 50, h.y + 50):
            return h
    return None

#set point so we can test the detection from our horse.
# find_closest_point
def findclosestPoint(points, x, y):
    for p in points:
        if math.hypot(p[0] - x, p[1] - y) <= int(width/8) :
            return p[0], p[1]
    return None

def display(x,y):
    pygame.draw.circle(screen,(255, 0, 0), (x, y), 5)

WHITE = [("Pawn",50,150),
         ("Pawn",150,150),
         ("Pawn",250,150),
         ("Pawn",350,150),
         ("Pawn",450,150),
         ("Pawn",550,150),
         ("Pawn",650,150),
         ("Pawn",750,150),
         ("Knight",150,50),
         ("Knight",650,50),
         ("Bishop",250,50),
         ("Bishop",550,50),
         ("King",450,50),
         ("Queen",350,50),
         ("Rook",50,50),
         ("Rook",750,50),
         ]

BLACK = [("Pawn",50,650),
         ("Pawn",150,650),
         ("Pawn",250,650),
         ("Pawn",350,650),
         ("Pawn",450,650),
         ("Pawn",550,650),
         ("Pawn",650,650),
         ("Pawn",750,650),
         ("Knight",150,750),
         ("Knight",650,750),
         ("Bishop",250,750),
         ("Bishop",550,750),
         ("King",450,750),
         ("Queen",350,750),
         ("Rook",50,750),
         ("Rook",750,750),
         ]

WHITE2 = []
BLACK2 = []

# How I append horse3 to a list is something we don't want to do. Just immediately append them to the list.
# Look into cases which should be used here and see if it is less code and/or more effective.
# Make a function Init pieces.
# This could be done wayyyyyyyyyyyyy nicer
for i in WHITE:
    if i[0] == "Pawn":
        WHITE2.append(pawn.Pawn(i[1],i[2], "WHITE"))
    elif i[0] == "Knight":
        WHITE2.append(knight.Knight(i[1],i[2], "WHITE"))
    elif i[0] == "Bishop":
        WHITE2.append(bishop.Bishop(i[1],i[2], "WHITE"))
    elif i[0] == "King":
        WHITE2.append(king.King(i[1],i[2], "WHITE"))
    elif i[0] == "Queen":
        WHITE2.append(queen.Queen(i[1],i[2], "WHITE"))
    elif i[0] == "Rook":
        WHITE2.append(rook.Rook(i[1],i[2], "WHITE"))

for i in BLACK:
    if i[0] == "Pawn":
        BLACK2.append(pawn.Pawn(i[1],i[2], "BLACK"))
    elif i[0] == "Knight":
        BLACK2.append(knight.Knight(i[1],i[2], "BLACK"))
    elif i[0] == "Bishop":
        BLACK2.append(bishop.Bishop(i[1],i[2], "BLACK"))
    elif i[0] == "King":
        BLACK2.append(king.King(i[1],i[2], "BLACK"))
    elif i[0] == "Queen":
        BLACK2.append(queen.Queen(i[1],i[2], "BLACK"))
    elif i[0] == "Rook":
        BLACK2.append(rook.Rook(i[1],i[2], "BLACK"))


allpieces = BLACK2 + WHITE2
points = []




for x in range(50,800,100):
    for y in range(50,800,100):
        points.append((x,y))

selected_piece = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # This has to stay here
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_piece = findHorse(allpieces, mouseX, mouseY) # Ik moest stoppen met het gebruiken van indexing en gewoon de param opvragen................
            # Maybe remove this logic (under) and put old position as a variable in piece and we update it here.?
            # Maybe this is the problem old or new python?
            oldposition_X, oldposition_Y = selected_piece.x, selected_piece.y
            # generate
        elif event.type == pygame.MOUSEBUTTONUP:
            # Create function that check for closest point.
            # Then the function maps it to that point.
            if findclosestPoint(points, mouseX, mouseY) == None:
                selected_piece.x = oldposition_X
                selected_piece.y = oldposition_Y
                selected_piece = None
            #check for valid move otherwise go back to old position.
            else:
                checker = True
                for i in legal_move_checker(selected_piece.colour, selected_piece.generate_moves(oldposition_X, oldposition_Y)):
                    if findclosestPoint(points, mouseX, mouseY)[0] ==  i[0] and findclosestPoint(points, mouseX, mouseY)[1] ==  i[1]:
                        # Check if we hit an enemy piece if so remove that piece.
                        # We can do this a lot better, maybe put the remove part in the function.
                        if check_for_enemy(selected_piece.colour, i[0], i[1]) is not False:
                            allpieces.remove(check_for_enemy(selected_piece.colour, i[0], i[1]))
                        selected_piece.x = findclosestPoint(points, mouseX, mouseY)[0]
                        selected_piece.y = findclosestPoint(points, mouseX, mouseY)[1]
                        checker = False
                        break
                if checker is True:
                    selected_piece.x = oldposition_X
                    selected_piece.y = oldposition_Y
                selected_piece = None

    if selected_piece:
        mouseX, mouseY = pygame.mouse.get_pos()
# save the starting position which we can use later on to reset the place.
        selected_piece.x = mouseX
        selected_piece.y = mouseY


# we gebruiken dit om de achtergrond schoon te maken
    board.drawBoard()
    for i in points:
        display(i[0], i[1])
    for i in allpieces:
        i.display()
    pygame.display.flip()